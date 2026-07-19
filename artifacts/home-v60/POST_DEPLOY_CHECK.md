# Post-Deploy Check V60

## Deployment

Implementation commit:

`07bde9f2fdc6fa18221e2e89944c5228fe285b44`

GitHub Pages workflow:

- Workflow: `pages-build-deployment`
- Run ID: `29692675430`
- Conclusion: success
- Build job: `88208043890`, success, 28s
- Report-build-status job: `88208091299`, success, 5s
- Deploy job: `88208091338`, success, 8s

GitHub Actions emitted a non-failing Node.js runtime deprecation warning during the Pages run. The deployment itself concluded successfully.

## Remote Validation

Public target:

`https://ivankotov.eu/`

Cache token:

`v60-20260719172234`

Required route checks:

| Route | HTTP status |
| --- | ---: |
| `/` | 200 |
| `/start-here/` | 200 |
| `/what-is-running/` | 200 |
| `/publications/` | 200 |
| `/diary/` | 200 |
| `/library/` | 200 |
| `/services/` | 200 |
| `/about/` | 200 |
| `/contact/` | 200 |
| `/install-c/` | 200 |
| `/diary-index.json` | 200 |
| `/diary-latest.json` | 200 |
| `/sitemap.xml` | 200 |

Remote homepage structural checks:

- Section order exact: pass
- One `h1`: pass
- Unified hero: pass
- `Three ways in` appears once: pass
- `How to install c` appears once: pass
- `Latest post` appears once: pass
- Latest post uses current Diary latest: pass
- Featured public work cards: 4
- Core concept cards: 3
- Explore routes: 6
- Compact book card: pass
- `Reality before rhetoric` appears once: pass
- Full publication catalogue absent: pass
- Timeline absent: pass
- Duplicate route systems absent: pass
- Homepage internal links resolve: pass

Remote Diary receipts:

- Diary public count: 206
- Diary item count: 206
- Latest date: `2026-07-18`
- Latest slug: `the-question-behind-c-a-b-is-not-whether-an-ai-can-look-consistent-over-time`

Remote sitemap receipts:

- Local sitemap URL count: 797
- Remote sitemap URL count: 797
- Added URLs: 0
- Removed URLs: 0

## Remote Visual Receipts

Stored under:

`C:\Users\kotov\Downloads\111\home-v60-visual\after`

| Receipt | Size |
| --- | ---: |
| `final-remote-v60-desktop-1440x900.png` | 169385 bytes |
| `final-remote-v60-mobile-390x844.png` | 61938 bytes |
| `final-remote-v60-full-page-desktop.png` | 867300 bytes |
| `final-remote-v60-print-a4.pdf` | 4782975 bytes |

Remote print receipt:

- PDF pages: 7

## Protected Surfaces

No V60 implementation diff was present in:

- `content/diary/*.md`
- `assets/diary/**`
- `diary/index.html`
- `diary-index.json`
- `diary-latest.json`
- `sitemap.xml`
- `robots.txt`

## Verdict

PASS.
