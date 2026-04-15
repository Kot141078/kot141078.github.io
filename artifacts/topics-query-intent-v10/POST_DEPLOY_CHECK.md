# POST_DEPLOY_CHECK

- contract: `SITE_TOPICS_QUERY_INTENT_LAYER_V10`
- checked_on: `2026-04-15`
- deploy_commit_under_test: `f7fe191c08c60e585e1a5955f83930ddd1979400`
- github_pages_build: `959315989`
- github_pages_status: `built`

## External URL checks

- `https://ivankotov.eu/` -> `200`
- `https://ivankotov.eu/topics/` -> `200`
- `https://ivankotov.eu/ai-governance/` -> `200`
- `https://ivankotov.eu/local-first-ai/` -> `200`
- `https://ivankotov.eu/long-lived-ai-entities/` -> `200`
- `https://ivankotov.eu/start-here/` -> `200`
- `https://ivankotov.eu/questions/` -> `200`
- `https://ivankotov.eu/services/` -> `200`
- `https://ivankotov.eu/use-cases/` -> `200`
- `https://ivankotov.eu/topics-index.json` -> `200`
- `https://ivankotov.eu/llms.txt` -> `200`
- `https://ivankotov.eu/sitemap.xml` -> `200`

## Content checks

- `/topics/` contains `CollectionPage`, `ItemList`, `BreadcrumbList`, canonical, and links to all three topic pages
- `/ai-governance/`, `/local-first-ai/`, `/long-lived-ai-entities/` contain `WebPage`, `BreadcrumbList`, required title/meta/canonical, and expected related links
- `/start-here/`, `/questions/`, `/services/`, `/use-cases/` expose the required topic-layer links
- `topics-index.json`, `llms.txt`, and `sitemap.xml` expose the required new URLs and notes
- home page exposes the new `Topics` nav link and compact topic-entry block

## Result

- `PASS`
