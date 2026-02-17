---
title: Why does my plan have less disk space than what's shown on the website?
id: plan-disk-space-difference
description: Understanding the differences between unlimited traffic plans and current plans, and what to consider before migrating.
keywords:
    - legacy plan
    - disk space
    - unlimited traffic
    - plan migration
    - plan upgrade
    - traffic quota
---

# Why does my plan have less disk space than what's shown on the website?

If you're on one of our legacy plans (Unlimited plans) and noticed that the website lists the same plan name with **double the disk space**, you might be wondering why your plan hasn't been updated. This is a great question, and we want to make sure you understand the full picture.

## The Key Difference: Unlimited Traffic

The most important difference that's easy to miss is this: **your legacy plan includes unlimited upload traffic, while the new plans have monthly traffic quotas.**

This is a significant advantage that many of our legacy plan users value highly, which is why we've kept those plans active for existing customers. Unlimited plans are not available anymore for new orders, but we do honour them for existing clients as long as they remain active.

## Detailed Comparison: Legacy vs. Current Plans

Here's what you need to know about the differences:

| Feature | Your Legacy Plan | Current Plans |
|---------|------------------|---------------|
| **Upload Traffic** | ✅ **Unlimited** - No restrictions, ever | ❌ Monthly quota (10TB - 40TB depending on plan) |
| **Disk Space** | Half of current plans | Double of legacy plans |
| **After Traffic Limit** | N/A - No limit to hit | Upload speed limited to 10 Mbit/s for remainder of month |
| **Download Speed** | Unlimited | Unlimited (even after quota) |
| **Pricing** | Same as current plans | Same as legacy plans |
| **All Other Features** | Identical | Identical |

### What Counts as Traffic?

This is important to understand: **all traffic leaving your seedbox counts toward the monthly quota** on current plans. This includes:

- 📤 Torrent uploads (seeding)
- 📥 FTP/SFTP downloads to your home
- 🎬 **Streaming from Plex, Emby, or Jellyfin**
- 🌐 Any other data leaving your seedbox through installed applications

So if you frequently stream content to multiple devices or seed heavily, you could hit the traffic limit more quickly than you might expect.

### What Happens When Traffic is Depleted?

Once you reach your monthly traffic quota on the new plans:

- ⚠️ **All upload speeds are limited to 10 Mbit/s** (not just torrents)
- This affects seeding, FTP uploads, streaming, and all other outbound traffic
- The limit remains until the start of your next billing cycle
- Download speeds remain unlimited

## Should You Migrate to a Current Plan?

We're happy to migrate you to a current plan if you prefer, but please consider these important points first:

**Remember: This is a one-way decision. You cannot return to an unlimited plan once you leave it - these plans are permanently discontinued.**

### ✅ Migration Makes Sense If:

- You rarely exceed the traffic quota for your plan tier
- You need significantly more storage space
- You primarily use your seedbox for storage rather than heavy seeding/streaming
- You've calculated your typical monthly traffic and it's well below the limit

### ❌ Consider Staying on Legacy If:

- You rely on unlimited traffic for heavy seeding
- You stream frequently to multiple users/devices via Plex/Emby/Jellyfin
- You maintain high ratio requirements on private trackers
- You prefer predictable performance without speed throttling concerns

## Migration Requirements and Limitations

If you do decide to migrate to a current plan, please be aware of these requirements:

### 1. Torrent Client Version Compatibility

The following **older torrent client versions are not supported** on current plans and will need to be switched before migration:

- ❌ ruTorrent 3.x (please upgrade to ruTorrent 4.x)
- ❌ Deluge 1.3.x (please upgrade to Deluge 2.x)
- ❌ Transmission 3.x (please upgrade to Transmission 4.x)

You can switch your torrent client from your [client area](https://www.seedboxes.cc/client/dashboard) before requesting migration.

### 2. Application Compatibility

Some older legacy applications that still work on legacy plans are no longer supported and **will not be migrated**:

- These apps will need to be uninstalled before migration
- You'll need to verify which of your installed apps are still supported
- Most popular apps (Plex, Sonarr, Radarr, etc.) are fully supported on current plans

:::warning Important
Before migrating, make sure to:
1. Check which torrent client version you're using
2. Upgrade to a supported version if needed (ruTorrent 4.x, Deluge 2.x, or Transmission 4.x)
3. Review your installed applications and remove any deprecated ones
4. **Estimate your typical monthly traffic** to ensure you won't exceed the new quota
:::

## How to Request a Migration

:::danger This Decision is Permanent
**Once you migrate from your unlimited plan to a current plan, you cannot switch back.** Unlimited traffic plans are no longer available - not even for existing customers who give them up. Make absolutely sure this is what you want before proceeding.
:::

If you've considered all the factors above and still want to migrate to a current plan:

1. **First**, update your torrent client to a supported version from your [client area](https://www.seedboxes.cc/client/dashboard)
2. **Second**, calculate your typical monthly traffic (check your usage history if available)
3. **Third**, open a support ticket explaining that you want to migrate from your legacy plan to the current plan
4. Our support team will assist you with the migration process

:::tip Our Recommendation
**You're one of the lucky few who still has an unlimited traffic plan.** We built these plans for users who need predictable performance without worrying about quotas, and we no longer offer them to anyone. Many of our most satisfied long-term customers remain on legacy plans precisely because unlimited traffic is so valuable. If you don't actually need the extra disk space there is no need to switch right now.
:::

## Still Have Questions?

If you're unsure which plan is right for you or need help calculating your traffic usage, please don't hesitate to [contact our support team](https://www.seedboxes.cc/client/dashboard). We're happy to help you make the best decision for your specific use case!

For a complete overview of all plans and features, see our [Overview of Our Plans](./overview-of-our-plans) guide.
