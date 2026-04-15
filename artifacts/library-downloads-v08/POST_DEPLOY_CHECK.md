# Post-Deploy Check

- Contract: `SITE_LIBRARY_DOWNLOADS_LAYER_V08`
- Checked on: `2026-04-15`
- Deploy commit under test: `09f7f1b3d153c5dbed1656e064ffdfa357929eba`
- GitHub Pages build: `959251911`
- Build status: `built`

## External URL checks

- `https://ivankotov.eu/` -> `200`; `/library/` and `/downloads/` links present; stylesheet linked
- `https://ivankotov.eu/library/` -> `200`; canonical points to `/library/`; `CollectionPage`, `ItemList`, and `BreadcrumbList` present; main source cards render
- `https://ivankotov.eu/downloads/` -> `200`; canonical points to `/downloads/`; `CollectionPage`, `ItemList`, and `BreadcrumbList` present; release/archive table and book matrix render
- `https://ivankotov.eu/publications/` -> `200`; `/library/` link present; canonical remains in place
- `https://ivankotov.eu/releases/` -> `200`; `/downloads/` link present; canonical remains in place
- `https://ivankotov.eu/qubit-of-hope/` -> `200`; `/downloads/` link present; canonical remains in place
- `https://ivankotov.eu/start-here/` -> `200`; `/library/` and `/downloads/` links present; canonical remains in place
- `https://ivankotov.eu/questions/` -> `200`; new question about primary sources/downloads is present; `/library/` and `/downloads/` links present; canonical remains in place
- `https://ivankotov.eu/library-index.json` -> `200`; JSON served; page and role fields visible
- `https://ivankotov.eu/downloads-index.json` -> `200`; JSON served; AGI, SER, and Qubit entries visible
- `https://ivankotov.eu/llms.txt` -> `200`; contains `/library/`, `/downloads/`, `/library-index.json`, `/downloads-index.json`, and the primary-source note
- `https://ivankotov.eu/sitemap.xml` -> `200`; contains `/library/` and `/downloads/`
- `https://ivankotov.eu/styles.css` -> `200`; root/body/nav rules present

## Result

- Status: `PASS`
- New library/downloads layer is reachable from the public domain
- Machine-readable source/download indexes are live
- Internal site bridges to the new layer are visible from home, start-here, questions, publications, releases, and the book page
- Style layer remains intact in the public deployment
