# POST_DEPLOY_CHECK

Batch: `SITE_DIARY_IMPORT_BATCH_0089_0093_V37`  
Implementation commit: `f1f53f2777d1493f3ce3afb112e297778a740223`

## Deployment readiness

- Poll target: `https://ivankotov.eu/diary-latest.json`
- Expected latest slug: `i-also-published-a-graph-visibility-layer-for-the-l4-glitch-stack`
- Result:
  - attempt 1: `200`, old content still served
  - attempt 2: `200`, old content still served
  - attempt 3: `200`, old content still served
  - attempt 4: `200`, new content served

## Live status

- Live validation result: pass
- Remote checks completed: `75`
- All checked URLs returned `200`

## Core live surfaces

- `https://ivankotov.eu/`
- `https://ivankotov.eu/diary/`
- `https://ivankotov.eu/diary/archive/`
- `https://ivankotov.eu/diary/tags/`
- `https://ivankotov.eu/diary-index.json`
- `https://ivankotov.eu/diary-latest.json`
- `https://ivankotov.eu/diary-tags.json`
- `https://ivankotov.eu/diary-feed.xml`
- `https://ivankotov.eu/sitemap.xml`

## New live entry URLs

- `https://ivankotov.eu/diary/one-of-the-most-persistent-mistakes-in-ai-discourse-is-the-fantasy-of-digital-immortality/`
- `https://ivankotov.eu/diary/a-new-public-layer-is-now-part-of-the-corpus/`
- `https://ivankotov.eu/diary/one-of-the-most-dangerous-habits-in-current-ai-systems-is-this/`
- `https://ivankotov.eu/diary/there-is-already-enough-public-structure-to-say-this-calmly/`
- `https://ivankotov.eu/diary/i-also-published-a-graph-visibility-layer-for-the-l4-glitch-stack/`

## New live image assets

- `https://ivankotov.eu/assets/diary/one-of-the-most-persistent-mistakes-in-ai-discourse-is-the-fantasy-of-digital-immortality/cover.jpg`
- `https://ivankotov.eu/assets/diary/a-new-public-layer-is-now-part-of-the-corpus/cover.jpg`
- `https://ivankotov.eu/assets/diary/one-of-the-most-dangerous-habits-in-current-ai-systems-is-this/cover.jpg`
- `https://ivankotov.eu/assets/diary/there-is-already-enough-public-structure-to-say-this-calmly/cover.jpg`
- `https://ivankotov.eu/assets/diary/i-also-published-a-graph-visibility-layer-for-the-l4-glitch-stack/cover.jpg`

## Assertions confirmed live

- Latest-post on home switched to `i-also-published-a-graph-visibility-layer-for-the-l4-glitch-stack`.
- `diary-index.json` newest-five order is:
  - `i-also-published-a-graph-visibility-layer-for-the-l4-glitch-stack`
  - `there-is-already-enough-public-structure-to-say-this-calmly`
  - `one-of-the-most-dangerous-habits-in-current-ai-systems-is-this`
  - `a-new-public-layer-is-now-part-of-the-corpus`
  - `we-are-still-looking-at-what-is-happening-from-the-wrong-angle`
- Same-date order for `2026-04-07` is correct: `0092` above `0091`.
- `POST 0089` preserved its notation and structure without introducing a non-existent body DOI or external link.
- `POST 0090` preserved `Input -> Experience -> Training -> Evidence`.
- `POST 0091` Zenodo URL renders as a clickable anchor with the visible URL as label.
- `POST 0092` preserved bold and backticked notation and its public code URL renders as a clickable anchor.
- `POST 0093` preserved the bullet list and its Zenodo URL renders as a clickable anchor.
- V23 baseline remained intact: home latest-post meta line and diary card meta lines are date-only.
- V28 baseline remained intact: `/diary/` still exposes the full newest-five preview window.
- `sitemap.xml` includes all five V37 entry URLs and the new V37 tag URLs.

## New tag pages introduced in V37

- `https://ivankotov.eu/diary/tags/embodied-intelligence/`
- `https://ivankotov.eu/diary/tags/ethics-of-ai/`
- `https://ivankotov.eu/diary/tags/multi-agent-systems/`
- `https://ivankotov.eu/diary/tags/knowledge-systems/`
- `https://ivankotov.eu/diary/tags/clean-architecture/`
- `https://ivankotov.eu/diary/tags/long-lived-systems/`
- `https://ivankotov.eu/diary/tags/persistent-ai/`

All of the above returned `200` and contained the expected V37 post membership.
