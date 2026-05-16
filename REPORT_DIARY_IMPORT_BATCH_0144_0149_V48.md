# Diary Import Batch 0144-0149 V48 Report

Contract: `SITE_DIARY_IMPORT_BATCH_0144_0149_V48`

Amendment: `V48_DUPLICATE_VARIANT_AMENDMENT_FOR_ENTRY_0146`

Repository: `C:\Users\kotov\Desktop\AGI\kot141078.github.io`

Branch: `main`

Scope: Diary import only.

=== DIARY IMPORT V48 PREFLIGHT START ===

- Repo exists: yes.
- Branch: `main`.
- Initial working tree: clean.
- Origin observed: `https://github.com/Kot141078/kot141078.github.io.git`.
- `.git` suffix accepted per contract; remote config was not changed.
- `DIARY_IMPORT_PROTOCOL.md`: present.
- `DIARY_IMPORT_CHECKLIST.md`: present.
- Baseline `diary-index.json` count: 145.
- Baseline latest entry: `2026-05-11` / `ai-is-leaving-the-text-box`.
- V23 date-only meta baseline: intact before import.
- V28 five-entry preview baseline: intact before import.
- Supplied images present/readable:
  - `C:\Users\kotov\Downloads\1778528833988.jpg` - 233870 bytes.
  - `C:\Users\kotov\Downloads\1778627759975.jpg` - 150341 bytes.
  - `C:\Users\kotov\Downloads\1778714759127.jpg` - 301445 bytes.
  - `C:\Users\kotov\Downloads\1778802108087.jpg` - 109375 bytes.
  - `C:\Users\kotov\Downloads\1778826647715.jpg` - 192457 bytes.
- ENTRY 0144 intentionally image-less: confirmed.
- ENTRY 0147 has image and no supplied LinkedIn URL: confirmed.
- Current Diary protocol allows empty `linkedin_url`, so ENTRY 0147 was eligible for source-less import.

=== DIARY IMPORT V48 PREFLIGHT END ===

=== DIARY IMPORT V48 DUPLICATE GUARD START ===

- Scanned 145 existing `content/diary` Markdown entries before writing.
- Checked by LinkedIn URL where supplied, activity ID where supplied, resolved slug, near-title, near-body, and image hash reuse risk.
- ENTRY 0144: no duplicate found.
- ENTRY 0145: no duplicate found.
- ENTRY 0146: old same-title / near-body entry found and intentionally authorized by amendment only for this entry.
  - Existing file preserved unchanged: `content/diary/2026-04-22-a-serious-ai-future-should-not-make-human-experience-socially-disposable.md`.
  - Existing old activity: `7452385710872973312`.
  - New V48 activity: `7460222669670703104`.
  - Variant slug required and used: `a-serious-ai-future-should-not-make-human-experience-socially-disposable-0146`.
- ENTRY 0147: no title/body/date/image-similarity duplicate found.
- ENTRY 0148: no duplicate found.
- ENTRY 0149: no duplicate found.
- Image reuse guard: no existing asset hash matched the supplied V48 images.
- After import, supplied LinkedIn URLs for entries 0144, 0145, 0146, 0148, and 0149 each appear exactly once in `content/diary`.
- Duplicate guard result: clean under `V48_DUPLICATE_VARIANT_AMENDMENT_FOR_ENTRY_0146`.

=== DIARY IMPORT V48 DUPLICATE GUARD END ===

=== DIARY IMPORT V48 SOURCE NORMALIZATION START ===

- 0144 -> `2026-05-12` / `arq-cq-integration-addendum-v0-1-is-now-public`; image-less; LinkedIn URL preserved.
- 0145 -> `2026-05-13` / `the-central-question-is-no-longer-only-what-exactly-are-we-scaling`; image copied; LinkedIn URL preserved.
- 0146 -> `2026-05-14` / `a-serious-ai-future-should-not-make-human-experience-socially-disposable-0146`; image copied; LinkedIn URL preserved.
- ENTRY 0146 was imported as an intentional same-title / near-body LinkedIn variant under V48_DUPLICATE_VARIANT_AMENDMENT_FOR_ENTRY_0146. Existing 2026-04-22 entry was preserved unchanged. Variant slug used: a-serious-ai-future-should-not-make-human-experience-socially-disposable-0146.
- 0147 -> `2026-05-15` / `grief-is-not-a-user-error`; image copied; `linkedin_url` present but empty.
- 0148 -> `2026-05-15` / `what-should-a-child-facing-ai-be-allowed-to-remember`; image copied; LinkedIn URL preserved.
- 0149 -> `2026-05-16` / `i-was-an-only-child`; image copied; LinkedIn URL preserved.
- Same-date ordering for `2026-05-15`: `0148` > `0147`, achieved by deterministic slug ordering under the existing `(entry_date, slug)` descending builder sort.
- 0148 and 0149 Zenodo/GitHub links were written as Markdown links so the generated HTML renders clickable anchors.

=== DIARY IMPORT V48 SOURCE NORMALIZATION END ===

=== DIARY IMPORT V48 ASSET INGEST START ===

- 0144: no image, no placeholder, no asset directory created for the entry.
- 0145 image copied to `assets/diary/the-central-question-is-no-longer-only-what-exactly-are-we-scaling/cover.jpg`.
- 0146 image copied to `assets/diary/a-serious-ai-future-should-not-make-human-experience-socially-disposable-0146/cover.jpg`.
- 0147 image copied to `assets/diary/grief-is-not-a-user-error/cover.jpg`.
- 0148 image copied to `assets/diary/what-should-a-child-facing-ai-be-allowed-to-remember/cover.jpg`.
- 0149 image copied to `assets/diary/i-was-an-only-child/cover.jpg`.

=== DIARY IMPORT V48 ASSET INGEST END ===

=== DIARY IMPORT V48 FILES WRITTEN START ===

- Added six `content/diary/*.md` source entries.
- Added five `assets/diary/<slug>/cover.jpg` images.
- Generated six diary entry pages.
- Generated/updated Diary archive, tags, feed, JSON surfaces, Diary home, and site home latest-post.
- Performed narrow sitemap repair for missing V48 entry URLs and affected tag URLs.
- Implementation commit: `e76d24390542cb49a17332e5e42a3525eaf73450`.

=== DIARY IMPORT V48 FILES WRITTEN END ===

=== DIARY IMPORT V48 BUILD START ===

- Build command: `python tools/build_diary.py`.
- Build result: exit code 0.
- Local `diary-index.json` count: 151.
- Local latest entry: `2026-05-16` / `i-was-an-only-child`.
- Local top ordering:
  - `2026-05-16` / `i-was-an-only-child`
  - `2026-05-15` / `what-should-a-child-facing-ai-be-allowed-to-remember`
  - `2026-05-15` / `grief-is-not-a-user-error`
  - `2026-05-14` / `a-serious-ai-future-should-not-make-human-experience-socially-disposable-0146`
  - `2026-05-13` / `the-central-question-is-no-longer-only-what-exactly-are-we-scaling`
  - `2026-05-12` / `arq-cq-integration-addendum-v0-1-is-now-public`
- Sitemap automatic update status: not automatic; narrow manual repair was required.
- Local sitemap missing count for expected V48 entry/tag URLs after repair: 0.

=== DIARY IMPORT V48 BUILD END ===

=== DIARY IMPORT V48 VALIDATION START ===

- Local validation passed before commit.
- Remote deployment initially served stale `diary-index.json` count 145, then refreshed to count 151 on the second poll.
- Remote entry pages: 6 checked, 6 returned HTTP 200.
- Remote asset URLs: 5 checked, 5 returned HTTP 200.
- Remote affected tag pages: 56 checked, 0 non-200.
- Remote Diary home: HTTP 200.
- Remote site home: HTTP 200 and latest-post points to `i-was-an-only-child`.
- Remote `diary-index.json`: HTTP 200, count 151, latest `i-was-an-only-child`.
- Remote `diary-feed.xml`: HTTP 200.
- Remote `sitemap.xml`: HTTP 200, missing expected V48 entry/tag URLs: 0.
- V23 date-only meta fix: intact on all six new entries.
- V28 five-entry preview fix: intact, latest section contains 5 entry cards.
- ENTRY 0144 renders image-less without placeholder.
- ENTRY 0147 renders without LinkedIn origin trace and keeps empty source URL metadata.
- ENTRY 0148 links render correctly.
- ENTRY 0149 links render correctly.
- Duplicate guard confirms no exact duplicate import occurred; ENTRY 0146 is the explicitly authorized same-title / near-body variant.

=== DIARY IMPORT V48 VALIDATION END ===

=== DIARY IMPORT V48 SEARCH CONSOLE PLAN START ===

- Manual remainder: submit URLs from `SEARCH_CONSOLE_SUBMISSION_PLAN_V48.md` to Search Console.
- Priority: six new entry URLs first, then affected tag URLs, then sitemap resubmission.

=== DIARY IMPORT V48 SEARCH CONSOLE PLAN END ===

=== DIARY IMPORT V48 GIT START ===

- Implementation commit on `main`: `e76d24390542cb49a17332e5e42a3525eaf73450`.
- Implementation commit pushed to `origin/main`.
- Report/artifact commit: created after this report file is committed; exact hash is reported in final status.
- Final working tree target: clean after report/artifact commit.

=== DIARY IMPORT V48 GIT END ===

## Final Summary

- Origin observed: `https://github.com/Kot141078/kot141078.github.io.git` with `.git` suffix.
- Final diary-index count: 151.
- Home latest-post: `i-was-an-only-child` / ENTRY 0149.
- Same-date ordering for `2026-05-15`: ENTRY 0148 (`what-should-a-child-facing-ai-be-allowed-to-remember`) before ENTRY 0147 (`grief-is-not-a-user-error`).
- ENTRY 0147 missing-source-URL handling: imported with empty `linkedin_url`; no fake URL created.
- Sitemap handling: manual narrow repair required and completed.
- Remote checks: entries 200, assets 200, affected tags 200, JSON/feed/sitemap/home 200.
- Duplicate guard: clean under the explicit 0146 variant amendment.
- Implementation commit: `e76d24390542cb49a17332e5e42a3525eaf73450`.
- Manual remainder: send URLs from `SEARCH_CONSOLE_SUBMISSION_PLAN_V48.md` to Search Console.
