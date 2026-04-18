# V22 Post-Deploy Check

Contract: `SITE_DIARY_IMPORT_BATCH_0019_0023_V22`
Date: `2026-04-18`
Deployment result: converged on first live check

## Live status

- `https://ivankotov.eu/` -> `200`
- `https://ivankotov.eu/diary/` -> `200`
- `https://ivankotov.eu/diary/archive/` -> `200`
- `https://ivankotov.eu/diary/tags/` -> `200`
- `https://ivankotov.eu/diary/why-the-market-is-underestimating-home-robots/` -> `200`
- `https://ivankotov.eu/diary/checklist-are-you-ready-for-a-robot-at-home/` -> `200`
- `https://ivankotov.eu/diary/context-length-is-not-understanding/` -> `200`
- `https://ivankotov.eu/diary/why-superintelligence-is-not-what-sci-fi-promised/` -> `200`
- `https://ivankotov.eu/diary/why-faster-is-not-better-and-why-asimov-was-solving-the-wrong-problem/` -> `200`
- `https://ivankotov.eu/diary/tags/robotics/` -> `200`
- `https://ivankotov.eu/diary/tags/ai-products/` -> `200`
- `https://ivankotov.eu/diary/tags/human-centered-ai/` -> `200`
- `https://ivankotov.eu/diary/tags/l4-boundary/` -> `200`
- `https://ivankotov.eu/diary/tags/tech-reality/` -> `200`
- `https://ivankotov.eu/diary/tags/future-economy/` -> `200`
- `https://ivankotov.eu/diary/tags/ai-design/` -> `200`
- `https://ivankotov.eu/diary/tags/ai-entities/` -> `200`
- `https://ivankotov.eu/diary/tags/human-ai-future/` -> `200`
- `https://ivankotov.eu/diary/tags/tech-and-life/` -> `200`
- `https://ivankotov.eu/diary/tags/ai-at-home/` -> `200`
- `https://ivankotov.eu/diary/tags/soft-safety/` -> `200`
- `https://ivankotov.eu/diary/tags/ai-architecture/` -> `200`
- `https://ivankotov.eu/diary/tags/context-is-not-understanding/` -> `200`
- `https://ivankotov.eu/diary/tags/real-world-ai/` -> `200`
- `https://ivankotov.eu/diary/tags/deep-tech/` -> `200`
- `https://ivankotov.eu/diary/tags/systems-thinking/` -> `200`
- `https://ivankotov.eu/diary/tags/ai-safety/` -> `200`
- `https://ivankotov.eu/diary/tags/ai-reality/` -> `200`
- `https://ivankotov.eu/diary/tags/l4/` -> `200`
- `https://ivankotov.eu/diary/tags/post-scifi-ai/` -> `200`
- `https://ivankotov.eu/diary/tags/cybernetics/` -> `200`
- `https://ivankotov.eu/diary/tags/future-of-ai/` -> `200`
- `https://ivankotov.eu/diary/tags/systems-over-myths/` -> `200`
- `https://ivankotov.eu/diary/tags/asimov/` -> `200`
- `https://ivankotov.eu/diary/tags/slow-intelligence/` -> `200`
- `https://ivankotov.eu/diary-index.json` -> `200`
- `https://ivankotov.eu/diary-tags.json` -> `200`
- `https://ivankotov.eu/diary-feed.xml` -> `200`
- `https://ivankotov.eu/sitemap.xml` -> `200`
- `https://ivankotov.eu/assets/diary/why-the-market-is-underestimating-home-robots/cover.jpg` -> `200`
- `https://ivankotov.eu/assets/diary/checklist-are-you-ready-for-a-robot-at-home/cover.jpg` -> `200`
- `https://ivankotov.eu/assets/diary/context-length-is-not-understanding/cover.jpg` -> `200`
- `https://ivankotov.eu/assets/diary/why-superintelligence-is-not-what-sci-fi-promised/cover.jpg` -> `200`
- `https://ivankotov.eu/assets/diary/why-faster-is-not-better-and-why-asimov-was-solving-the-wrong-problem/cover.jpg` -> `200`

## Live assertions

- Home latest points to `why-superintelligence-is-not-what-sci-fi-promised`: `True`
- Home latest uses the expected alt text: `True`
- `0019` cover present: `True`
- `0020` cover present: `True`
- `0021` cover present: `True`
- `0022` cover present: `True`
- `0023` cover present: `True`
- `0021` platform noise absent on live page: `True`
- `0021` platform noise absent in live `diary-index.json`: `True`
- `0021` platform noise absent in live `diary-feed.xml`: `True`
- `diary-index.json count`: `23`
- `diary-index.json latest`: `why-superintelligence-is-not-what-sci-fi-promised`
- Same-date order `2026-01-11`: `why-the-market-is-underestimating-home-robots | a-home-robot-is-not-a-box-with-a-ribbon`
- Same-date order `2026-01-12`: `context-length-is-not-understanding | checklist-are-you-ready-for-a-robot-at-home`
- Same-date order `2026-01-13`: `why-superintelligence-is-not-what-sci-fi-promised | why-faster-is-not-better-and-why-asimov-was-solving-the-wrong-problem`
- `diary-feed.xml` item count: `23`
- `sitemap.xml` contains `why-faster-is-not-better-and-why-asimov-was-solving-the-wrong-problem`: `True`
- `sitemap.xml` contains `ai-products` tag page: `True`
- Previous entry `a-home-robot-is-not-a-box-with-a-ribbon` still live: `True`

## Live tag counts

- `robotics`: `3`
- `ai-products`: `1`
- `human-centered-ai`: `2`
- `l4-boundary`: `12`
- `tech-reality`: `1`
- `future-economy`: `1`
- `ai-design`: `1`
- `ai-entities`: `3`
- `human-ai-future`: `1`
- `tech-and-life`: `1`
- `ai-at-home`: `1`
- `soft-safety`: `2`
- `ai-architecture`: `11`
- `context-is-not-understanding`: `1`
- `real-world-ai`: `1`
- `deep-tech`: `10`
- `systems-thinking`: `4`
- `ai-safety`: `9`
- `ai-reality`: `1`
- `l4`: `3`
- `post-scifi-ai`: `1`
- `cybernetics`: `13`
- `future-of-ai`: `4`
- `systems-over-myths`: `1`
- `asimov`: `1`
- `slow-intelligence`: `1`
