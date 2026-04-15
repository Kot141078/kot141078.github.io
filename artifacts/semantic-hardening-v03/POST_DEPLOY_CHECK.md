# POST_DEPLOY_CHECK

Date: `2026-04-15`

Target commit:

- `de8162461db75ebae874557d1babfb238b7cc251`

Pages build:

- build id: `959099322`
- status: `built`

## URL checks

- `https://ivankotov.eu/` — `200`, expected title present, canonical tag present, meta description present
- `https://ivankotov.eu/advanced-global-intelligence/` — `200`, expected title present, canonical tag present, meta description present, `BreadcrumbList` present
- `https://ivankotov.eu/c-a-plus-b/` — `200`, expected title present, canonical tag present, meta description present, `BreadcrumbList` present
- `https://ivankotov.eu/l4/` — `200`, expected title present, canonical tag present, meta description present, `BreadcrumbList` present
- `https://ivankotov.eu/ser/` — `200`, expected title present, canonical tag present, meta description present, `BreadcrumbList` present
- `https://ivankotov.eu/qubit-of-hope/` — `200`, expected title present, canonical tag present, meta description present, `BreadcrumbList` present, `Book` schema present
- `https://ivankotov.eu/glossary/` — `200`, expected title present, canonical tag present, meta description present, `BreadcrumbList` present, `DefinedTermSet` present
- `https://ivankotov.eu/reading-path/` — `200`, expected title present, canonical tag present, meta description present, `BreadcrumbList` present
- `https://ivankotov.eu/sitemap.xml` — `200`, contains `/glossary/` and `/reading-path/`
- `https://ivankotov.eu/llms.txt` — `200`, contains glossary and reading-path lines
- `https://ivankotov.eu/canonical-map.json` — `200`, parsed successfully, `nodes=7`, `reading_path=5`

## Result

- Pages open
- title / meta / canonical are in place
- `BreadcrumbList` is present where required
- structured data is not visibly broken in the checked surfaces
- `llms.txt` and `canonical-map.json` are served
- canonical page URLs and book URL are live
