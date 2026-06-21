# V51 Post Deploy Check

Contract: `SITE_DIARY_IMPORT_BATCH_0167_0172_V51`

Amendment: `V51_BASELINE_DRIFT_AMENDMENT_169`

Implementation commit: `567ca831d0681cb9d1781a11882397459b59f086`

## Local Checks

- `python tools/build_diary.py`: pass.
- `git diff --check`: pass, with only Git CRLF working-copy warnings.
- JSON parse: `diary-index.json`, `diary-tags.json`, `diary-latest.json` pass.
- XML parse: `diary-feed.xml`, `sitemap.xml` pass.
- `diary-index.json`: count 175.
- `diary-latest.json`: latest `ccdp-v0-1-1-hygiene-addendum-published`.
- Home latest-post: `ccdp-v0-1-1-hygiene-addendum-published`.
- V51 batch latest: `relocating-an-office-is-always-a-good-moment-to-take-stock`.
- V23 date-only home latest meta: pass.
- V28 five-entry preview baseline: pass, 5 latest-entry cards.
- ENTRY 0167 image-less render: pass, 0 images and no placeholder text.
- ENTRY 0167 DOI, GitHub Release, and Website links: pass.
- ENTRY 0168 near-duplicate final sentence: preserved.
- Duplicate guard: clean.

## Remote Checks

Remote verification used cache-busting after pushing the implementation commit.

- New V51 entry URLs: 6 checked, 6 HTTP 200.
- New V51 asset URLs: 5 checked, 5 HTTP 200.
- Affected tag pages: 43 checked, 43 HTTP 200.
- `/diary/`: HTTP 200.
- `/diary/archive/`: HTTP 200.
- `/diary/tags/`: HTTP 200.
- `diary-index.json`: HTTP 200, count 175, latest `ccdp-v0-1-1-hygiene-addendum-published`.
- `diary-feed.xml`: HTTP 200.
- `sitemap.xml`: HTTP 200.
- `sitemap.xml`: includes all six new V51 entry URLs and all affected tag URLs.
- Home page: HTTP 200 and latest-post remains `ccdp-v0-1-1-hygiene-addendum-published`.
- ENTRY 0167 remote page: 0 images, no placeholder, DOI/GitHub/Website links rendered.
- ENTRY 0168 remote page: near-duplicate final sentence rendered as preserved source content.

## Sitemap

- Automatic sitemap update: no.
- Manual narrow repair: yes.
- Added 20 missing URLs: 6 new diary entry URLs and 14 missing affected tag URLs. Existing affected tag URLs already present were not duplicated.

## Manual Remainder

Submit URLs from `SEARCH_CONSOLE_SUBMISSION_PLAN_V51.md` to Search Console.
