# Post Deploy Check V53

Implementation commit validated: `31593d90ed56a00f06aaa006f9e249c99efbe5ef`

Public deployment observed at `https://ivankotov.eu/` after `origin/main` updated.

## HTTP Results

- New entry pages: `4/4` HTTP 200.
- New image assets: `3/3` HTTP 200.
- Affected tag pages: `29/29` HTTP 200.
- `/`: HTTP 200.
- `/diary/`: HTTP 200.
- `/diary/archive/`: HTTP 200.
- `/diary/tags/`: HTTP 200.
- `/diary-index.json`: HTTP 200.
- `/diary-feed.xml`: HTTP 200.
- `/sitemap.xml`: HTTP 200.

## State Checks

- Remote `diary-index.json` count: `185`.
- Remote latest slug: `article-50-transparency-implementation-briefs-v0-1`.
- Remote home latest-post: ENTRY 0182.
- Existing ENTRY 0178 remained present.
- Remote top order:
  1. `2026-06-21` / `article-50-transparency-implementation-briefs-v0-1`
  2. `2026-06-18` / `when-tokens-start-costing-like-humans-ai-architecture-becomes-governance`
  3. `2026-06-17` / `a-small-boundary-question-kept-returning-to-the-project-ester-corpus`
  4. `2026-06-16` / `digital-beings-may-not-need-temples-they-may-need-law-and-that-law-may-become-their-religion`
  5. `2026-06-15` / `there-is-a-pattern-that-many-people-do-not-want-to-look-at-directly`

## Regression Checks

- V23 date-only meta fix: pass.
- V28 five-entry preview fix: pass, remote `/diary/` latest preview has `5` entry cards.
- ENTRY 0182 image-less without placeholder: pass.
- ENTRY 0180 publication links preserved/clickable: pass.
- ENTRY 0182 DOI/Derived/Website/GitHub links preserved/clickable: pass.
- Duplicate import check on remote slugs: pass.
- Remote `sitemap.xml` includes all four V53 entry URLs and all affected tag URLs: pass.

## Sitemap

- Builder automatic sitemap update: no.
- Manual narrow sitemap repair: yes.
- Missing URLs added before deployment: `15`.

## Manual Remainder

Submit URLs from `SEARCH_CONSOLE_SUBMISSION_PLAN_V53.md` to Search Console.
