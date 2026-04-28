# Post-Deploy Check — Kotov Principle L4-Bound Experience V44

Contract: `SITE_KOTOV_PRINCIPLE_L4_BOUND_EXPERIENCE_V44`  
Base URL: `https://ivankotov.eu/`  
Integration commit checked: `69112951e8ecba29ba9deab9923eaab6672dbf2f`  
GitHub Pages build id: `976779486`  
GitHub Pages build status: `built`

## Method

- Live HTTP checks via PowerShell `Invoke-WebRequest`.
- HTML checks: status `200`, title/meta/canonical, schema markers, stylesheet reference, expected Kotov Principle links.
- JSON check: status `200`, valid JSON parse, expected title and page fields.
- Text checks: `llms.txt` includes the page and JSON endpoint; `sitemap.xml` includes the HTML page.
- External release checks: GitHub release page and three release asset links respond with `200`.

## Endpoint Results

| Path | Status | Key checks | Result |
| --- | --- | --- | --- |
| `/` | `200` | shared stylesheet | PASS |
| `/kotov-principle-l4-bound-experience/` | `200` | title, meta, canonical, `CreativeWork`, `BreadcrumbList`, release link, asset link | PASS |
| `/publications/` | `200` | stylesheet, Kotov Principle link | PASS |
| `/releases/` | `200` | stylesheet, Kotov Principle link | PASS |
| `/evidence/` | `200` | stylesheet, Kotov Principle link | PASS |
| `/library/` | `200` | stylesheet, Kotov Principle link | PASS |
| `/downloads/` | `200` | stylesheet, Kotov Principle link | PASS |
| `/l4/` | `200` | stylesheet, Kotov Principle link | PASS |
| `/advanced-global-intelligence/` | `200` | stylesheet, Kotov Principle link | PASS |
| `/kotov-principle-l4-bound-experience.json` | `200` | valid JSON, expected title, expected page URL | PASS |
| `/llms.txt` | `200` | includes `/kotov-principle-l4-bound-experience/` and `/kotov-principle-l4-bound-experience.json` | PASS |
| `/sitemap.xml` | `200` | includes `https://ivankotov.eu/kotov-principle-l4-bound-experience/` | PASS |

## External Release Links

| URL | Status | Result |
| --- | --- | --- |
| `https://github.com/Kot141078/advanced-global-intelligence/releases/tag/kotov-principle-l4-bound-experience-v0.1.1` | `200` | PASS |
| `https://github.com/Kot141078/advanced-global-intelligence/releases/download/kotov-principle-l4-bound-experience-v0.1.1/KOTOV_PRINCIPLE_L4_BOUND_EXPERIENCE.md` | `200` | PASS |
| `https://github.com/Kot141078/advanced-global-intelligence/releases/download/kotov-principle-l4-bound-experience-v0.1.1/KOTOV_PRINCIPLE_L4_BOUND_EXPERIENCE_v0.1.1.pdf` | `200` | PASS |
| `https://github.com/Kot141078/advanced-global-intelligence/releases/download/kotov-principle-l4-bound-experience-v0.1.1/KOTOV_PRINCIPLE_L4_BOUND_EXPERIENCE_v0.1.1.sha256` | `200` | PASS |

## Findings

- All required URLs returned `200`.
- The new page exposes title, meta description, canonical URL, `CreativeWork`, and `BreadcrumbList`.
- The machine-readable JSON endpoint returns valid JSON and the expected canonical page URL.
- Release asset links are external GitHub release links; no release assets were copied into the site repo.
- `sitemap.xml` includes the new HTML page and does not include the JSON endpoint.
- The shared stylesheet is referenced on checked HTML pages.

## Verdict

`PASS`
