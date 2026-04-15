# Post-Deploy Check

- Contract: `SITE_AUTHORITY_EVIDENCE_LAYER_V04`
- Repository: `Kot141078/kot141078.github.io`
- Authority/evidence commit under test: `b48e1c990729533b3d8c939f6c9013241d179ff2`
- GitHub Pages build id: `959142198`
- GitHub Pages build status: `built`
- Build duration: `33725 ms`
- Pages URL: `https://ivankotov.eu/`
- Custom domain: `ivankotov.eu`
- HTTPS enforced: `true`
- HTTPS certificate state: `approved`

## External URL Checks

| URL | Status | Content-Type | Key checks |
| --- | --- | --- | --- |
| `https://ivankotov.eu/` | `200` | `text/html; charset=utf-8` | `ProfilePage`, `Person`, `Public works and evidence`, canonical to `/` |
| `https://ivankotov.eu/publications/` | `200` | `text/html; charset=utf-8` | `CollectionPage`, `ItemList`, `BreadcrumbList`, canonical to `/publications/` |
| `https://ivankotov.eu/releases/` | `200` | `text/html; charset=utf-8` | `CollectionPage`, `ItemList`, `BreadcrumbList`, canonical to `/releases/` |
| `https://ivankotov.eu/evidence/` | `200` | `text/html; charset=utf-8` | `WebPage`, `BreadcrumbList`, evidence definition line, canonical to `/evidence/` |
| `https://ivankotov.eu/reading-path/` | `200` | `text/html; charset=utf-8` | `Next step` block present, canonical to `/reading-path/` |
| `https://ivankotov.eu/glossary/` | `200` | `text/html; charset=utf-8` | `DefinedTermSet`, canonical to `/glossary/` |
| `https://ivankotov.eu/works-index.json` | `200` | `application/json; charset=utf-8` | JSON served and contains `Ivan Kotov` |
| `https://ivankotov.eu/humans.txt` | `200` | `text/plain; charset=utf-8` | human-readable anchor file served |
| `https://ivankotov.eu/llms.txt` | `200` | `text/plain; charset=utf-8` | includes `/publications/`, `/releases/`, `/evidence/`, `/works-index.json` |
| `https://ivankotov.eu/sitemap.xml` | `200` | `application/xml` | includes `/publications/`, `/releases/`, `/evidence/` |

## Notes

- External smoke-check passed with no missing markers.
- No DNS or GitHub Pages configuration changes were required for v0.4.
- This post-deploy artifact was added after the tested authority/evidence build completed.
