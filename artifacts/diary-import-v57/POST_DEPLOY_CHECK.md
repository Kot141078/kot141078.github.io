# Post Deploy Check V57

Implementation commit validated: `1cfed97feebbae1647c0c87a2082aa2b4c1b04ab`

Public deployment observed at `https://ivankotov.eu/` after `origin/main` updated.

GitHub Pages run: `29660674194` (`https://github.com/Kot141078/kot141078.github.io/actions/runs/29660674194`), conclusion `success`.

## HTTP Results

- New entry pages: `6/6` HTTP 200.
- New image assets: `6/6` HTTP 200.
- Affected tag pages: `43/43` HTTP 200.
- Core surfaces returned HTTP 200:
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

- Selected live HTML pages: `53` parsed.
- Live JSON: selected diary machine files parsed.
- Live XML: `2/2` parsed (`diary-feed.xml` and `sitemap.xml`).

## State Checks

- Remote `diary-index.json` count: `206`.
- Remote latest slug: `the-question-behind-c-a-b-is-not-whether-an-ai-can-look-consistent-over-time`.
- Remote home latest-post: ENTRY 0203, dated `2026-07-18`.
- Remote top order:
  1. `2026-07-18` / `the-question-behind-c-a-b-is-not-whether-an-ai-can-look-consistent-over-time`
  2. `2026-07-16` / `ownership-ends-where-the-screwdriver-is-forbidden`
  3. `2026-07-15` / `suspension-preserves-continuity-it-does-not-create-maturity`
  4. `2026-07-14` / `ai-does-not-die-when-it-is-switched-off`
  5. `2026-07-13` / `silicon-valley-2026`
  6. `2026-07-12` / `the-future-of-work-has-a-body-temperature`
  7. `2026-07-11` / `saturday-thought`
- No `2026-07-17` entry was present.

## Regression and Content Checks

- V23 date-only meta fix: pass.
- V28 five-entry preview fix: pass; remote `/diary/` latest preview has `5` entry cards.
- All six V57 entries are image-bearing: pass.
- ENTRY 0203 Read, Canonical archive, and Source links: `3/3` clickable on the live page.
- Duplicate import check: each V57 slug occurs exactly once in the remote index, and no V57 LinkedIn URL or activity ID duplicate was found.
- No selected live page showed a local `C:\Users\...` path.
- Remote `sitemap.xml` includes all six V57 entry URLs and all 43 affected tag URLs: `49/49` pass.

## Sitemap

- Builder automatic sitemap status: partial.
- Expected V57 URLs: `49`.
- Automatically present before repair: `26`.
- Missing URLs added before deployment: `23`.
- URLs removed: `0`.

## Manual Remainder

Send URLs from `SEARCH_CONSOLE_SUBMISSION_PLAN_V57.md` to Google Search Console. No Google Search Console submission is claimed by this run.
