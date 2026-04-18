# Post-Deploy Check — V19

Date: 2026-04-18
Implementation commit: `7836a25200422ca02489ca0524f4b0bdda438708`
Resolved entry slugs: `geoffrey-hinton-is-right-ai-is-immortal`, `the-great-ai-barter`, `why-a-real-ai-entity-has-no-reason-to-lie`, `why-ai-entities-can-act-as-a-safety-filter`, `we-are-discarding-our-most-valuable-asset-lived-human-experience`
Primary domain: `https://ivankotov.eu/`

## Live status check

- `/` -> `200`
- `/diary/` -> `200`
- `/diary/archive/` -> `200`
- `/diary/tags/` -> `200`
- `/diary/geoffrey-hinton-is-right-ai-is-immortal/` -> `200`
- `/diary/the-great-ai-barter/` -> `200`
- `/diary/why-a-real-ai-entity-has-no-reason-to-lie/` -> `200`
- `/diary/why-ai-entities-can-act-as-a-safety-filter/` -> `200`
- `/diary/we-are-discarding-our-most-valuable-asset-lived-human-experience/` -> `200`
- `/diary/proof-of-reality/` -> `200`
- `/diary/we-are-building-a-partner/` -> `200`
- `/diary/tags/ai-safety/` -> `200`
- `/diary/tags/geoffrey-hinton/` -> `200`
- `/diary/tags/cybernetics/` -> `200`
- `/diary/tags/engineering/` -> `200`
- `/diary/tags/robotics/` -> `200`
- `/diary/tags/eu-ai-act/` -> `200`
- `/diary/tags/deep-tech/` -> `200`
- `/diary/tags/ai-economy/` -> `200`
- `/diary/tags/big-tech/` -> `200`
- `/diary/tags/synthetic-data/` -> `200`
- `/diary/tags/future-of-ai/` -> `200`
- `/diary/tags/b2b/` -> `200`
- `/diary/tags/partnership/` -> `200`
- `/diary/tags/complex-systems/` -> `200`
- `/diary/tags/l4-boundary/` -> `200`
- `/diary/tags/affective-computing/` -> `200`
- `/diary/tags/ai-entities/` -> `200`
- `/diary/tags/parenting-in-tech/` -> `200`
- `/diary/tags/soft-safety/` -> `200`
- `/diary/tags/ai-architecture/` -> `200`
- `/diary/tags/human-capital/` -> `200`
- `/diary/tags/economy-of-meaning/` -> `200`
- `/diary/tags/future-of-work/` -> `200`
- `/diary/tags/age-tech/` -> `200`
- `diary-index.json` -> `200`
- `diary-tags.json` -> `200`
- `diary-feed.xml` -> `200`
- `sitemap.xml` -> `200`
- `assets/diary/geoffrey-hinton-is-right-ai-is-immortal/cover.jpg` -> `200`
- `assets/diary/why-a-real-ai-entity-has-no-reason-to-lie/cover.jpg` -> `200`
- `assets/diary/why-ai-entities-can-act-as-a-safety-filter/cover.jpg` -> `200`
- `assets/diary/we-are-discarding-our-most-valuable-asset-lived-human-experience/cover.jpg` -> `200`

## Validation assertions

- home latest-post title is `Why AI Entities Can Act as a Safety Filter`: pass
- home latest-post link points to `/diary/why-ai-entities-can-act-as-a-safety-filter/`: pass
- home latest-post image points to `/assets/diary/why-ai-entities-can-act-as-a-safety-filter/cover.jpg`: pass
- home latest-post image alt matches the factual resolved alt text: pass
- `/diary/` includes all five imported posts: pass
- `/diary/archive/` includes all five imported posts: pass
- `/diary/tags/` includes the expanded tag set: pass
- `0004` page renders the supplied image: pass
- `0005` page renders without `og:image`: pass
- `0005` page renders without an `<img>` tag: pass
- `0005` page still exposes `BlogPosting`: pass
- `0006` page renders the supplied image: pass
- `0007` page renders the supplied image: pass
- `0008` page renders the supplied image: pass
- `0008` page renders the external link `https://lnkd.in/eut_425U`: pass
- `0007` page exposes `BlogPosting`: pass
- `0008` page exposes `BlogPosting`: pass
- `diary-index.json` count is `8`: pass
- `diary-index.json` latest slug is `why-ai-entities-can-act-as-a-safety-filter`: pass
- `diary-index.json` `2026-01-03` order is `we-are-building-a-partner | geoffrey-hinton-is-right-ai-is-immortal`: pass
- `diary-index.json` `2026-01-05` order is `why-ai-entities-can-act-as-a-safety-filter | why-a-real-ai-entity-has-no-reason-to-lie | we-are-discarding-our-most-valuable-asset-lived-human-experience`: pass
- `diary-tags.json` `ai-safety` count is `4`: pass
- `diary-tags.json` `cybernetics` count is `5`: pass
- `diary-tags.json` `l4-boundary` count is `3`: pass
- `diary-tags.json` `ai-architecture` count is `2`: pass
- `diary-tags.json` `ai-economy` count is `1`: pass
- `diary-tags.json` `human-capital` count is `1`: pass
- `diary-feed.xml` contains `8` items: pass
- `sitemap.xml` includes `/diary/the-great-ai-barter/`: pass
- `sitemap.xml` includes `/diary/tags/l4-boundary/`: pass
- previously imported entry `proof-of-reality` still renders: pass
- previously imported entry `we-are-building-a-partner` still renders: pass
- no fake image or placeholder was introduced anywhere: pass

## No fake image confirmation

- `0004`, `0006`, `0007`, and `0008` use only the supplied image files: pass
- `0005` remained explicitly image-less: pass
- no replacement or placeholder image was introduced on any new entry page: pass
- no replacement or placeholder image was introduced in the home latest-post slot: pass

## Pages build trace

- public deploy was already converged on the first live check after push
- full affected URL set returned `200` on first live validation pass
