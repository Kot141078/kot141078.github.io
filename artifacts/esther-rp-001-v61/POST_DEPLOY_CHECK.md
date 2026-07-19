# Post-Deploy Check V61

## Deployment

Implementation commit:

`a9e6fa19a37168134b4c813df8240c94474e3328`

Implementation Pages run:

- Run ID: `29701587490`
- Conclusion: success
- Build job: `88231418197`, success, 33s
- Report-build-status job: `88231467690`, success, 3s
- Deploy job: `88231467693`, success, 11s

GitHub Actions emitted a non-failing Node.js 20 deprecation warning. The Pages deployment succeeded.

## Cache Busting

Remote validation token:

`v61-20260719215840`

Target URL validated:

`https://ivankotov.eu/publications/esther-rp-001/?v61-20260719215840`

Canonical URL remains:

`https://ivankotov.eu/publications/esther-rp-001/`

## Public HTTP Checks

| Route | HTTP status |
| --- | ---: |
| `/` | 200 |
| `/publications/` | 200 |
| `/publications/esther-rp-001/` | 200 |
| `/diary/` | 200 |
| `/start-here/` | 200 |
| `/sitemap.xml` | 200 |

## Computed-Style Checks

Remote desktop 1440 x 900:

- Page overflow: false
- Archive overflow: false
- H1 count: 1
- Header visible: true
- Navigation visible: true
- Footer visible: true
- Full SHA-256 rendered: true
- Raw `pre` block present: false
- Body text color: `rgb(30, 36, 41)`
- Body font: `"Segoe UI", "Trebuchet MS", system-ui, sans-serif`
- H1 font: `Georgia, "Times New Roman", serif`

Remote mobile 390 x 844:

- Page overflow: false
- Archive overflow: false
- Header visible: true
- Navigation visible: true
- Footer visible: true

Remote narrow mobile 320 x 700:

- Page overflow: false
- Archive overflow: false
- Header visible: true
- Navigation visible: true
- Footer visible: true

## Content-Fidelity Checks

Full SHA-256:

`83e71e2fab938e3110293a61967a85440969d8d7eb78a69bf4c1ae40afd4a9d7`

Checks:

- Full SHA-256 present: true
- Truncated SHA-256 present: false
- Archive filename exact: true
- Members `116`: true
- CRC `PASS`: true
- Status statements exact: true
- Evidence values exact: true
- DOI values exact: true
- Claim boundary exact: true
- License line exact: true
- English-only page language: true

Content values changed: 0.

DOI values changed: 0.

Evidence values changed: 0.

## Link Checks

Remote target-page anchors:

- Total unique anchors: 21
- HTTP PASS: 20
- LinkedIn automation block: 1
- Failures: 0

Existing target-page hrefs missing after implementation: 0.

The LinkedIn public profile URL returns HTTP 999 to automated requests while the URL is preserved.

## Metadata Checks

Unchanged:

- `<title>`
- meta description
- canonical URL
- Open Graph title
- Open Graph description
- Open Graph type
- Open Graph URL
- JSON-LD payload
- English language declaration

Metadata verdict: PASS.

## Overflow Checks

Local:

- 1440 px page overflow: false
- 768 px page overflow: false
- 390 px page overflow: false
- 320 px page overflow: false
- 1440 px archive overflow: false
- 768 px archive overflow: false
- 390 px archive overflow: false
- 320 px archive overflow: false

Remote:

- 1440 px page overflow: false
- 390 px page overflow: false
- 320 px page overflow: false
- 1440 px archive overflow: false
- 390 px archive overflow: false
- 320 px archive overflow: false

Overflow verdict: PASS.

## Regression Checks

Homepage V60:

- HTTP 200
- Required markers present
- Verdict: PASS

Diary V59:

- HTTP 200
- Diary count: 206
- Latest slug: `the-question-behind-c-a-b-is-not-whether-an-ai-can-look-consistent-over-time`
- Verdict: PASS

Publications index:

- HTTP 200
- ESTHER-RP-001 marker present
- Verdict: PASS

Comparison publication page:

- `https://ivankotov.eu/publications/cleanroom-arm-p-open-verification-v1-0-1/`
- HTTP 200
- Shared header/navigation markers present
- Verdict: PASS

## Sitemap Comparison

Local sitemap URL count: 798.

Remote sitemap URL count: 798.

URLs added: 0.

URLs removed: 0.

Target URL count: 1.

Sitemap verdict: PASS.

## Final Verdict

PASS.

The live target page is now aligned with the shared ivankotov.eu visual system, no longer forces a standalone dark page, preserves the authoritative full SHA-256 and research identifiers, passes responsive and print checks, and leaves sitemap, homepage, Diary, Publications index, and comparison publication surfaces unchanged.
