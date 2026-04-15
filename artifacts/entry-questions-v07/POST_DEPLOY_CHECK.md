# Post-Deploy Check

- Contract: `SITE_ENTRY_QUESTIONS_LAYER_V07`
- Checked on: `2026-04-15`
- Deploy commit under test: `bed58776721fac536c43e0ae8f00e1215ab988c6`
- GitHub Pages build: `959220974`
- Build status: `built`

## External URL checks

- `https://ivankotov.eu/` -> `200`; `ProfilePage` present; links to `/start-here/` and `/questions/`; stylesheet linked
- `https://ivankotov.eu/about/` -> `200`; canonical points to `/about/`; `/start-here/` entry link present
- `https://ivankotov.eu/glossary/` -> `200`; canonical points to `/glossary/`; `/questions/` reference present
- `https://ivankotov.eu/reading-path/` -> `200`; canonical points to `/reading-path/`; `/start-here/` entry link present
- `https://ivankotov.eu/start-here/` -> `200`; canonical points to `/start-here/`; `WebPage` and `BreadcrumbList` present; `Questions` link present
- `https://ivankotov.eu/questions/` -> `200`; canonical points to `/questions/`; `FAQPage` and `BreadcrumbList` present; first question present; links to `/distinctions/` and `/reading-path/` present
- `https://ivankotov.eu/start-here.json` -> `200`; JSON served; `sequence` length `7`; includes `/about/` and `/qubit-of-hope/`
- `https://ivankotov.eu/questions.json` -> `200`; JSON served; `items` length `10`; includes `What does AGI mean here?` and `How should the corpus be read?`
- `https://ivankotov.eu/llms.txt` -> `200`; contains `/start-here/`, `/questions/`, `/start-here.json`, `/questions.json`, and the first-pass orientation note
- `https://ivankotov.eu/sitemap.xml` -> `200`; contains `/start-here/` and `/questions/`
- `https://ivankotov.eu/styles.css` -> `200`; CSS asset reachable; root/body/nav rules present

## Result

- Status: `PASS`
- Entry layer deployed and reachable from the public domain
- Query layer deployed and reachable from the public domain
- Machine-readable entry files are live and parseable
- Navigation surfaces expose the new entry points without breaking the existing style layer
