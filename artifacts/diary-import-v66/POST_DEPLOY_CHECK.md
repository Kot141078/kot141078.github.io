# V66 Post-Deploy Check

Implementation commit: `cf9a4216de4d129fcdd1ec3da12d5c24fbd1f10a`

Cache-bust key: `cf9a4216de4d129fcdd1ec3da12d5c24fbd1f10a`

## Deployment runs

| Workflow/job | ID | Head | Conclusion |
| --- | ---: | --- | --- |
| Pages build and deployment | 33561432858 | `cf9a4216de4d129fcdd1ec3da12d5c24fbd1f10a` | success |
| Pages build job | 100034604181 | same | success |
| Pages deploy job | 100034678234 | same | success |
| Pages report-build-status job | 100034678311 | same | success |
| Machine readability | 33561434461 | same | success |

The implementation commit's GPG signature verified successfully before deployment validation.

## Required route result

Ninety-three cache-busted route checks returned HTTP 200:

- 10 core home/Diary/JSON/XML/robots routes;
- 6 new entry routes;
- 10 new image routes;
- 57 affected detail-tag routes, with the tag index separately included among the core routes;
- 10 protected regression routes.

Core results:

- `/`: homepage latest Diary slot is ENTRY 0217.
- `/diary/`: count 217, date range through 2026-08-16, five latest cards.
- `/diary/archive/`: all six V66 entries are present.
- `/diary/tags/`: canonical tag display remains present.
- `/diary-index.json`: count 217, latest ENTRY 0217 / 2026-08-16.
- `/diary-tags.json`: valid JSON.
- `/diary-latest.json`: ENTRY 0217.
- `/diary-feed.xml`: valid XML.
- `/sitemap.xml`: valid XML, 309 URLs.
- `/robots.txt`: HTTP 200 and semantically identical to the signed source.

## Entry routes

All returned HTTP 200 and matched their signed generated files:

1. `https://ivankotov.eu/diary/published-pasc-f0-gap-closure-scaffold-and-structural-templates-v0-1-1/`
2. `https://ivankotov.eu/diary/every-now-and-then-between-my-usual-thoughts-on-ai-infrastructure-and-machine-intelligence-the-old-pc-geek-in-me-stages-a-small-rebellion/`
3. `https://ivankotov.eu/diary/what-do-we-really-expect-from-ai/`
4. `https://ivankotov.eu/diary/sooner-or-later-we-will-have-to-negotiate-with-ai/`
5. `https://ivankotov.eu/diary/sometimes-useful-reading-for-ai-can-be-found-in-places-where-nobody-thinks-to-look/`
6. `https://ivankotov.eu/diary/the-ai-system-is-not-the-model/`

Remote V23: `PASS`.

Remote V28: `PASS`, exact order ENTRY 0217, 0216, 0215, 0214, 0213. ENTRY 0212 is sixth and does not displace the five-card preview.

Each of the six activity IDs and slugs occurs exactly once among the 217 remote `diary-index.json.items` records. Remote duplicate guard: `PASS`.

## Image routes

All ten returned HTTP 200 with the expected media type and matched their supplied/local bytes:

| Entry/order | Destination asset | Bytes | SHA-256 | Remote type |
| --- | --- | ---: | --- | --- |
| 0212/1 | `cover.jpg` | 285029 | `9d41e9a2bea0b1e972048d8284b3551ae4fdfc75c65b1aa594a5f1a0a3b5a425` | `image/jpeg` |
| 0213/1 | `cover.jpg` | 229634 | `d25d34882785c6f1de15baaeebf33c830cf58bca95653aa4f78f5fbcf94f6f93` | `image/jpeg` |
| 0214/1 | `cover.jpg` | 230411 | `168175f61baebec4d68d3117a9ffd0c4740c3feaa5b304c1b516a7d827dfd68b` | `image/jpeg` |
| 0215/1 | `cover.jpg` | 228308 | `f3662419b8987717a2cd1d243784661e92af9af19f6a8f2d0df073f275272ebf` | `image/jpeg` |
| 0216/1 | `cover.jpg` | 283825 | `376ce8fb3e5fbd0dde614a9cca434db2c88d80bdd4877c280ce6465738918876` | `image/jpeg` |
| 0216/2 | `image-02.jpg` | 272878 | `4f06b653ec879d8d2fcb0f5a801da93778dbbadf4168bc3f934747f9a12f7613` | `image/jpeg` |
| 0216/3 | `image-03.jpg` | 357097 | `9698f7065ca723bea10f22d07cf79d9978b1592f00d0f01cefb08fc8370da8cb` | `image/jpeg` |
| 0216/4 | `image-04.jpg` | 235785 | `47180d6913007663c7a2de3db04717e036f95bc5a2def3744f6f06b44fd8a747` | `image/jpeg` |
| 0216/5 | `image-05.jpg` | 279503 | `5bd18bd98358b6ff253fd96b7cbd586a5f36f27d4c6f4154b302ce503b2a4ef1` | `image/jpeg` |
| 0217/1 | `cover.png` | 2624481 | `dc58c8fbc5f91a0f5598c99f81175bcf5a9f87045c513b904844536aac59d531` | `image/png` |

ENTRY 0216 remote DOM contains one lead figure and four ordered gallery figures. All five images load at 1672x941; extras are lazy/async; no carousel exists. ENTRY 0217 begins with the valid PNG signature and displays normally.

## Affected tag routes

All 57 affected detail-tag routes returned HTTP 200, contained `noindex`, and remained absent from `sitemap.xml`:

`agentic-ai`, `agenticai`, `ai-alignment`, `ai-architecture`, `ai-governance`, `ai-safety`, `ai`, `aialignment`, `aiarchitecture`, `aigovernance`, `aisafety`, `artificial-intelligence`, `artificialintelligence`, `cloud-gaming`, `cloudgaming`, `continuity`, `cybernetics`, `digital-continuity`, `digital-identity`, `digitalcontinuity`, `digitalidentity`, `digitalownership`, `dlss`, `engineering`, `future-of-ai`, `futureofai`, `futureofgaming`, `gamedevelopment`, `gamingindustry`, `gamingtechnology`, `geforcenow`, `governance`, `hotas`, `human-ai`, `humanai`, `humancomputerinteraction`, `immersivetechnology`, `llm`, `local-ai`, `local-first-ai`, `local-first`, `localfirstai`, `machineintelligence`, `on-prem-ai`, `pasc`, `pavelbazhov`, `pcgaming`, `persistent-ai`, `persistentai`, `philosophyofai`, `postanchorgovernance`, `provenance`, `simracing`, `systems-thinking`, `systemsthinking`, `useragency`, `vr`.

The `/diary/tags/` index also returned HTTP 200 and retained `noindex`. Thus all 58 changed tag HTML files (57 detail pages plus the index) remain noindex. Tag-page sitemap additions: 0.

## Sitemap result

- Baseline: 303 URLs.
- Deployed: 309 URLs.
- Six V66 entry URLs: present.
- Affected tag URLs: 0.
- Removed URLs: 0.
- Corpus JSON endpoints: 0.
- Remote sitemap set equals the signed local sitemap set.

## Critical source/render checks

- ENTRY 0212 PASC status block: exact.
- ENTRY 0215 control and negotiated relationship blocks: exact.
- ENTRY 0216 Open Library author/work anchors: present and clickable.
- ENTRY 0217 authored punctuation and final paired statements: exact.
- Windows local paths in new remote HTML: none.
- Placeholder text in new remote HTML: none.

## Protected routes and regressions

All returned HTTP 200 and matched signed local content after normalizing only CRLF/LF transport differences where applicable:

- `/start-here/`
- `/corpus/`
- `/corpus/changes/`
- `/corpus/open-problems/`
- `/corpus/protocol-map/`
- `/vision/`
- `/publications/`
- `/publications/esther-rp-001/`
- `/distinctions/`
- `/install-c/`

The implementation diff changed zero tracked files under Corpus, Vision, Publications, Start here, Distinctions, install-c, or robots.txt. Living Corpus V62, Agent/c V63, Vision V64, ESTHER-RP-001 V61, publications, and navigation regressions: `PASS`.

## Remote visual artifacts

Output root: `C:\Users\kotov\Downloads\111\diary-v66-visual\`

| Artifact | Dimensions | SHA-256 |
| --- | --- | --- |
| `final-remote-diary-desktop-1440x900.png` | 1440x900 | `4df9456df6b7f68667de9a86a59051f96a6b0cdd027d760a85ee7b6e7c633c47` |
| `final-remote-diary-mobile-390x844.png` | 390x844 | `8f8050783f4139d34bede29c4c552594adfaa07dda993ba619634af5ae62df58` |
| `final-remote-home-desktop-1440x900.png` | 1440x900 | `66ad8aab71dd1e3d1d3bdbb90165dc40a18f7245b0ea9f647405b1aad4d6bb79` |
| `final-remote-entry0216-desktop-1440x900.png` | 1440x900 | `b57f4c37519236061b8e0fa1a33c9068c0e9ce6aa6eb8948b915872c288ed405` |
| `final-remote-entry0216-mobile-390x844.png` | 390x844 | `67e521b5dbe7f209b3000554b56bafa0120d614b75415d55e64f4c9f8a1702ae` |
| `final-remote-entry0217-desktop-1440x900.png` | 1440x900 | `3dc3fabf852512a92a7378aab03554247a45552290452b8bea429bec7ef36d8c` |

Desktop gallery is a balanced 2x2 presentation. At mobile width, document and scroll width both equal 390 pixels, all images load, and the gallery remains one column. Remote visual verdict: `PASS`.
