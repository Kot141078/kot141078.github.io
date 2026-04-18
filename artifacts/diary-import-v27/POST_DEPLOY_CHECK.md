# POST_DEPLOY_CHECK_V27

## Live URL Status

All URLs below returned `200` in the production check:

- `https://ivankotov.eu/`
- `https://ivankotov.eu/diary/`
- `https://ivankotov.eu/diary/archive/`
- `https://ivankotov.eu/diary/tags/`
- `https://ivankotov.eu/diary/why-asics-decentralized-ai-and-a-rack-in-the-garage-are-the-same-story/`
- `https://ivankotov.eu/diary/cognition-is-not-a-single-scale-a-clarification/`
- `https://ivankotov.eu/diary/ai-infrastructure-why-the-future-is-neither-cloud-only-nor-garage-only/`
- `https://ivankotov.eu/diary/how-ai-unexpectedly-taught-me-how-to-play-life-play-is-a-metaphor/`
- `https://ivankotov.eu/diary/ocean-is-earths-cosmos-only-here-the-space-is-alive/`
- `https://ivankotov.eu/diary/tags/cognition/`
- `https://ivankotov.eu/diary/tags/asic/`
- `https://ivankotov.eu/diary/tags/ser/`
- `https://ivankotov.eu/diary/tags/ocean/`
- `https://ivankotov.eu/diary/tags/deep-sea/`
- `https://ivankotov.eu/diary/tags/c-a-b/`
- `https://ivankotov.eu/diary/tags/applied-cybernetics/`
- `https://ivankotov.eu/diary/tags/reality-bound-ai/`
- `https://ivankotov.eu/diary/tags/ai-and-nature/`
- `https://ivankotov.eu/diary/tags/human-non-human-intelligence/`
- `https://ivankotov.eu/diary/tags/multi-intelligence-systems/`
- `https://ivankotov.eu/diary/tags/ecological-ai/`
- `https://ivankotov.eu/diary-index.json`
- `https://ivankotov.eu/diary-tags.json`
- `https://ivankotov.eu/diary-latest.json`
- `https://ivankotov.eu/diary-feed.xml`
- `https://ivankotov.eu/sitemap.xml`
- `https://ivankotov.eu/assets/diary/why-asics-decentralized-ai-and-a-rack-in-the-garage-are-the-same-story/cover.jpg`
- `https://ivankotov.eu/assets/diary/cognition-is-not-a-single-scale-a-clarification/cover.jpg`
- `https://ivankotov.eu/assets/diary/ai-infrastructure-why-the-future-is-neither-cloud-only-nor-garage-only/cover.jpg`
- `https://ivankotov.eu/assets/diary/how-ai-unexpectedly-taught-me-how-to-play-life-play-is-a-metaphor/cover.jpg`
- `https://ivankotov.eu/assets/diary/ocean-is-earths-cosmos-only-here-the-space-is-alive/cover.jpg`

## Live Data Checks

- `diary-index.json count = 43`: pass
- `diary-index.json latest.slug = ocean-is-earths-cosmos-only-here-the-space-is-alive`: pass
- `diary-latest.json item.slug = ocean-is-earths-cosmos-only-here-the-space-is-alive`: pass
- `2026-01-22` order in live `diary-index.json`:
- `why-asics-decentralized-ai-and-a-rack-in-the-garage-are-the-same-story`
- `cognition-is-not-a-single-scale-a-clarification`
- `2026-01-23` order in live `diary-index.json`:
- `how-ai-unexpectedly-taught-me-how-to-play-life-play-is-a-metaphor`
- `ai-infrastructure-why-the-future-is-neither-cloud-only-nor-garage-only`
- live `cybernetics` tag bucket count = `25`: pass
- live `cybernetics` display label = `Cybernetics`: pass
- live `POST 0043` tag count in `diary-index.json` = `17`: pass
- live `POST 0043` preserved long-tag list exactly: pass

## Live UI Checks

- home latest-post slot shows `2026-01-24`: pass
- home latest-post title is `Ocean is Earth's cosmos - only here, the "space" is alive.`: pass
- home latest-post link points to `/diary/ocean-is-earths-cosmos-only-here-the-space-is-alive/`: pass
- home latest-post meta line contains date only: pass
- `/diary/` lists all five imported posts: pass
- `/diary/` card meta lines contain date only: pass
- no `date - slug/title/tags/count` regression found in the live home slot or live diary cards: pass

## Live Structured Data Checks

- live `POST 0042` page contains `BlogPosting`: pass
- live `POST 0042` page contains its canonical URL: pass
- live `POST 0043` page contains `BlogPosting`: pass
- live `POST 0043` page contains its canonical URL: pass

## Conclusion

- V27 deploy is live.
- New entries, new tag pages, updated JSON/RSS outputs, updated home latest-post state, and updated sitemap are all present on production.
- No fake image or duplicate lowercase `cybernetics` bucket was introduced.
