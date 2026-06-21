# Post Deploy Check V52

Implementation commit validated: `a1ec3ce58f0383a9954225500788a9ad4cba8ade`

Public deployment observed at `https://ivankotov.eu/` after `origin/main` updated.

## HTTP Results

- New entry pages: `6/6` HTTP 200.
- New image assets: `5/5` HTTP 200.
- Affected tag pages: `37/37` HTTP 200.
- `/`: HTTP 200.
- `/diary/`: HTTP 200.
- `/diary/archive/`: HTTP 200.
- `/diary/tags/`: HTTP 200.
- `/diary-index.json`: HTTP 200.
- `/diary-feed.xml`: HTTP 200.
- `/sitemap.xml`: HTTP 200.

## State Checks

- Remote `diary-index.json` count: `181`.
- Remote latest slug: `there-is-a-pattern-that-many-people-do-not-want-to-look-at-directly`.
- Remote home latest-post: ENTRY 0178.
- Existing 2026-06-13 entry `ccdp-v0-1-1-hygiene-addendum-published` remained present.
- Remote top order:
  1. `2026-06-15` / `there-is-a-pattern-that-many-people-do-not-want-to-look-at-directly`
  2. `2026-06-14` / `a-system-can-speak-fluently-remember-fragments-imitate-continuity-survive-a-restart-or-even-sound-emotionally-consistent-and-still-not-have-enough-evidence-for-a-personality-formation-claim`
  3. `2026-06-13` / `ccdp-v0-1-1-hygiene-addendum-published`
  4. `2026-06-12` / `a-persistent-ai-system-does-not-fail-only-when-it-forgets`
  5. `2026-06-11` / `today-i-published-theoretical-core-of-project-ester-v0-1-as-a-doi-bound-working-paper`
  6. `2026-06-10` / `capability-can-be-installed`
  7. `2026-06-09` / `memory-is-becoming-the-next-ai-interface`

## Regression Checks

- V23 date-only meta fix: pass.
- V28 five-entry preview fix: pass, remote `/diary/` latest preview has `5` entry cards.
- ENTRY 0175 image-less without placeholder: pass.
- ENTRY 0173 required rendering and final cadence: pass.
- ENTRY 0174 shortened `lnkd.in` links preserved/clickable: pass.
- ENTRY 0175 Zenodo/GitHub links preserved/clickable: pass.
- ENTRY 0176 shortened DOI link preserved/clickable: pass.
- ENTRY 0177 DOI links preserved/clickable: pass.
- Duplicate import check on remote slugs: pass.
- Remote `sitemap.xml` includes all six V52 entry URLs and all affected tag URLs: pass.

## Sitemap

- Builder automatic sitemap update: no.
- Manual narrow sitemap repair: yes.
- Missing URLs added before deployment: `20`.

## Manual Remainder

Submit URLs from `SEARCH_CONSOLE_SUBMISSION_PLAN_V52.md` to Search Console.
