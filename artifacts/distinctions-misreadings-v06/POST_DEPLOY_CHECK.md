# Post-Deploy Check

- Contract: `SITE_DISTINCTIONS_MISREADINGS_V06`
- Repository: `Kot141078/kot141078.github.io`
- Distinctions/misreadings commit under test: `5b855e0eb51e37284bb4eb79713c0f30685510fc`
- GitHub Pages build id: `959197601`
- GitHub Pages build status: `built`
- Build duration: `33675 ms`
- Pages URL: `https://ivankotov.eu/`
- Custom domain: `ivankotov.eu`
- HTTPS enforced: `true`
- HTTPS certificate state: `approved`

## External URL Checks

| URL | Status | Content-Type | Key checks |
| --- | --- | --- | --- |
| `https://ivankotov.eu/` | `200` | `text/html; charset=utf-8` | home returns `ProfilePage`, distinctions link, misreadings link, stylesheet link |
| `https://ivankotov.eu/about/` | `200` | `text/html; charset=utf-8` | `ProfilePage`, `Person`, distinctions link, canonical to `/about/` |
| `https://ivankotov.eu/corpus-map/` | `200` | `text/html; charset=utf-8` | `CollectionPage`, `ItemList`, `BreadcrumbList`, semantic hygiene note present |
| `https://ivankotov.eu/glossary/` | `200` | `text/html; charset=utf-8` | distinctions phrase marker present, distinctions link present, `See distinctions.` marker present |
| `https://ivankotov.eu/reading-path/` | `200` | `text/html; charset=utf-8` | `After glossary` note, distinctions link, misreadings link |
| `https://ivankotov.eu/distinctions/` | `200` | `text/html; charset=utf-8` | `CollectionPage`, `ItemList`, `BreadcrumbList`, negative-frame section present |
| `https://ivankotov.eu/misreadings/` | `200` | `text/html; charset=utf-8` | `CollectionPage`, `ItemList`, `BreadcrumbList`, final note present |
| `https://ivankotov.eu/distinctions.json` | `200` | `application/json; charset=utf-8` | machine-readable distinctions layer served |
| `https://ivankotov.eu/misreadings.json` | `200` | `application/json; charset=utf-8` | machine-readable misreadings layer served |
| `https://ivankotov.eu/llms.txt` | `200` | `text/plain; charset=utf-8` | includes distinctions pages, JSON files, and summarization note |
| `https://ivankotov.eu/sitemap.xml` | `200` | `application/xml` | includes `/distinctions/` and `/misreadings/` |
| `https://ivankotov.eu/styles.css` | `200` | `text/css; charset=utf-8` | CSS asset reachable; base theme and table rules present |

## Notes

- Required HTML pages return `200`.
- Required JSON files return `200`.
- `/distinctions/` exposes `CollectionPage` + `ItemList` + `BreadcrumbList`.
- `/misreadings/` exposes `CollectionPage` + `ItemList` + `BreadcrumbList`.
- Sampled internal semantic links are present in the deployed HTML, and the linked core targets in this check return `200`.
- No deploy-time evidence of broken styling was observed in the static asset check.
