#!/usr/bin/env python3
import os
import re
import time
import hashlib
import logging
import traceback
import sys
from datetime import datetime, timezone
from typing import List, Dict, Optional
from urllib.parse import urlparse

# Keep native libs from over-parallelizing on small VMs
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

import requests
from bs4 import BeautifulSoup
import trafilatura
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from dotenv import load_dotenv
import xml.etree.ElementTree as ET

# OpenAI v1 SDK
from openai import OpenAI

# Pinecone v5 SDK
from pinecone import Pinecone, ServerlessSpec

load_dotenv()


def _read_env(name: str, default: Optional[str] = None, required: bool = False) -> str:
    value = os.environ.get(name)
    if value is not None:
        value = value.strip()
    if not value:
        if required and default is None:
            raise RuntimeError(f"Environment variable {name} is required but missing or empty")
        return default or ""
    return value


# -------------------- Config via env --------------------
PINECONE_API_KEY = _read_env("PINECONE_API_KEY", required=True)
PINECONE_INDEX   = _read_env("PINECONE_INDEX", default="sbcc-docs")
PINECONE_CLOUD   = _read_env("PINECONE_CLOUD", default="aws")
PINECONE_REGION  = _read_env("PINECONE_REGION", default="us-east-1")
OPENAI_API_KEY   = _read_env("OPENAI_API_KEY", required=True)
EMBED_MODEL      = _read_env("EMBED_MODEL", default="text-embedding-3-large")
PINECONE_NAMESPACE = _read_env("PINECONE_NAMESPACE", default="")  # optional
MAX_EXTRACT_CHARS = int(_read_env("MAX_EXTRACT_CHARS", default="400000"))      # per-page cap

# ------------- optional tiktoken (lazy) -------------
_TIKTOKEN_ENCODER = None
def get_encoder():
    global _TIKTOKEN_ENCODER
    if _TIKTOKEN_ENCODER is None:
        import tiktoken
        _TIKTOKEN_ENCODER = tiktoken.get_encoding("cl100k_base")
    return _TIKTOKEN_ENCODER

# -------------------- Logging --------------------
def setup_logging(verbose: bool, log_file: Optional[str]):
    level = logging.DEBUG if verbose else logging.INFO
    handlers = [logging.StreamHandler(sys.stdout)]
    if log_file:
        handlers.append(logging.FileHandler(log_file, encoding="utf-8"))
    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=handlers,
    )

log = logging.getLogger("sitemap2pinecone")

# -------------------- HTTP --------------------
class NotFound(Exception): pass

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=8),
       retry=retry_if_exception_type((requests.RequestException,)))
def http_get(url: str, timeout=20) -> requests.Response:
    log.debug(f"HTTP GET {url}")
    resp = requests.get(url, timeout=timeout, headers={"User-Agent": "SiteSitemapScraper/1.0"})
    if resp.status_code in (404, 410):
        raise NotFound(f"{resp.status_code} for {url}")
    resp.raise_for_status()
    return resp

SitemapEntry = Dict[str, Optional[str]]  # keys: url, lastmod


# -------------------- Sitemap --------------------
def parse_sitemap(url: str) -> List[SitemapEntry]:
    """Recursively parse sitemap and return list of (url, lastmod) pairs."""
    r = http_get(url)
    soup = BeautifulSoup(r.content, "xml")
    entries: List[SitemapEntry] = []

    # <sitemapindex> case
    sitemapindex = soup.find("sitemapindex")
    if sitemapindex:
        for sm_loc in sitemapindex.find_all("loc"):
            if not sm_loc.text:
                continue
            child = sm_loc.text.strip()
            if not child:
                continue
            entries.extend(parse_sitemap(child))
        return entries

    url_nodes = soup.find_all("url")
    for node in url_nodes:
        loc_tag = node.find("loc")
        if not loc_tag or not loc_tag.text:
            continue
        loc_text = loc_tag.text.strip()
        if not loc_text:
            continue
        lastmod_tag = node.find("lastmod")
        lastmod_text = None
        if lastmod_tag and lastmod_tag.text:
            lastmod_text = lastmod_tag.text.strip() or None
        entries.append({"url": loc_text, "lastmod": lastmod_text})

    return entries

# -------------------- Extraction --------------------
def extract_main_html(full_html: str, css_selector: Optional[str]) -> str:
    """Return HTML string of the selected container or the original HTML."""
    if not css_selector:
        return full_html
    try:
        soup = BeautifulSoup(full_html, "lxml")
        for tag in soup(["script", "style", "noscript"]):
            tag.decompose()
        node = soup.select_one(css_selector)
        if node:
            return str(node)
    except Exception:
        pass
    return full_html

def clean_text(full_html: str, base_url: str, css_selector: Optional[str]) -> str:
    """Prefer extracting from a specific CSS container, fall back to full-page, then simple HTML→text."""
    fragment_html = extract_main_html(full_html, css_selector)
    extracted = trafilatura.extract(
        fragment_html,
        url=base_url,
        include_links=False,
        include_comments=False,
        favor_recall=False,
    )
    if extracted and extracted.strip():
        return extracted.strip()

    extracted_full = trafilatura.extract(
        full_html,
        url=base_url,
        include_links=False,
        include_comments=False,
        favor_recall=False,
    )
    if extracted_full and extracted_full.strip():
        return extracted_full.strip()

    soup = BeautifulSoup(fragment_html, "lxml")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    text = soup.get_text(separator="\n").strip()
    return re.sub(r"\n{3,}", "\n\n", text)

# -------------------- Chunking --------------------
def chunk_text(text: str,
               use_tiktoken: bool,
               chunk_tokens: int = 800,
               overlap_tokens: int = 80,
               chunk_chars: int = 4000,
               overlap_chars: int = 400) -> List[str]:
    """Chunk by tokens (tiktoken) or fallback to plain character windows."""
    if use_tiktoken:
        enc = get_encoder()  # lazy, global
        toks = enc.encode(text)
        chunks: List[str] = []
        start = 0
        while start < len(toks):
            end = min(len(toks), start + chunk_tokens)
            chunk = enc.decode(toks[start:end]).strip()
            if chunk:
                chunks.append(chunk)
            if end >= len(toks): break
            start = max(0, end - overlap_tokens)
        return chunks
    else:
        chunks: List[str] = []
        start = 0
        n = len(text)
        while start < n:
            end = min(n, start + chunk_chars)
            chunk = text[start:end].strip()
            if chunk:
                chunks.append(chunk)
            if end >= n: break
            start = max(0, end - overlap_chars)
        return chunks

def sha1(s: str) -> str:
    return hashlib.sha1(s.encode("utf-8")).hexdigest()

# -------------------- Embeddings --------------------
_openai = OpenAI(api_key=OPENAI_API_KEY)

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=8),
       retry=retry_if_exception_type(Exception))
def embed_batch(texts: List[str]) -> List[List[float]]:
    log.debug(f"Calling OpenAI embeddings for batch size={len(texts)}")
    resp = _openai.embeddings.create(model=EMBED_MODEL, input=texts)
    return [d.embedding for d in resp.data]

# -------------------- Pinecone --------------------
pc = Pinecone(api_key=PINECONE_API_KEY)

def ensure_index(name: str):
    # Match dims to model
    dims = {
        "text-embedding-3-small": 1536,
        "text-embedding-3-large": 3072
    }
    dim = dims.get(EMBED_MODEL, 1536)

    existing = [idx["name"] for idx in pc.list_indexes()]
    if name not in existing:
        log.info(f"Creating Pinecone index '{name}' (dim={dim}, metric=cosine)…")
        pc.create_index(
            name=name,
            dimension=dim,
            metric="cosine",
            spec=ServerlessSpec(cloud=PINECONE_CLOUD, region=PINECONE_REGION),
        )
        while True:
            desc = pc.describe_index(name)
            if desc.status.get("ready"):
                break
            time.sleep(2)
        log.info("Index is ready.")

def upsert_vectors(index_name: str, vectors: List[Dict], namespace: str = ""):
    index = pc.Index(index_name)
    for i in range(0, len(vectors), 100):
        batch = vectors[i:i+100]
        log.debug(f"Upserting {len(batch)} vectors…")
        index.upsert(vectors=batch, namespace=namespace or None)

def delete_by_urls(index_name: str, urls: List[str], namespace: str = ""):
    """Delete all vectors whose metadata.url is in urls."""
    if not urls:
        return
    index = pc.Index(index_name)
    for i in range(0, len(urls), 100):
        subset = urls[i:i+100]
        log.info(f"Deleting {len(subset)} url(s) from index…")
        index.delete(filter={"url": {"$in": subset}}, namespace=namespace or None)

def extract_title(html: str) -> str:
    try:
        soup = BeautifulSoup(html, "lxml")
        if soup.title and soup.title.text:
            return soup.title.text.strip()[:512]
    except Exception:
        pass
    return ""

def parse_lastmod_timestamp(value: Optional[str]) -> Optional[datetime]:
    if not value:
        return None
    text = value.strip()
    if not text:
        return None
    cleaned = text
    if cleaned.endswith("Z"):
        cleaned = cleaned[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(cleaned)
    except ValueError:
        # Try to normalise space-separated format
        try:
            dt = datetime.fromisoformat(cleaned.replace(" ", "T"))
        except ValueError:
            log.debug(f"Could not parse lastmod value '{text}'")
            return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    else:
        dt = dt.astimezone(timezone.utc)
    return dt


def dedupe_entries(entries: List[SitemapEntry]) -> List[SitemapEntry]:
    deduped: Dict[str, SitemapEntry] = {}
    for entry in entries:
        url = entry["url"]
        lastmod = entry.get("lastmod")
        existing = deduped.get(url)
        if not existing:
            deduped[url] = entry
            continue
        new_dt = parse_lastmod_timestamp(lastmod)
        existing_dt = parse_lastmod_timestamp(existing.get("lastmod"))
        if new_dt and existing_dt:
            if new_dt > existing_dt:
                deduped[url] = entry
        elif lastmod and not existing.get("lastmod"):
            deduped[url] = entry
    return sorted(deduped.values(), key=lambda e: e["url"])


def parse_sitemap_content(content: str) -> List[SitemapEntry]:
    soup = BeautifulSoup(content, "xml")
    entries: List[SitemapEntry] = []
    for node in soup.find_all("url"):
        loc_tag = node.find("loc")
        if not loc_tag or not loc_tag.text:
            continue
        loc_text = loc_tag.text.strip()
        if not loc_text:
            continue
        lastmod_tag = node.find("lastmod")
        lastmod_text = None
        if lastmod_tag and lastmod_tag.text:
            lastmod_text = lastmod_tag.text.strip() or None
        entries.append({"url": loc_text, "lastmod": lastmod_text})
    return dedupe_entries(entries)


def load_previous_sitemap(path: Optional[str]) -> List[SitemapEntry]:
    if not path or not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as exc:
        log.warning(f"Failed to read previous sitemap from {path}: {exc}")
        return []
    return parse_sitemap_content(content)


def save_sitemap_copy(path: Optional[str], entries: List[SitemapEntry]):
    if not path:
        return
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    sorted_entries = sorted(entries, key=lambda e: e["url"])
    urlset = ET.Element("urlset")
    urlset.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")
    for entry in sorted_entries:
        url_elem = ET.SubElement(urlset, "url")
        loc_elem = ET.SubElement(url_elem, "loc")
        loc_elem.text = entry["url"]
        if entry.get("lastmod"):
            lastmod_elem = ET.SubElement(url_elem, "lastmod")
            lastmod_elem.text = entry["lastmod"]
    tree = ET.ElementTree(urlset)
    tmp = path + ".tmp"
    tree.write(tmp, encoding="utf-8", xml_declaration=True)
    os.replace(tmp, path)


def read_last_run_time(path: Optional[str]) -> Optional[datetime]:
    if not path or not os.path.exists(path):
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read().strip()
    except Exception as exc:
        log.warning(f"Failed to read last run timestamp from {path}: {exc}")
        return None
    if not text:
        return None
    try:
        dt = datetime.fromisoformat(text)
    except ValueError:
        dt = parse_lastmod_timestamp(text)
        if not dt:
            log.warning(f"Could not parse last run timestamp '{text}' from {path}")
            return None
        return dt
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    else:
        dt = dt.astimezone(timezone.utc)
    return dt


def write_last_run_time(path: Optional[str], run_time: datetime):
    if not path:
        return
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(run_time.isoformat())
    os.replace(tmp, path)


def apply_excludes(entries: List[SitemapEntry], patterns: List[str]) -> (List[SitemapEntry], List[SitemapEntry]):
    if not patterns:
        return entries, []
    regs = [re.compile(p) for p in patterns]
    kept: List[SitemapEntry] = []
    dropped: List[SitemapEntry] = []
    for entry in entries:
        url = entry["url"]
        if any(r.search(url) for r in regs):
            dropped.append(entry)
        else:
            kept.append(entry)
    if dropped:
        log.info(f"Excluded by pattern: {len(dropped)} URL(s)")
    return kept, dropped

# -------------------- Main --------------------
def main(sitemap_url: str,
         allow_domains: Optional[List[str]] = None,
         css_selector: Optional[str] = None,
         dry_run: bool = False,
         limit: Optional[int] = None,
         batch_size: int = 32,
         sleep_s: float = 0.0,
         use_tiktoken: bool = True,
         min_chars: int = 200,
         exclude_patterns: Optional[List[str]] = None,
         namespace: str = "",
         store_text: bool = False,
         preview_chars: int = 3000,
         state_dir: Optional[str] = None):
    log.info(f"Parsing sitemap: {sitemap_url}")
    run_started_at = datetime.now(timezone.utc)

    raw_entries = parse_sitemap(sitemap_url)
    all_entries = dedupe_entries(raw_entries)
    log.info(f"Found {len(all_entries)} URLs in sitemap")

    # Domain filter
    if allow_domains:
        allow_set = set(allow_domains)
        all_entries = [
            entry for entry in all_entries
            if any(urlparse(entry["url"]).netloc.endswith(d) for d in allow_set)
        ]
        log.info(f"After domain filter: {len(all_entries)} URLs")

    last_run_time_path: Optional[str] = None
    last_sitemap_path: Optional[str] = None
    previous_entries: List[SitemapEntry] = []
    last_run_time: Optional[datetime] = None

    if state_dir:
        last_run_time_path = os.path.join(state_dir, "last_run_time.txt")
        last_sitemap_path = os.path.join(state_dir, "last_sitemap.xml")
        previous_entries = load_previous_sitemap(last_sitemap_path)
        last_run_time = read_last_run_time(last_run_time_path)
        if not previous_entries and not last_run_time:
            log.info("State files not found; performing full reindex.")
        else:
            if not previous_entries:
                log.info("Previous sitemap not found; deletions will not be detected this run.")
            if not last_run_time:
                log.info("Last run timestamp missing; reindexing all eligible URLs.")

    # Exclude patterns -> split into kept/excluded
    kept_entries, excluded_entries = apply_excludes(all_entries, exclude_patterns or [])
    log.info(f"{len(kept_entries)} URL(s) remain after excludes")

    # Detect removals before applying lastmod filter or limit
    vanished_urls: List[str] = []
    if previous_entries:
        prev_urls = {entry["url"] for entry in previous_entries}
        current_urls = {entry["url"] for entry in all_entries}
        vanished_urls = sorted(prev_urls - current_urls)
        if vanished_urls:
            log.info(f"Detected {len(vanished_urls)} URL(s) removed since last run")

    # Filter by lastmod > last_run_time
    entries_to_process = kept_entries
    if last_run_time:
        filtered: List[SitemapEntry] = []
        for entry in kept_entries:
            lastmod_dt = parse_lastmod_timestamp(entry.get("lastmod"))
            if lastmod_dt is None or lastmod_dt > last_run_time:
                filtered.append(entry)
        log.info(
            f"{len(filtered)} URL(s) to index after lastmod filter (last run at {last_run_time.isoformat()})"
        )
        entries_to_process = filtered
    else:
        log.info("No last run timestamp; indexing all remaining URLs.")

    # Apply limit after lastmod filter
    if limit is not None:
        entries_to_process = entries_to_process[:limit]
        log.info(f"Limiting to first {len(entries_to_process)} URL(s) after filters (limit={limit})")

    if dry_run:
        for entry in entries_to_process:
            log.info(f"DRY-RUN reindex: {entry['url']} (lastmod={entry.get('lastmod') or 'n/a'})")
        for entry in excluded_entries:
            log.info(f"DRY-RUN EXCLUDE (will delete): {entry['url']}")
        if vanished_urls:
            log.info(f"DRY-RUN would delete {len(vanished_urls)} URL(s) vanished from sitemap.")
        log.info("Dry run only. Exiting.")
        return

    ensure_index(PINECONE_INDEX)

    # Delete URLs that vanished from the sitemap since last run
    if vanished_urls:
        log.info(f"Deleting {len(vanished_urls)} URL(s) vanished from sitemap since last run…")
        delete_by_urls(PINECONE_INDEX, vanished_urls, namespace=namespace)

    # Delete URLs matching current exclude patterns
    if excluded_entries:
        excluded_urls = [entry["url"] for entry in excluded_entries]
        log.info(f"Deleting {len(excluded_urls)} URL(s) due to exclude patterns…")
        delete_by_urls(PINECONE_INDEX, excluded_urls, namespace=namespace)

    if not entries_to_process:
        log.info("No URLs require indexing after lastmod filter. Updating state only.")
    total = len(entries_to_process)
    for idx, entry in enumerate(entries_to_process, 1):
        url = entry["url"]
        try:
            log.info(f"[{idx}/{total}] Fetch: {url}")
            try:
                r = http_get(url, timeout=25)
            except NotFound:
                log.warning(f"Not found: {url} -> deleting from index")
                delete_by_urls(PINECONE_INDEX, [url], namespace=namespace)
                continue

            log.debug("Extracting main text…")
            text = clean_text(r.text, base_url=url, css_selector=css_selector)
            if not text:
                log.warning("Skip: no text extracted")
                continue

            if len(text) > MAX_EXTRACT_CHARS:
                log.info(f"Truncating extracted text from {len(text)} to {MAX_EXTRACT_CHARS} chars")
                text = text[:MAX_EXTRACT_CHARS]

            n_chars = len(text)
            log.info(f"Extracted {n_chars} chars")
            if n_chars < min_chars:
                log.warning(f"Skip: too little text (len={n_chars} < {min_chars})")
                continue

            chunks = chunk_text(
                text,
                use_tiktoken=use_tiktoken,
                chunk_tokens=800, overlap_tokens=80,
                chunk_chars=4000, overlap_chars=400
            )
            log.info(f"Chunked into {len(chunks)} parts")

            embeds: List[List[float]] = []
            for i in range(0, len(chunks), batch_size):
                batch = chunks[i:i+batch_size]
                log.debug(f"Embedding batch {i//batch_size+1} size={len(batch)}")
                embeds.extend(embed_batch(batch))

            title = extract_title(r.text)
            vecs = []
            for chunk_idx, (chunk, emb) in enumerate(zip(chunks, embeds)):
                vid = sha1(f"{url}:::{chunk_idx}")
                meta = {
                    "url": url,
                    "title": title,
                    "chunk": chunk_idx,
                    "n_chunks": len(chunks)
                }
                if store_text:
                    meta["text"] = chunk[:preview_chars]
                vecs.append({"id": vid, "values": emb, "metadata": meta})

            log.info(f"Upserting {len(vecs)} vectors…")
            upsert_vectors(PINECONE_INDEX, vecs, namespace=namespace)

            if sleep_s > 0:
                time.sleep(sleep_s)

        except Exception as e:
            log.error(f"Error on {url}: {e}")
            log.debug(traceback.format_exc())
            continue

    if state_dir:
        os.makedirs(state_dir, exist_ok=True)
        save_sitemap_copy(last_sitemap_path, all_entries)
        write_last_run_time(last_run_time_path, run_started_at)
        log.info("Persisted sitemap snapshot and last run timestamp.")

    log.info("Done.")

# -------------------- CLI --------------------
if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description="Scrape sitemap URLs into Pinecone with incremental updates based on lastmod")
    ap.add_argument("sitemap", help="URL to sitemap.xml (or sitemap index)")
    ap.add_argument("--allow-domain", action="append", default=[], help="Limit to domain(s), e.g. --allow-domain example.com")
    ap.add_argument("--css", default=".theme-doc-markdown.markdown", help="CSS selector for content container")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, help="Limit number of pages processed")
    ap.add_argument("--batch-size", type=int, default=32, help="Embedding batch size (lower if OOM)")
    ap.add_argument("--sleep", type=float, default=0.0, help="Sleep seconds between pages")
    ap.add_argument("--no-tiktoken", action="store_true", help="Use char-based chunking (lower RAM)")
    ap.add_argument("--min-chars", type=int, default=20, help="Minimum characters required to index a page")
    ap.add_argument("--exclude", action="append", default=[], help="Regex to exclude URLs (can be repeated)")
    ap.add_argument("--state-dir", help="Directory to persist last run timestamp and sitemap snapshot")
    ap.add_argument("--namespace", default=os.environ.get("PINECONE_NAMESPACE", ""), help="Pinecone namespace (optional)")
    ap.add_argument("--store-text", action="store_true", help="Store chunk text in Pinecone metadata for reranking")
    ap.add_argument("--preview-chars", type=int, default=3000, help="Max chars of chunk text to store in metadata")
    ap.add_argument("--verbose", action="store_true", help="Verbose logging")
    ap.add_argument("--log-file", help="Write logs to this file")
    args = ap.parse_args()

    setup_logging(args.verbose, args.log_file)
    allow = args.allow_domain if args.allow_domain else None
    try:
        main(
            sitemap_url=args.sitemap,
            allow_domains=allow,
            css_selector=args.css,
            dry_run=args.dry_run,
            limit=args.limit,
            batch_size=args.batch_size,
            sleep_s=args.sleep,
            use_tiktoken=not args.no_tiktoken,
            min_chars=args.min_chars,
            exclude_patterns=args.exclude,
            namespace=args.namespace,
            store_text=args.store_text,
            preview_chars=args.preview_chars,
            state_dir=args.state_dir,
        )
    except KeyboardInterrupt:
        log.warning("Interrupted by user")
