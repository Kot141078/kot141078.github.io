# Post-Deploy Check

- Contract: `SITE_SERVICES_USECASES_CONTACT_V09`
- Checked on: `2026-04-15`
- Deploy commit under test: `aca76f39e68c72c0db2d864cbfa1f086438cb5ad`
- GitHub Pages build: `959290442`
- Build status: `built`

## External URL checks

- `https://ivankotov.eu/` -> `200`; `/services/`, `/use-cases/`, and `/contact/` links present; stylesheet linked
- `https://ivankotov.eu/services/` -> `200`; canonical points to `/services/`; `CollectionPage`, `ItemList`, and `BreadcrumbList` present; service directions render
- `https://ivankotov.eu/use-cases/` -> `200`; canonical points to `/use-cases/`; `CollectionPage`, `ItemList`, and `BreadcrumbList` present; use-case blocks render
- `https://ivankotov.eu/contact/` -> `200`; canonical points to `/contact/`; `ContactPage` and `BreadcrumbList` present; public anchor cards render
- `https://ivankotov.eu/about/` -> `200`; `/services/` link present; canonical remains in place
- `https://ivankotov.eu/start-here/` -> `200`; `/services/` and `/use-cases/` links present; canonical remains in place
- `https://ivankotov.eu/questions/` -> `200`; new practical-directions question is present; `/services/` and `/use-cases/` links present; canonical remains in place
- `https://ivankotov.eu/services.json` -> `200`; JSON served; grounded service titles visible
- `https://ivankotov.eu/use-cases.json` -> `200`; JSON served; practical situations visible
- `https://ivankotov.eu/contact.json` -> `200`; JSON served; GitHub / LinkedIn / ORCID / HAL anchors visible
- `https://ivankotov.eu/llms.txt` -> `200`; contains `/services/`, `/use-cases/`, `/contact/`, `/services.json`, `/use-cases.json`, `/contact.json`, and the practical-entry notes
- `https://ivankotov.eu/sitemap.xml` -> `200`; contains `/services/`, `/use-cases/`, and `/contact/`
- `https://ivankotov.eu/styles.css` -> `200`; root/body/nav rules present

## Result

- Status: `PASS`
- New services/use-cases/contact layer is reachable from the public domain
- Machine-readable practical-entry and contact indexes are live
- Internal site bridges to the new layer are visible from home, about, start-here, and questions
- Style layer remains intact in the public deployment
