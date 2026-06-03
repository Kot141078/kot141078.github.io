# V50 Post Deploy Check

Contract: `SITE_DIARY_IMPORT_BATCH_0158_0166_V50`

Implementation commit: `7237e20b883bb0a015b6c5e4ba80185a1b7c6e87`

## Local Checks

- `python tools/build_diary.py`: pass.
- `git diff --check`: pass after generated whitespace cleanup.
- `diary-index.json`: count 168.
- `diary-latest.json`: latest `powerful-hardware-needs-powerful-tasks`.
- `diary-feed.xml`: XML parse pass.
- `sitemap.xml`: XML parse pass.
- V23 date-only home latest meta: pass.
- V28 five-entry preview baseline: pass.
- V50 LinkedIn links: 9 checked, 9 rendered.
- Duplicate guard: clean.
- Secret/local-path marker scan: pass.

## Remote Checks

Remote verification used cache-busting. First public check was stale, second attempt observed V50.

- New entry URLs: 9 checked, 9 HTTP 200.
- New asset URLs: 9 checked, 9 HTTP 200.
- Affected tag pages: 55 checked, 55 HTTP 200.
- `/diary/`: HTTP 200.
- `/diary/archive/`: HTTP 200.
- `/diary/tags/`: HTTP 200.
- `diary-index.json`: HTTP 200, count 168, latest `powerful-hardware-needs-powerful-tasks`.
- `diary-feed.xml`: HTTP 200 and XML parse pass.
- `sitemap.xml`: HTTP 200 and XML parse pass.
- `sitemap.xml`: includes all new entry URLs and affected tag URLs.
- Home page: HTTP 200 and latest-post points to `powerful-hardware-needs-powerful-tasks`.

## Sitemap

- Automatic sitemap update: no.
- Manual narrow repair: yes.
- Added 31 missing URLs: 9 new diary entry URLs and 22 missing affected tag URLs. Existing affected tag URLs already present were not duplicated.

## Manual Remainder

Submit URLs from `SEARCH_CONSOLE_SUBMISSION_PLAN_V50.md` to Search Console.
