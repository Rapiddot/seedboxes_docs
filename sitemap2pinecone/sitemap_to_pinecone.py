#!/usr/bin/env python3
import os
import re
import json
import time
import hashlib
import logging
import traceback
import sys
from typing import List, Dict, Optional, Set
from urllib.parse import urlparse

# Keep native libs from over-parallelizing on small VMs
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

import requests
from bs4 import BeautifulSoup
import trafilatura
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from tqdm import tqdm
from dotenv import load_dotenv

# OpenAI v1 SDK
from openai import OpenAI

# Pinecone v5 SDK
from pinecone import Pinecone, ServerlessSpec

load_dotenv()

# -------------------- Config via env --------------------
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY", "")
PINECONE_INDEX   = os.environ.get("PINECONE_INDEX", "sbcc-docs")
PINECONE_CLOUD   = os.environ.get("PINECONE_CLOUD", "aws")
PINECONE_REGION  = os.environ.get("PINECONE_REGION", "us-east-1")
OPENAI_API_KEY   = os.environ.get("OPENAI_API_KEY", "")
EMBED_MODEL      = os.environ.get("EMBED_MODEL", "text-embedding-3-large")
PINECONE_NAMESPACE = os.environ.get("PINECONE_NAMESPACE", "")  # optional
MAX_EXTRACT_CHARS = int(os.environ.get("MAX_EXTRACT_CHARS", "400000"))      # per-page cap

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

# -------------------- Sitemap --------------------
def parse_sitemap(url: str) -> List[str]:
    """Recursively parse sitemap and return list of page URLs."""
    r = http_get(url)
    soup = BeautifulSoup(r.content, "xml")
    urls: List[str] = []

    # <sitemapindex> case
    sitemapindex = soup.find("sitemapindex")
    if sitemapindex:
        for sm_loc in sitemapindex.find_all("loc"):
            child = sm_loc.text.strip()
            urls.extend(parse_sitemap(child))
        return urls

    # <urlset> case
    urlset = soup.find("urlset")
    if not urlset:
        url_elems = soup.find_all("url")
        if url_elems:
            return [u.loc.text.strip() for u in url_elems if u.loc and u.loc.text]
        return []

    for u in urlset.find_all("url"):
        loc = u.find("loc")
        if loc and loc.text:
            urls.append(loc.text.strip())

    return urls

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

# -------------------- Helpers --------------------
def load_inventory(path: str) -> Set[str]:
    if not path or not os.path.exists(path):
        return set()
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return set(data.get("urls", []))
    except Exception:
        return set()

def save_inventory(path: str, urls: Set[str]):
    if not path:
        return
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump({"urls": sorted(urls)}, f, ensure_ascii=False, indent=2)
    os.replace(tmp, path)

def apply_excludes(urls: List[str], patterns: List[str]) -> (List[str], List[str]):
    if not patterns:
        return urls, []
    regs = [re.compile(p) for p in patterns]
    kept, dropped = [], []
    for u in urls:
        if any(r.search(u) for r in regs):
            dropped.append(u)
        else:
            kept.append(u)
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
         inventory_file: Optional[str] = None,
         namespace: str = "",
         store_text: bool = False,
         preview_chars: int = 3000):
    log.info(f"Parsing sitemap: {sitemap_url}")

    # Parse full sitemap first (to know what was excluded)
    all_urls = sorted(set(parse_sitemap(sitemap_url)))
    log.info(f"Found {len(all_urls)} URLs in sitemap")

    # Domain filter
    if allow_domains:
        allow_set = set(allow_domains)
        all_urls = [u for u in all_urls if any(urlparse(u).netloc.endswith(d) for d in allow_set)]
        log.info(f"After domain filter: {len(all_urls)} URLs")

    # Exclude patterns -> split into kept/excluded
    urls, excluded_now = apply_excludes(all_urls, exclude_patterns or [])

    # Limit after excludes
    if limit is not None:
        urls = urls[:limit]
        log.info(f"Limiting to first {limit} URLs")

    # Inventory load (for sitemap diff tombstones)
    prev_urls = load_inventory(inventory_file) if inventory_file else set()

    if dry_run:
        for u in urls:
            log.info(f"DRY-RUN keep: {u}")
        for u in excluded_now:
            log.info(f"DRY-RUN EXCLUDE (will delete): {u}")
        if inventory_file:
            vanished = sorted(prev_urls - set(all_urls))
            if vanished:
                log.info(f"DRY-RUN would delete {len(vanished)} URL(s) vanished from sitemap.")
        log.info("Dry run only. Exiting.")
        return

    ensure_index(PINECONE_INDEX)

    # 1) Delete URLs that vanished from the sitemap since last run
    if inventory_file and prev_urls:
        vanished = sorted(prev_urls - set(all_urls))
        if vanished:
            log.info(f"Deleting {len(vanished)} URL(s) vanished from sitemap since last run…")
            delete_by_urls(PINECONE_INDEX, vanished, namespace=namespace)

    # 2) Delete URLs matching current exclude patterns
    if excluded_now:
        log.info(f"Deleting {len(excluded_now)} URL(s) due to exclude patterns…")
        delete_by_urls(PINECONE_INDEX, list(excluded_now), namespace=namespace)

    # 3) Ingest kept URLs
    for uix, url in enumerate(urls, 1):
        try:
            log.info(f"[{uix}/{len(urls)}] Fetch: {url}")
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

            # Embed in batches
            embeds: List[List[float]] = []
            for i in range(0, len(chunks), batch_size):
                batch = chunks[i:i+batch_size]
                log.debug(f"Embedding batch {i//batch_size+1} size={len(batch)}")
                embeds.extend(embed_batch(batch))

            title = extract_title(r.text)
            vecs = []
            # include chunk text in metadata when requested
            for idx, (chunk, emb) in enumerate(zip(chunks, embeds)):
                vid = sha1(f"{url}:::{idx}")
                meta = {
                    "url": url,
                    "title": title,
                    "chunk": idx,
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

    # Save the full sitemap URL set as inventory baseline
    if inventory_file:
        save_inventory(inventory_file, set(all_urls))

    log.info("Done.")

# -------------------- CLI --------------------
if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description="Scrape sitemap URLs into Pinecone (with excludes, tombstoning, and stored text)")
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
    ap.add_argument("--inventory-file", help="Path to JSON storing last-run sitemap URLs (for diff-based deletions)")
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
            inventory_file=args.inventory_file,
            namespace=args.namespace,
            store_text=args.store_text,
            preview_chars=args.preview_chars,
        )
    except KeyboardInterrupt:
        log.warning("Interrupted by user")