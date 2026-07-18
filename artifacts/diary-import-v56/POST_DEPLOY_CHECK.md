# Post Deploy Check V56

Implementation commit validated: `d80227ff5261cbb663f56f04933935c0043299e5`

Public deployment observed at `https://ivankotov.eu/` after `origin/main` updated.

GitHub Pages run: `29658285462` (`https://github.com/Kot141078/kot141078.github.io/actions/runs/29658285462`), conclusion `success`.

## HTTP Results

- New entry pages: `5/5` HTTP 200.
- New image assets: `5/5` HTTP 200.
- Affected tag pages: `36/36` HTTP 200.
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

- Selected live HTML pages: `45/45` parsed (`5` entries, `36` affected tag pages, and `4` core HTML surfaces).
- Strict live JSON: `3/3` parsed without duplicate keys or UTF-8 BOM.
- Live XML: `2/2` parsed with entity resolution and network access disabled.

## State Checks

- Remote `diary-index.json` count: `200`.
- Remote latest slug: `saturday-thought`.
- Remote home latest-post: ENTRY 0197, dated `2026-07-11`.
- Existing ENTRY 0192 remained immediately below the five new entries.
- Remote top order:
  1. `2026-07-11` / `saturday-thought`
  2. `2026-07-09` / `agi-is-not-one-giant-model-it-is-a-system`
  3. `2026-07-08` / `a6-composition-transition-predicate-addendum-v0-1-4`
  4. `2026-07-07` / `c-calculus-governed-binding-stack-v0-1`
  5. `2026-07-06` / `as-local-ai-systems-become-more-persistent-named-memory-bearing-and-emotionally-present-one-safety-problem-moves-from-cloud-ux-into-private-ownership`
  6. `2026-07-05` / `entity-vs-profile-a-witness-root-custody-criterion-for-persistent-digital-entities-v0-1-1`

## Regression and Content Checks

- V23 date-only meta fix: pass.
- V28 five-entry preview fix: pass; remote `/diary/` latest preview has `5` entry cards.
- All five V56 entries are image-bearing: pass.
- Five image assets reproduce their source SHA-256 hashes: pass.
- ENTRY 0193 Reader page and Zenodo DOI links: pass.
- ENTRY 0194 Page, DOI, and GitHub links: pass.
- ENTRY 0195 Publication page, DOI, and Parent A6 artifact links: pass.
- Supplied clickable source-link surfaces: `8/8`.
- ENTRY 0196 preserves `Project Esther` body spelling and `ProjectEsther` tag: pass.
- ENTRY 0197 renders as the latest diary entry and home latest-post: pass.
- Duplicate import check: each new slug occurs exactly once in the remote index.
- Remote `sitemap.xml` includes all five V56 entry URLs and all 36 affected tag URLs: `41/41` pass.

## Sitemap

- Builder automatic sitemap update: no.
- Manual narrow sitemap repair: yes.
- Missing URLs added before deployment: `24` (`5` entries plus `19` newly required tag URLs).
- URLs removed: `0`.

## Browser Availability

- The in-app browser runtime reported no available browser tabs (`browsers = []`).
- No unrelated browser backend was substituted.
- Required live HTTP and rendered HTML/DOM parsing checks completed successfully through the independent live validator.

## Manual Remainder

Submit URLs from `SEARCH_CONSOLE_SUBMISSION_PLAN_V56.md` to Search Console. No Search Console submission is claimed by this run.
