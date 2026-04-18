# Post-Deploy Check — V20

Date: 2026-04-18
Implementation commit: `2a09172be5a3dd2cbe87e053bd6c985576b0e315`
Resolved entry slugs: `why-ai-entities-must-have-limits`, `empathy-is-not-magic`, `why-1000000-token-context-windows-are-not-the-solution`, `nvidia-didnt-pivot-nvidia-looked-ahead`, `why-id-put-an-ai-rack-in-my-garage`
Primary domain: `https://ivankotov.eu/`

## Live status check

- `/` -> `200`
- `/diary/` -> `200`
- `/diary/archive/` -> `200`
- `/diary/tags/` -> `200`
- `/diary/why-ai-entities-must-have-limits/` -> `200`
- `/diary/empathy-is-not-magic/` -> `200`
- `/diary/why-1000000-token-context-windows-are-not-the-solution/` -> `200`
- `/diary/nvidia-didnt-pivot-nvidia-looked-ahead/` -> `200`
- `/diary/why-id-put-an-ai-rack-in-my-garage/` -> `200`
- `/diary/why-ai-entities-can-act-as-a-safety-filter/` -> `200`
- `/diary/the-great-ai-barter/` -> `200`
- `/diary/tags/digital-sovereignty/` -> `200`
- `/diary/tags/ai-architecture/` -> `200`
- `/diary/tags/l4-boundary/` -> `200`
- `/diary/tags/affective-computing/` -> `200`
- `/diary/tags/cybernetics/` -> `200`
- `/diary/tags/deep-tech/` -> `200`
- `/diary/tags/future-of-ai/` -> `200`
- `/diary/tags/ai-entities/` -> `200`
- `/diary/tags/advanced-global-intelligence/` -> `200`
- `/diary/tags/affective-systems/` -> `200`
- `/diary/tags/ai-infrastructure/` -> `200`
- `/diary/tags/ces2026/` -> `200`
- `/diary/tags/coexistence/` -> `200`
- `/diary/tags/cognitive-infrastructure/` -> `200`
- `/diary/tags/context-engineering/` -> `200`
- `/diary/tags/distillation/` -> `200`
- `/diary/tags/edge-ai/` -> `200`
- `/diary/tags/human-centered-ai/` -> `200`
- `/diary/tags/llm/` -> `200`
- `/diary/tags/local-ai/` -> `200`
- `/diary/tags/long-term-memory/` -> `200`
- `/diary/tags/long-term-thinking/` -> `200`
- `/diary/tags/nvidia/` -> `200`
- `/diary/tags/philosophy-of-code/` -> `200`
- `/diary/tags/post-cloud/` -> `200`
- `/diary/tags/private-ai/` -> `200`
- `/diary/tags/system-design/` -> `200`
- `/diary/tags/systems-thinking/` -> `200`
- `/diary/tags/tech-ethics/` -> `200`
- `/diary/tags/true-judge/` -> `200`
- `diary-index.json` -> `200`
- `diary-tags.json` -> `200`
- `diary-feed.xml` -> `200`
- `sitemap.xml` -> `200`
- `assets/diary/why-ai-entities-must-have-limits/cover.jpg` -> `200`
- `assets/diary/empathy-is-not-magic/cover.jpg` -> `200`
- `assets/diary/nvidia-didnt-pivot-nvidia-looked-ahead/cover.jpg` -> `200`
- `assets/diary/why-id-put-an-ai-rack-in-my-garage/cover.jpg` -> `200`

## Validation assertions

- home latest-post title is `Why I'd Put an AI Rack in My Garage`: pass
- home latest-post link points to `/diary/why-id-put-an-ai-rack-in-my-garage/`: pass
- home latest-post image points to `/assets/diary/why-id-put-an-ai-rack-in-my-garage/cover.jpg`: pass
- home latest-post image alt matches the factual resolved alt text: pass
- `/diary/` includes all five imported posts: pass
- `/diary/archive/` includes all five imported posts: pass
- `/diary/tags/` includes the expanded tag set: pass
- `0009` page renders the supplied image: pass
- `0010` page preserves `math.log(emotion) + vector_memory`: pass
- `0010` page renders the supplied image: pass
- `0011` page renders without `og:image`: pass
- `0011` page renders without an `<img>` tag: pass
- `0011` page still exposes `BlogPosting`: pass
- `0012` page renders the supplied image: pass
- `0013` page renders the supplied image: pass
- `diary-index.json` count is `13`: pass
- `diary-index.json` latest slug is `why-id-put-an-ai-rack-in-my-garage`: pass
- `diary-index.json` `2026-01-06` order is `why-ai-entities-must-have-limits | empathy-is-not-magic`: pass
- `diary-index.json` `2026-01-07` order is `why-1000000-token-context-windows-are-not-the-solution | nvidia-didnt-pivot-nvidia-looked-ahead`: pass
- `diary-tags.json` `digital-sovereignty` count is `2`: pass
- `diary-tags.json` `ai-architecture` count is `6`: pass
- `diary-tags.json` `l4-boundary` count is `6`: pass
- `diary-tags.json` `llm` count is `1`: pass
- `diary-tags.json` `advanced-global-intelligence` count is `1`: pass
- `diary-tags.json` `long-term-memory` count is `2`: pass
- `diary-tags.json` `systems-thinking` count is `2`: pass
- `diary-tags.json` `nvidia` count is `1`: pass
- `diary-tags.json` `edge-ai` count is `2`: pass
- `diary-tags.json` `private-ai` count is `1`: pass
- `diary-tags.json` `ai-infrastructure` count is `1`: pass
- `diary-tags.json` `human-centered-ai` count is `1`: pass
- `diary-feed.xml` contains `13` items: pass
- `sitemap.xml` includes `/diary/why-id-put-an-ai-rack-in-my-garage/`: pass
- `sitemap.xml` includes `/diary/tags/private-ai/`: pass
- shared-source strategy for `0012` and `0013` produced two independent deployed asset URLs: pass
- shared-source asset copies return `image/jpeg` on both URLs: pass
- shared-source asset copies match in byte length under the chosen strategy: pass
- previously imported entry `why-ai-entities-can-act-as-a-safety-filter` still renders: pass
- previously imported entry `the-great-ai-barter` still renders: pass
- no fake image or placeholder was introduced anywhere: pass

## No fake image confirmation

- `0009`, `0010`, `0012`, and `0013` use only the supplied image files: pass
- `0011` remained explicitly image-less: pass
- no replacement or placeholder image was introduced on any new entry page: pass
- no replacement or placeholder image was introduced in the home latest-post slot: pass

## Pages build trace

- public deploy was already converged on the first live check after push
- full affected URL set returned `200` on first live validation pass
