# Diary Import Batch 0140-0143 V47 Report

Contract: `SITE_DIARY_IMPORT_BATCH_0140_0143_V47`

Repository: `C:\Users\kotov\Desktop\AGI\kot141078.github.io`

Branch: `main`

Scope: Diary import only.

=== DIARY IMPORT V47 PREFLIGHT START ===

- Repo exists: yes.
- Branch: `main`.
- Initial working tree: clean.
- Origin observed: `https://github.com/Kot141078/kot141078.github.io.git`.
- `.git` suffix accepted per contract; remote config was not changed.
- Baseline `diary-index.json` count: 141.
- Baseline latest entry: `2026-05-09` / `the-next-ai-risk-may-not-look-like-rebellion`.
- `DIARY_IMPORT_PROTOCOL.md`: present.
- `DIARY_IMPORT_CHECKLIST.md`: present.
- Current builder behavior inspected: entries sort by `(entry_date, slug)` descending.
- Same-date ordering requirement satisfied by existing builder order: `0141 > 0140` for effective date `2026-05-09`.
- Supplied images present/readable:
  - `C:\Users\kotov\Downloads\1778134048743.jpg` - 229397 bytes.
  - `C:\Users\kotov\Downloads\1778104648848.jpg` - 410929 bytes.
  - `C:\Users\kotov\Downloads\1778279307272.jpg` - 87385 bytes.
  - `C:\Users\kotov\Downloads\1778390354630.jpg` - 155725 bytes.

=== DIARY IMPORT V47 PREFLIGHT END ===

=== DIARY IMPORT V47 DUPLICATE GUARD START ===

- Checked `content/diary` and generated `diary/` outputs before writing.
- Checked all four LinkedIn URLs: no matches.
- Checked all four activity IDs: no matches.
- Checked likely resolved slugs: no matches.
- Checked near-title and near-body phrases: no matches in Diary.
- Non-diary site surfaces already contained the phrase `controlled non-collapse under uncertainty`; this was not a Diary duplicate and did not match any supplied LinkedIn URL/activity/slug.
- After import, each supplied LinkedIn URL appears exactly once in `content/diary`.
- Duplicate guard result: clean.

=== DIARY IMPORT V47 DUPLICATE GUARD END ===

=== DIARY IMPORT V47 SOURCE NORMALIZATION START ===

- 0140 raw date `09-04-2026` imported as effective date `2026-05-09`.
- 0141 raw date `09-05-2026` imported as effective date `2026-05-09`.
- 0142 raw date `10-05-2026` imported as effective date `2026-05-10`.
- 0143 source block had no explicit date line; imported as effective date `2026-05-11`.
- Same-date ordering on `2026-05-09`: `0141` appears before `0140`; the existing 0139 entry remains between them under the current `(date, slug)` descending builder behavior.
- Hashtag sets were preserved as supplied tag labels, with the LinkedIn UI prefix `hashtag#` removed for diary frontmatter labels.

=== DIARY IMPORT V47 SOURCE NORMALIZATION END ===

=== DIARY IMPORT V47 ASSET INGEST START ===

- 0140 image copied to `assets/diary/ai-is-not-a-toy-for-clever-podcast-lines/cover.jpg`.
- 0141 image copied to `assets/diary/one-of-the-most-damaging-habits-in-technical-culture-is-the-assumption-that-every-pause-means-failure/cover.jpg`.
- 0142 image copied to `assets/diary/most-public-conversations-about-quantum-computing-still-begin-with-fear/cover.jpg`.
- 0143 image copied to `assets/diary/ai-is-leaving-the-text-box/cover.jpg`.
- No placeholder images were created.

=== DIARY IMPORT V47 ASSET INGEST END ===

=== DIARY IMPORT V47 FILES WRITTEN START ===

- Added four `content/diary/*.md` source files.
- Added four `assets/diary/<slug>/cover.jpg` images.
- Generated four diary entry pages.
- Generated/updated Diary archive, tags, feed, JSON, Diary home, and site home latest-post.
- Performed narrow sitemap repair for the four new entry URLs and affected tag URLs.
- Implementation commit: `e3007ed120f8c8254ee3a0e41a35a75e384d924f`.

=== DIARY IMPORT V47 FILES WRITTEN END ===

=== DIARY IMPORT V47 BUILD START ===

- Build command: `python tools/build_diary.py`.
- Build result: exit code 0.
- Local `diary-index.json` count: 145.
- Local latest entry: `2026-05-11` / `ai-is-leaving-the-text-box`.
- Local top ordering:
  - `2026-05-11` / `ai-is-leaving-the-text-box`
  - `2026-05-10` / `most-public-conversations-about-quantum-computing-still-begin-with-fear`
  - `2026-05-09` / `the-next-ai-risk-may-not-look-like-rebellion`
  - `2026-05-09` / `one-of-the-most-damaging-habits-in-technical-culture-is-the-assumption-that-every-pause-means-failure`
  - `2026-05-09` / `ai-is-not-a-toy-for-clever-podcast-lines`
- Sitemap automatic update status: not automatic; narrow manual repair was required.
- Local sitemap missing count for expected V47 entry/tag URLs: 0.

=== DIARY IMPORT V47 BUILD END ===

=== DIARY IMPORT V47 VALIDATION START ===

- Remote entry pages: 4 checked, 4 returned HTTP 200.
- Remote asset URLs: 4 checked, 4 returned HTTP 200.
- Remote affected tag pages: 35 checked, 0 non-200.
- Remote Diary home: HTTP 200.
- Remote Diary archive: HTTP 200.
- Remote `diary-feed.xml`: HTTP 200.
- Remote `diary-index.json`: HTTP 200, count 145.
- Remote `sitemap.xml`: HTTP 200, missing expected V47 entry/tag URLs: 0.
- Remote site home: HTTP 200, latest-post points to `ai-is-leaving-the-text-box`.
- V23 date-only meta fix: intact on all four new entries.
- V28 five-entry preview fix: intact, latest section contains 5 entry cards.

=== DIARY IMPORT V47 VALIDATION END ===

=== DIARY IMPORT V47 SEARCH CONSOLE PLAN START ===

- Manual remainder: submit URLs from `SEARCH_CONSOLE_SUBMISSION_PLAN_V47.md` to Search Console.
- Priority: four new entry URLs first, then affected tag URLs, then sitemap resubmission.

=== DIARY IMPORT V47 SEARCH CONSOLE PLAN END ===

=== DIARY IMPORT V47 GIT START ===

- Implementation commit on `main`: `e3007ed120f8c8254ee3a0e41a35a75e384d924f`.
- Implementation commit pushed to `origin/main`.
- Report/artifact commit: created after this report file is committed.
- Final working tree target: clean after report/artifact commit.

=== DIARY IMPORT V47 GIT END ===
