# Post-Deploy Check

- Contract: `SITE_IDENTITY_CORPUS_MAP_V05`
- Repository: `Kot141078/kot141078.github.io`
- Identity/corpus commit under test: `9d91161339ce246da98b14a7dcae83e75a611bd0`
- GitHub Pages build id: `959178144`
- GitHub Pages build status: `built`
- Build duration: `41020 ms`
- Pages URL: `https://ivankotov.eu/`
- Custom domain: `ivankotov.eu`
- HTTPS enforced: `true`
- HTTPS certificate state: `approved`

## External URL Checks

| URL | Status | Content-Type | Key checks |
| --- | --- | --- | --- |
| `https://ivankotov.eu/` | `200` | `text/html; charset=utf-8` | `ProfilePage`, `/about/`, `/corpus-map/`, stylesheet link |
| `https://ivankotov.eu/about/` | `200` | `text/html; charset=utf-8` | `ProfilePage`, `Person`, `AI Systems Architect`, canonical to `/about/` |
| `https://ivankotov.eu/corpus-map/` | `200` | `text/html; charset=utf-8` | `CollectionPage`, `ItemList`, `BreadcrumbList`, canonical to `/corpus-map/` |
| `https://ivankotov.eu/glossary/` | `200` | `text/html; charset=utf-8` | `DefinedTermSet`, `corpus`, `public anchor` |
| `https://ivankotov.eu/reading-path/` | `200` | `text/html; charset=utf-8` | orientation note with `About` and `Corpus map` |
| `https://ivankotov.eu/publications/` | `200` | `text/html; charset=utf-8` | publications page still reachable |
| `https://ivankotov.eu/works-index.json` | `200` | `application/json; charset=utf-8` | includes `about_url` and `corpus_map_url` |
| `https://ivankotov.eu/about.json` | `200` | `application/json; charset=utf-8` | machine-readable author identity layer served |
| `https://ivankotov.eu/humans.txt` | `200` | `text/plain; charset=utf-8` | includes `About` and `Corpus map` block |
| `https://ivankotov.eu/llms.txt` | `200` | `text/plain; charset=utf-8` | includes `About`, `Corpus map`, and preference note |
| `https://ivankotov.eu/sitemap.xml` | `200` | `application/xml` | includes `/about/` and `/corpus-map/` |
| `https://ivankotov.eu/styles.css` | `200` | `text/css; charset=utf-8` | CSS asset reachable; table and base theme rules present |

## Notes

- Required HTML pages return `200`.
- Required machine-readable files return `200`.
- `/about/` exposes `ProfilePage` + `Person`.
- `/corpus-map/` exposes `CollectionPage` + `ItemList` + `BreadcrumbList`.
- Internal identity/corpus links sampled from the deployed HTML are present, and the linked core targets in this check return `200`.
- No deploy-time evidence of broken styling was observed in the static asset check.
