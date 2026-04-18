# Post-Deploy Check — V18

Date: 2026-04-18
Implementation commit: `91c400aa83176f2dac2874c6471dbb8133d389b9`
Resolved entry slug: `we-are-building-a-partner`
Primary domain: `https://ivankotov.eu/`

## Initial status check immediately after push

- `/` -> `200`
- `/diary/` -> `200`
- `/diary/archive/` -> `200`
- `/diary/tags/` -> `200`
- `/diary/we-are-building-a-partner/` -> `404`
- `/diary/proof-of-reality/` -> `200`
- `/diary/agi-public-release-v1-1/` -> `200`
- `/diary/tags/agi/` -> `200`
- `/diary/tags/human-centric-ai/` -> `404`
- `/diary/tags/digital-sovereignty/` -> `404`
- `/diary/tags/philosophy/` -> `404`
- `/diary/tags/innovation/` -> `404`
- `diary-index.json` -> `200`
- `diary-tags.json` -> `200`
- `diary-feed.xml` -> `200`
- `sitemap.xml` -> `200`
- `assets/diary/we-are-building-a-partner/cover.jpg` -> `404`

## Follow-up status check after propagation delay

- `/` -> `200`
- `/diary/` -> `200`
- `/diary/archive/` -> `200`
- `/diary/tags/` -> `200`
- `/diary/we-are-building-a-partner/` -> `200`
- `/diary/proof-of-reality/` -> `200`
- `/diary/agi-public-release-v1-1/` -> `200`
- `/diary/tags/agi/` -> `200`
- `/diary/tags/human-centric-ai/` -> `200`
- `/diary/tags/digital-sovereignty/` -> `200`
- `/diary/tags/philosophy/` -> `200`
- `/diary/tags/innovation/` -> `200`
- `diary-index.json` -> `200`
- `diary-tags.json` -> `200`
- `diary-feed.xml` -> `200`
- `sitemap.xml` -> `200`
- `assets/diary/we-are-building-a-partner/cover.jpg` -> `200`

## Validation assertions

- home latest-post title is `We are building a Partner`: pass
- home latest-post link points to `/diary/we-are-building-a-partner/`: pass
- home latest-post image points to `/assets/diary/we-are-building-a-partner/cover.jpg`: pass
- home latest-post image alt matches the factual resolved alt text: pass
- `/diary/` shows the new post: pass
- `/diary/` still shows `proof-of-reality`: pass
- `/diary/archive/` shows the new post: pass
- `/diary/tags/` shows `Human Centric AI`: pass
- `/diary/tags/` shows `Digital Sovereignty`: pass
- `/diary/tags/` shows `Philosophy`: pass
- `/diary/tags/` shows `Innovation`: pass
- `/diary/tags/agi/` shows the new post: pass
- `/diary/tags/human-centric-ai/` shows the new post: pass
- `/diary/tags/digital-sovereignty/` shows the new post: pass
- `/diary/tags/philosophy/` shows the new post: pass
- `/diary/tags/innovation/` shows the new post: pass
- new post page has `BlogPosting` schema: pass
- new post page has `mainEntityOfPage`: pass
- new post page has `keywords`: pass
- new post page has `image` schema field: pass
- new post page has `og:image`: pass
- new post page renders the supplied cover image: pass
- new post page renders the factual image alt: pass
- previous imported post `proof-of-reality` still renders: pass
- previous imported post `agi-public-release-v1-1` still renders: pass
- `diary-index.json` count is `3`: pass
- `diary-index.json` latest slug is `we-are-building-a-partner`: pass
- `diary-tags.json` keeps `AGI` count at `3`: pass
- `diary-tags.json` includes `human-centric-ai`: pass
- `diary-tags.json` includes `digital-sovereignty`: pass
- `diary-tags.json` includes `philosophy`: pass
- `diary-tags.json` includes `innovation`: pass
- `diary-feed.xml` contains `3` items: pass
- `diary-feed.xml` includes `we-are-building-a-partner`: pass
- `sitemap.xml` includes `/diary/we-are-building-a-partner/`: pass
- `sitemap.xml` includes `/diary/tags/human-centric-ai/`: pass
- `sitemap.xml` includes `/diary/tags/digital-sovereignty/`: pass
- `sitemap.xml` includes `/diary/tags/philosophy/`: pass
- `sitemap.xml` includes `/diary/tags/innovation/`: pass
- live image asset returns `image/jpeg`: pass

## No fake image confirmation

- the imported entry uses only the supplied source image: pass
- no replacement or placeholder image was introduced on the post page: pass
- no replacement or placeholder image was introduced in the home latest-post slot: pass

## Pages build trace

- public deploy showed a short propagation delay on first check
- follow-up live URL checks confirmed the new pages and image asset after propagation
