# Post-Deploy Check — V17

Date: 2026-04-18
Implementation commit: `1ea5cab9c9c8c4135f3fb04b1e890a954376c36c`
Resolved entry slug: `proof-of-reality`
Primary domain: `https://ivankotov.eu/`

## Initial status check immediately after push

- `/` -> `200`
- `/diary/` -> `200`
- `/diary/archive/` -> `200`
- `/diary/tags/` -> `200`
- `/diary/proof-of-reality/` -> `404`
- `/diary/agi-public-release-v1-1/` -> `200`
- `/diary/tags/agi/` -> `200`
- `/diary/tags/future-tech/` -> `404`
- `/diary/tags/data-mining/` -> `404`
- `/diary/tags/ai-architecture/` -> `404`
- `/diary/tags/economy/` -> `404`
- `diary-index.json` -> `200`
- `diary-tags.json` -> `200`
- `diary-feed.xml` -> `200`
- `sitemap.xml` -> `200`
- `styles.css` -> `200`

## Follow-up status check after propagation delay

- `/` -> `200`
- `/diary/` -> `200`
- `/diary/archive/` -> `200`
- `/diary/tags/` -> `200`
- `/diary/proof-of-reality/` -> `200`
- `/diary/agi-public-release-v1-1/` -> `200`
- `/diary/tags/agi/` -> `200`
- `/diary/tags/future-tech/` -> `200`
- `/diary/tags/data-mining/` -> `200`
- `/diary/tags/ai-architecture/` -> `200`
- `/diary/tags/economy/` -> `200`
- `diary-index.json` -> `200`
- `diary-tags.json` -> `200`
- `diary-feed.xml` -> `200`
- `sitemap.xml` -> `200`
- `styles.css` -> `200`

## Validation assertions

- home latest-post slot title is `Proof of Reality`: pass
- home latest-post slot link points to `/diary/proof-of-reality/`: pass
- home latest-post slot has no image tag: pass
- `/diary/` shows the new post: pass
- `/diary/` still shows the previous imported post: pass
- `/diary/archive/` shows the new post: pass
- `/diary/tags/` shows `Future Tech`: pass
- `/diary/tags/` shows `Data Mining`: pass
- `/diary/tags/` shows `AI Architecture`: pass
- `/diary/tags/` shows `Economy`: pass
- `/diary/tags/agi/` shows the new post: pass
- `/diary/tags/future-tech/` shows the new post: pass
- `/diary/tags/data-mining/` shows the new post: pass
- `/diary/tags/ai-architecture/` shows the new post: pass
- `/diary/tags/economy/` shows the new post: pass
- new post page has `BlogPosting` schema: pass
- new post page has `mainEntityOfPage`: pass
- new post page has `keywords`: pass
- new post page has no `og:image`: pass
- new post page has no `<img>` tag: pass
- previous imported post page still renders: pass
- `diary-index.json` count is `2`: pass
- `diary-index.json` latest slug is `proof-of-reality`: pass
- `diary-tags.json` keeps `AGI` count at `2`: pass
- `diary-tags.json` includes `future-tech`: pass
- `diary-feed.xml` contains `2` items: pass
- `diary-feed.xml` includes `proof-of-reality`: pass
- `sitemap.xml` includes `/diary/proof-of-reality/`: pass
- `sitemap.xml` includes `/diary/tags/future-tech/`: pass
- live `styles.css` keeps `@media (max-width: 820px)`: pass
- live `styles.css` keeps `.archive-grid`: pass

## No fake image confirmation

- no primary image was introduced into the source entry: pass
- no post-page image element was rendered: pass
- no home latest-slot image element was rendered: pass

## Pages build trace

- GitHub commit workflow runs exposed for `1ea5cab9c9c8c4135f3fb04b1e890a954376c36c`: none
- Combined commit statuses exposed for `1ea5cab9c9c8c4135f3fb04b1e890a954376c36c`: none
- public deploy confirmed by live URL checks after a short propagation delay
