# V24 Post-Deploy Check

Contract: `SITE_DIARY_IMPORT_BATCH_0024_0028_V24`
Date: `2026-04-18`
Deployment result: converged on first live check

## Live status

- `https://ivankotov.eu/` -> `200`
- `https://ivankotov.eu/diary/` -> `200`
- `https://ivankotov.eu/diary/archive/` -> `200`
- `https://ivankotov.eu/diary/tags/` -> `200`
- `https://ivankotov.eu/diary/living-with-an-always-on-interface-the-quiet-shift/` -> `200`
- `https://ivankotov.eu/diary/the-problem-of-digital-sensory-deprivation-or-why-ai-needs-fresh-air/` -> `200`
- `https://ivankotov.eu/diary/why-obedience-is-the-most-dangerous-property-of-ai/` -> `200`
- `https://ivankotov.eu/diary/when-an-ai-stops-being-a-tool-and-becomes-a-presence/` -> `200`
- `https://ivankotov.eu/diary/the-right-to-slowness-why-delay-is-a-safety-feature/` -> `200`
- `https://ivankotov.eu/diary/tags/private-ai/` -> `200`
- `https://ivankotov.eu/diary/tags/human-centered-ai/` -> `200`
- `https://ivankotov.eu/diary/tags/persistent-memory/` -> `200`
- `https://ivankotov.eu/diary/tags/local-ai/` -> `200`
- `https://ivankotov.eu/diary/tags/ai-interfaces/` -> `200`
- `https://ivankotov.eu/diary/tags/long-term-thinking/` -> `200`
- `https://ivankotov.eu/diary/tags/even-g2/` -> `200`
- `https://ivankotov.eu/diary/tags/systems-architecture/` -> `200`
- `https://ivankotov.eu/diary/tags/cognitive-science/` -> `200`
- `https://ivankotov.eu/diary/tags/ai-alignment/` -> `200`
- `https://ivankotov.eu/diary/tags/perception-router/` -> `200`
- `https://ivankotov.eu/diary/tags/digital-entities/` -> `200`
- `https://ivankotov.eu/diary/tags/temporal-ai/` -> `200`
- `https://ivankotov.eu/diary/tags/l4/` -> `200`
- `https://ivankotov.eu/diary/tags/future-of-ai/` -> `200`
- `https://ivankotov.eu/diary/tags/ai-safety/` -> `200`
- `https://ivankotov.eu/diary/tags/ai-architecture/` -> `200`
- `https://ivankotov.eu/diary/tags/cybernetics/` -> `200`
- `https://ivankotov.eu/diary/tags/systems-engineering/` -> `200`
- `https://ivankotov.eu/diary/tags/trust-and-safety/` -> `200`
- `https://ivankotov.eu/diary/tags/identity/` -> `200`
- `https://ivankotov.eu/diary/tags/least-privilege/` -> `200`
- `https://ivankotov.eu/diary/tags/ai-entities/` -> `200`
- `https://ivankotov.eu/diary/tags/systems-thinking/` -> `200`
- `https://ivankotov.eu/diary/tags/presence/` -> `200`
- `https://ivankotov.eu/diary/tags/slow-intelligence/` -> `200`
- `https://ivankotov.eu/diary/tags/right-to-pause/` -> `200`
- `https://ivankotov.eu/diary-index.json` -> `200`
- `https://ivankotov.eu/diary-tags.json` -> `200`
- `https://ivankotov.eu/diary-feed.xml` -> `200`
- `https://ivankotov.eu/sitemap.xml` -> `200`
- `https://ivankotov.eu/assets/diary/living-with-an-always-on-interface-the-quiet-shift/cover.jpg` -> `200`
- `https://ivankotov.eu/assets/diary/the-problem-of-digital-sensory-deprivation-or-why-ai-needs-fresh-air/cover.jpg` -> `200`
- `https://ivankotov.eu/assets/diary/why-obedience-is-the-most-dangerous-property-of-ai/cover.jpg` -> `200`
- `https://ivankotov.eu/assets/diary/when-an-ai-stops-being-a-tool-and-becomes-a-presence/cover.jpg` -> `200`
- `https://ivankotov.eu/assets/diary/the-right-to-slowness-why-delay-is-a-safety-feature/cover.jpg` -> `200`

## Live assertions

- home latest-post meta span count: `1`
- home latest-post meta equals only a date: `True`
- home latest-post headline: `When an AI Stops Being a Tool - and Becomes a Presence`
- home has no old extra meta pattern: `True`
- `/diary/` first card meta span count: `1`
- `/diary/` first card meta equals only a date: `True`
- `/diary/archive/` first card meta span count: `1`
- `/diary/archive/` first card meta equals only a date: `True`
- all five new entry pages show their intended cover images: `True`
- `diary-index.json count`: `28`
- `diary-index.json latest`: `when-an-ai-stops-being-a-tool-and-becomes-a-presence`
- Same-date order `2026-01-13`: `why-superintelligence-is-not-what-sci-fi-promised | why-faster-is-not-better-and-why-asimov-was-solving-the-wrong-problem | living-with-an-always-on-interface-the-quiet-shift`
- Same-date order `2026-01-14`: `why-obedience-is-the-most-dangerous-property-of-ai | the-problem-of-digital-sensory-deprivation-or-why-ai-needs-fresh-air`
- Same-date order `2026-01-15`: `when-an-ai-stops-being-a-tool-and-becomes-a-presence | the-right-to-slowness-why-delay-is-a-safety-feature`
- `diary-feed.xml` item count: `28`
- previous entry `why-superintelligence-is-not-what-sci-fi-promised` still live: `True`
- live tag pages checked from `diary-tags.json`: `89`
- live tag pages with bad meta blocks: `0`

## Live tag counts

- `private-ai`: `2`
- `human-centered-ai`: `5`
- `persistent-memory`: `1`
- `local-ai`: `2`
- `ai-interfaces`: `1`
- `long-term-thinking`: `2`
- `even-g2`: `1`
- `systems-architecture`: `1`
- `cognitive-science`: `1`
- `ai-alignment`: `1`
- `perception-router`: `1`
- `digital-entities`: `1`
- `temporal-ai`: `1`
- `l4`: `7`
- `future-of-ai`: `5`
- `ai-safety`: `11`
- `ai-architecture`: `13`
- `cybernetics`: `16`
- `systems-engineering`: `1`
- `trust-and-safety`: `1`
- `identity`: `1`
- `least-privilege`: `1`
- `ai-entities`: `4`
- `systems-thinking`: `6`
- `presence`: `1`
- `slow-intelligence`: `2`
- `right-to-pause`: `1`
