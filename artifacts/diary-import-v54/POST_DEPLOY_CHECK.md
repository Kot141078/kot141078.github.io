# Post Deploy Check V54

Implementation commit validated: `aed4860abb51399fd726c7c221d3b3c1276f5cd3`

Public deployment observed at `https://ivankotov.eu/` after `origin/main` updated.

GitHub Pages run: `29654986503` (`https://github.com/Kot141078/kot141078.github.io/actions/runs/29654986503`), conclusion `success`.

## HTTP Results

- New entry pages: `5/5` HTTP 200.
- New image assets: `3/3` HTTP 200.
- Affected tag pages: `30/30` HTTP 200.
- Core surfaces: `9/9` HTTP 200:
  - `/`
  - `/diary/`
  - `/diary/archive/`
  - `/diary/tags/`
  - `/diary-index.json`
  - `/diary-tags.json`
  - `/diary-latest.json`
  - `/diary-feed.xml`
  - `/sitemap.xml`

## Parse Results

- Selected live HTML pages: `39/39` parsed (`5` entries, `30` affected tag pages, and `4` core HTML surfaces).
- Strict live JSON: `3/3` parsed without duplicate keys or UTF-8 BOM.
- Live XML: `2/2` parsed with entity resolution and network access disabled.

## State Checks

- Remote `diary-index.json` count: `190`.
- Remote latest slug: `a-small-external-comment-turned-into-a-useful-control-layer-correction`.
- Remote home latest-post: ENTRY 0187, dated `2026-06-30`.
- Existing ENTRY 0182 remained present immediately below the five new entries.
- Remote top order:
  1. `2026-06-30` / `a-small-external-comment-turned-into-a-useful-control-layer-correction`
  2. `2026-06-29` / `bounded-capability-extraction-clause-v0-2-1`
  3. `2026-06-28` / `the-industry-is-building-a-staircase-to-nowhere-while-true-intelligence-requires-a-foundation`
  4. `2026-06-27` / `pavel-durovs-original-speech-english-oslo-freedom-forum-june-2026`
  5. `2026-06-26` / `self-evo-document-package-v0-1-1`
  6. `2026-06-21` / `article-50-transparency-implementation-briefs-v0-1`

## Regression Checks

- V23 date-only meta fix: pass.
- V28 five-entry preview fix: pass; remote `/diary/` latest preview has `5` entry cards.
- ENTRY 0184 and ENTRY 0186 image-less without placeholders: pass.
- Three image assets reproduce their source SHA-256 hashes: pass.
- Ten supplied source URLs are preserved as clickable anchors: pass.
- Duplicate import check: each new slug occurs exactly once in the remote index.
- Remote `sitemap.xml` includes all five V54 entry URLs and all 30 affected tag URLs: `35/35` pass.

## Sitemap

- Builder automatic sitemap update: no.
- Manual narrow sitemap repair: yes.
- Missing URLs added before deployment: `19` (`5` entries plus `14` newly required tag URLs).
- URLs removed: `0`.

## Manual Remainder

Submit URLs from `SEARCH_CONSOLE_SUBMISSION_PLAN_V54.md` to Search Console. No Search Console submission is claimed by this run.
