# V21 Post-Deploy Check

Contract: `SITE_DIARY_IMPORT_BATCH_0014_0018_V21`
Date: `2026-04-18`
Deployment result: converged on first live check

## Live status

- `https://ivankotov.eu/` -> `200`
- `https://ivankotov.eu/diary/` -> `200`
- `https://ivankotov.eu/diary/archive/` -> `200`
- `https://ivankotov.eu/diary/tags/` -> `200`
- `https://ivankotov.eu/diary/why-visual-perception-matters-only-after-memory-exists/` -> `200`
- `https://ivankotov.eu/diary/how-ai-should-live-with-humans-when-the-world-is-already-in-crisis/` -> `200`
- `https://ivankotov.eu/diary/why-thinking-ai-wont-take-over-the-world/` -> `200`
- `https://ivankotov.eu/diary/reality-bound-ai-l4-public-release-v1-2-0/` -> `200`
- `https://ivankotov.eu/diary/a-home-robot-is-not-a-box-with-a-ribbon/` -> `200`
- `https://ivankotov.eu/diary/tags/ai-architecture/` -> `200`
- `https://ivankotov.eu/diary/tags/ai-safety/` -> `200`
- `https://ivankotov.eu/diary/tags/l4-boundary/` -> `200`
- `https://ivankotov.eu/diary/tags/cybernetics/` -> `200`
- `https://ivankotov.eu/diary/tags/complex-systems/` -> `200`
- `https://ivankotov.eu/diary/tags/agi/` -> `200`
- `https://ivankotov.eu/diary/tags/advanced-global-intelligence/` -> `200`
- `https://ivankotov.eu/diary/tags/deep-tech/` -> `200`
- `https://ivankotov.eu/diary/tags/decentralized-ai/` -> `200`
- `https://ivankotov.eu/diary/tags/affective-systems/` -> `200`
- `https://ivankotov.eu/diary/tags/human-ai/` -> `200`
- `https://ivankotov.eu/diary/tags/protocol-design/` -> `200`
- `https://ivankotov.eu/diary/tags/l4/` -> `200`
- `https://ivankotov.eu/diary/tags/privacy-by-design/` -> `200`
- `https://ivankotov.eu/diary/tags/future-of-living/` -> `200`
- `https://ivankotov.eu/diary-index.json` -> `200`
- `https://ivankotov.eu/diary-tags.json` -> `200`
- `https://ivankotov.eu/diary-feed.xml` -> `200`
- `https://ivankotov.eu/sitemap.xml` -> `200`
- `https://ivankotov.eu/assets/diary/why-visual-perception-matters-only-after-memory-exists/cover.jpg` -> `200`
- `https://ivankotov.eu/assets/diary/how-ai-should-live-with-humans-when-the-world-is-already-in-crisis/cover.jpg` -> `200`
- `https://ivankotov.eu/assets/diary/why-thinking-ai-wont-take-over-the-world/cover.jpg` -> `200`
- `https://ivankotov.eu/assets/diary/a-home-robot-is-not-a-box-with-a-ribbon/cover.jpg` -> `200`

## Live assertions

- Home latest points to `a-home-robot-is-not-a-box-with-a-ribbon`: `True`
- Home latest uses the expected alt text: `True`
- `0014` cover present: `True`
- `0015` cover present: `True`
- `0016` cover present: `True`
- `0017` has no `<img>` tag: `True`
- `0017` has no `og:image`: `True`
- `0017` preserved the GitHub release link: `True`
- `0018` cover present: `True`
- `diary-index.json count`: `18`
- `diary-index.json latest`: `a-home-robot-is-not-a-box-with-a-ribbon`
- Same-date order `2026-01-09`: `why-visual-perception-matters-only-after-memory-exists | how-ai-should-live-with-humans-when-the-world-is-already-in-crisis`
- Same-date order `2026-01-10`: `why-thinking-ai-wont-take-over-the-world | reality-bound-ai-l4-public-release-v1-2-0`
- `0017` tag count in `diary-index.json`: `0`
- No polluted `Cybernetics.` tag on live surfaces: `True`
- No `untagged` tag page or tag entry generated: `True`
- `diary-feed.xml` item count: `18`

## Live tag counts

- `ai-architecture`: `10`
- `ai-safety`: `7`
- `l4-boundary`: `9`
- `cybernetics`: `11`
- `complex-systems`: `4`
- `agi`: `7`
- `advanced-global-intelligence`: `4`
- `human-ai`: `4`
- `protocol-design`: `2`
- `deep-tech`: `8`
- `l4`: `1`
- `privacy-by-design`: `1`
- `affective-systems`: `2`
- `future-of-living`: `1`
- `decentralized-ai`: `2`
