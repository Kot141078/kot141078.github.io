# POST_DEPLOY_CHECK

Batch: `SITE_DIARY_IMPORT_BATCH_0084_0088_V36`  
Implementation commit: `751850ddd82da6ad3aa3a005a78bd1fad67a9ca7`

## Deployment readiness

- Poll target: `https://ivankotov.eu/diary-latest.json`
- Expected latest slug: `we-are-still-looking-at-what-is-happening-from-the-wrong-angle`
- Result:
  - attempt 1: `200`, old content still served
  - attempt 2: `200`, old content still served
  - attempt 3: `200`, new content served

## Live status

- Live validation result: pass
- Remote checks completed: `66`
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

- `https://ivankotov.eu/diary/ea-l4-eatp-is-now-published-in-a-canonical-form-inside-the-public-stack/`
- `https://ivankotov.eu/diary/one-of-the-oldest-mistakes-in-ai-discourse-is-deciding-too-early-that-tool-is-already-a-sufficient-category/`
- `https://ivankotov.eu/diary/a-serious-system-does-not-improvise-through-failure-it-stops/`
- `https://ivankotov.eu/diary/what-worries-me-more-now-is-not-the-ai-bubble-itself-but-the-fact-that-wars-are-starting-to-shape-the-physical-boundary-conditions-around-it/`
- `https://ivankotov.eu/diary/we-are-still-looking-at-what-is-happening-from-the-wrong-angle/`

## New live image assets

- `https://ivankotov.eu/assets/diary/ea-l4-eatp-is-now-published-in-a-canonical-form-inside-the-public-stack/cover.jpg`
- `https://ivankotov.eu/assets/diary/one-of-the-oldest-mistakes-in-ai-discourse-is-deciding-too-early-that-tool-is-already-a-sufficient-category/cover.jpg`
- `https://ivankotov.eu/assets/diary/a-serious-system-does-not-improvise-through-failure-it-stops/cover.jpg`
- `https://ivankotov.eu/assets/diary/we-are-still-looking-at-what-is-happening-from-the-wrong-angle/cover.jpg`

## Assertions confirmed live

- Latest-post on home switched to `we-are-still-looking-at-what-is-happening-from-the-wrong-angle`.
- `diary-index.json` newest-five order is:
  - `we-are-still-looking-at-what-is-happening-from-the-wrong-angle`
  - `what-worries-me-more-now-is-not-the-ai-bubble-itself-but-the-fact-that-wars-are-starting-to-shape-the-physical-boundary-conditions-around-it`
  - `a-serious-system-does-not-improvise-through-failure-it-stops`
  - `one-of-the-oldest-mistakes-in-ai-discourse-is-deciding-too-early-that-tool-is-already-a-sufficient-category`
  - `ea-l4-eatp-is-now-published-in-a-canonical-form-inside-the-public-stack`
- Same-date order for `2026-04-04` is correct: `0087` above `0086`.
- `POST 0087` remained untagged in machine-readable outputs.
- `POST 0087` remained image-less and did not receive a placeholder or fake image.
- `POST 0086` preserved the GitHub and Zenodo link blocks as usable links.
- `POST 0084` preserved the two-line ending.
- `POST 0085` preserved `c = a + b`.
- `POST 0086` preserved `runtime collision -> typed glitch -> quarantined research`.
- V23 baseline remained intact: home latest-post meta line and diary card meta lines are date-only.
- V28 baseline remained intact: `/diary/` still exposes the full newest-five preview window.
- `sitemap.xml` includes all five V36 entry URLs and the newly created V36 tag URLs.

## Affected live tag pages sampled and verified

- `https://ivankotov.eu/diary/tags/machine-learning/`
- `https://ivankotov.eu/diary/tags/ontology/`
- `https://ivankotov.eu/diary/tags/software-architecture/`
- `https://ivankotov.eu/diary/tags/engineering-discipline/`
- `https://ivankotov.eu/diary/tags/software-engineering/`
- `https://ivankotov.eu/diary/tags/backend-engineering/`
- `https://ivankotov.eu/diary/tags/fault-tolerance/`
- `https://ivankotov.eu/diary/tags/error-handling/`
- `https://ivankotov.eu/diary/tags/resilient-systems/`
- `https://ivankotov.eu/diary/tags/state-machines/`
- `https://ivankotov.eu/diary/tags/data-integrity/`
- `https://ivankotov.eu/diary/tags/tech-leadership/`
- `https://ivankotov.eu/diary/tags/structural-honesty/`
- `https://ivankotov.eu/diary/tags/future-of-tech/`
- `https://ivankotov.eu/diary/tags/infrastructure/`
- `https://ivankotov.eu/diary/tags/data-centers/`
- `https://ivankotov.eu/diary/tags/memory/`
- `https://ivankotov.eu/diary/tags/compute-infrastructure/`
- `https://ivankotov.eu/diary/tags/architectural-safety/`
- `https://ivankotov.eu/diary/tags/infrastructure-thinking/`

All of the above returned `200` and contained the expected V36 post membership.
