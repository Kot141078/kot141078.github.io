# Search Console Submission Plan V62

Date: 2026-07-19

## Submit

Submit the updated sitemap:

- `https://ivankotov.eu/sitemap.xml`

New HTML routes included in the sitemap:

- `https://ivankotov.eu/corpus/`
- `https://ivankotov.eu/corpus/protocol-map/`
- `https://ivankotov.eu/corpus/current-state/`
- `https://ivankotov.eu/corpus/open-problems/`
- `https://ivankotov.eu/corpus/failures/`
- `https://ivankotov.eu/corpus/changes/`

Updated existing route:

- `https://ivankotov.eu/start-here/`

## Do Not Submit As Sitemap URLs

The corpus JSON endpoints are public receipts but are not sitemap URLs in V62:

- `https://ivankotov.eu/corpus-index.json`
- `https://ivankotov.eu/corpus-current.json`
- `https://ivankotov.eu/corpus-protocol-map.json`
- `https://ivankotov.eu/corpus-open-problems.json`
- `https://ivankotov.eu/corpus-failures.json`
- `https://ivankotov.eu/corpus-changes.json`
- `https://ivankotov.eu/corpus-canonical-sources.json`

## Local Pre-Submission Checks

- Local HTTP 200 check for all six new corpus HTML routes: PASS
- Local HTTP 200 check for `/start-here/`: PASS
- Sitemap parse check: PASS
- Sitemap total: 804 URLs
- New corpus HTML URLs present: 6/6
- Corpus JSON URLs present in sitemap: 0
- Claim-boundary and privacy scan for public HTML/JSON: PASS

