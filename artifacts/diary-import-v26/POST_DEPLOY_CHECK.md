# POST_DEPLOY_CHECK

## Live status

All required V26 URLs returned `200` on `2026-04-18`.

### Core surfaces

- `https://ivankotov.eu/`
- `https://ivankotov.eu/diary/`
- `https://ivankotov.eu/diary/archive/`
- `https://ivankotov.eu/diary/tags/`
- `https://ivankotov.eu/diary-index.json`
- `https://ivankotov.eu/diary-tags.json`
- `https://ivankotov.eu/diary-latest.json`
- `https://ivankotov.eu/diary-feed.xml`
- `https://ivankotov.eu/sitemap.xml`

### New entries

- `https://ivankotov.eu/diary/why-control-always-fails-at-scale-and-why-we-keep-trying-anyway/`
- `https://ivankotov.eu/diary/the-great-ai-barter-why-sovereign-entities-are-the-best-friends-of-big-tech/`
- `https://ivankotov.eu/diary/are-you-actually-ready-for-a-robot-at-home/`
- `https://ivankotov.eu/diary/release-v1-3-0-sovereign-entity-recursion-ser/`
- `https://ivankotov.eu/diary/when-presence-becomes-violence/`

### Image assets

- `https://ivankotov.eu/assets/diary/why-control-always-fails-at-scale-and-why-we-keep-trying-anyway/cover.jpg`
- `https://ivankotov.eu/assets/diary/are-you-actually-ready-for-a-robot-at-home/cover.jpg`
- `https://ivankotov.eu/assets/diary/when-presence-becomes-violence/cover.jpg`

## Live machine-readable state

- `diary-index.json` count: `38`
- `diary-index.json` latest slug: `when-presence-becomes-violence`
- `diary-latest.json` latest slug: `when-presence-becomes-violence`
- `diary-feed.xml` item count: `38`
- Same-date ordering:
  - `2026-01-18=why-control-always-fails-at-scale-and-why-we-keep-trying-anyway | on-wearable-ai-interfaces-why-elegance-matters-more-than-features`
  - `2026-01-20=the-great-ai-barter-why-sovereign-entities-are-the-best-friends-of-big-tech | are-you-actually-ready-for-a-robot-at-home`
  - `2026-01-21=when-presence-becomes-violence | release-v1-3-0-sovereign-entity-recursion-ser`

## Integrity checks

- Home latest-post changed from `on-wearable-ai-interfaces-why-elegance-matters-more-than-features` to `when-presence-becomes-violence`
- Home latest-post meta line is still date-only: `true`
- `/diary/` bad entry-card meta blocks: `0`
- `/diary/archive/` bad entry-card meta blocks: `0`
- Live tag pages checked for bad meta: `97`
- Live tag pages with bad meta: `0`
- Imaged entries show intended cover assets: `true`
- Image-less entries `0035` and `0037` render without placeholder images: `true`
- Shared-source-URL case for `0035` remains correct:
  - `the-great-ai-barter`
  - `the-great-ai-barter-why-sovereign-entities-are-the-best-friends-of-big-tech`
- `POST 0037` remains untagged on the live machine-readable layer: `true`
- `POST 0035` GitHub link is present on the live page: `true`
- `POST 0037` release link is present on the live page: `true`
- New `soft-boundaries` tag surface exists on the live site: `true`
- No fake image or placeholder was introduced

## Live affected tag counts

- `ai-safety=16`
- `system-design=2`
- `cybernetics=22`
- `l4=14`
- `complex-systems=6`
- `ai-architecture=16`
- `deep-tech=12`
- `responsible-ai=2`
- `ai-economy=2`
- `big-tech=2`
- `synthetic-data=2`
- `future-of-ai=8`
- `b2b=2`
- `partnership=2`
- `home-robots=2`
- `ai-entities=7`
- `privacy-by-design=2`
- `human-systems=3`
- `future-of-living=2`
- `presence=2`
- `soft-boundaries=1`
