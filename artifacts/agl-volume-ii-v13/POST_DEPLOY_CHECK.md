# Post-Deploy Check

Contract: `SITE_AGL_AND_VOLUME_II_INTEGRATION_V13`  
Date: `2026-04-18`  
Base URL: `https://ivankotov.eu/`  
Integration commit checked: `9b9e45162f73f45d4c3c77446bc0b29732b61752`

## Method

- Live HTTP checks via PowerShell `Invoke-WebRequest`.
- HTML checks: `200`, title, meta description, canonical, shared stylesheet, required structural strings, schema markers where required.
- JSON checks: `200`, valid JSON parse, expected `title` and `page`.
- Text checks: `200`, expected entries in `llms.txt` and `sitemap.xml`.

## Endpoint Results

| Path | Status | Key checks | Result |
| --- | --- | --- | --- |
| `/` | `200` | title, meta, canonical, shared stylesheet, `New layers`, AGL link, Volume II link | PASS |
| `/actor-grounding-layer/` | `200` | title, meta, canonical, shared stylesheet, `WebPage`, `BreadcrumbList`, canonical AGL copy | PASS |
| `/qubit-of-hope-volume-ii/` | `200` | title, meta, canonical, shared stylesheet, `Book`, `BreadcrumbList`, cover, Volume I / hub / download references | PASS |
| `/l4/` | `200` | title, meta, canonical, shared stylesheet, AGL link present | PASS |
| `/corpus-map/` | `200` | title, meta, canonical, shared stylesheet, AGL node, Volume II node | PASS |
| `/evidence/` | `200` | title, meta, canonical, shared stylesheet, AGL reviewable-layer mention | PASS |
| `/qubit-of-hope/` | `200` | title, meta, canonical, shared stylesheet, `CollectionPage`, `BreadcrumbList`, Volume I + Volume II hub structure | PASS |
| `/library/` | `200` | title, meta, canonical, shared stylesheet, AGL source surface, Volume II source surface | PASS |
| `/downloads/` | `200` | title, meta, canonical, shared stylesheet, AGL document surface, Volume II release/file matrix | PASS |
| `/publications/` | `200` | title, meta, canonical, shared stylesheet, AGL public work surface, Volume II public work surface | PASS |
| `/reading-path/` | `200` | title, meta, canonical, shared stylesheet, AGL step, Volume II continuation step | PASS |
| `/start-here/` | `200` | title, meta, canonical, shared stylesheet, compact AGL + Volume II entry links | PASS |
| `/questions/` | `200` | title, meta, canonical, shared stylesheet, AGL question, Volume II question | PASS |
| `/actor-grounding-layer.json` | `200` | valid JSON, title `Actor Grounding Layer`, canonical page URL | PASS |
| `/qubit-of-hope-volume-ii.json` | `200` | valid JSON, title `Qubit of Hope — Volume II`, canonical page URL | PASS |
| `/llms.txt` | `200` | includes AGL page, Volume II page, both JSON files, explicit usage line for grounding and narrative continuation layers | PASS |
| `/sitemap.xml` | `200` | includes `/actor-grounding-layer/` and `/qubit-of-hope-volume-ii/` | PASS |

## Findings

- All required endpoints responded with `200`.
- All required HTML pages exposed title, meta description, canonical URL, and the shared stylesheet reference.
- `/actor-grounding-layer/` exposes `WebPage` + `BreadcrumbList`.
- `/qubit-of-hope-volume-ii/` exposes `Book` + `BreadcrumbList`.
- `/qubit-of-hope/` now acts as a structural hub for Volume I and Volume II rather than a single-volume leaf.
- JSON endpoints parsed successfully and returned the expected canonical `title` and `page` fields.
- `llms.txt` and `sitemap.xml` include the new AGL and Volume II surfaces.
- The live HTML confirms cross-linking from the surrounding corpus pages, so the integration is structural rather than a pair of isolated leaf pages.
- Shared stylesheet references remain in place across the new and updated pages, so no style drift was observed from the live HTML layer.

## Verdict

`PASS`

AGL integration status after pass: `PRESENT_AND_STRUCTURAL`  
Volume II integration status after pass: `PRESENT_AND_STRUCTURAL`  
Integration type after pass: `STRUCTURAL`
