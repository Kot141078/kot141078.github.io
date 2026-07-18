# Diary Import Batch 0188-0192 V55 Report

Contract: `SITE_DIARY_IMPORT_BATCH_0188_0192_V55`

Source packet: `C:\Users\kotov\Downloads\ITERATION2.txt`

Source packet SHA-256: `7672ecaa9d64ce598fcc0271cc134dc1cbeb91cb3aef4f0f53163e65c25c54f9`

Implementation commit: `aa1f5bb973e65c61c6267a99981286229eb9c0a9`

Report/artifact commit: emitted in the final terminal output after this file is committed.

## Summary

- Imported exactly ENTRY 0188 through ENTRY 0192 as real diary entries.
- The posts dated `2026-07-06` and `2026-07-07` were not imported in V55.
- Final local and remote `diary-index.json` count: `195`.
- Global home latest-post became ENTRY 0192: `entity-vs-profile-a-witness-root-custody-criterion-for-persistent-digital-entities-v0-1-1`.
- Existing entries were not removed, overwritten, reordered, or modified as source records.
- Existing ENTRY 0187 remained immediately below the five new entries.
- Origin was observed with `.git` suffix: `https://github.com/Kot141078/kot141078.github.io.git`.
- Sitemap automatic update: no.
- Manual narrow sitemap repair: yes; exactly `15` missing URLs were added (`5` entries and `10` newly required tag pages), with `0` removals.
- Duplicate guard: pass. No exact LinkedIn URL, activity ID, resolved slug, body, body opening, or image reuse blocker was found.
- ENTRY 0189 and ENTRY 0190 are intentionally image-less and render without placeholders.
- GitHub Pages deployment run `29656834303` completed successfully for the implementation commit.

## Required Marker Report

=== DIARY IMPORT V55 PREFLIGHT START ===

- Repository exists: pass.
- Branch: `main`.
- Working tree before import: clean.
- HEAD before import: `7e1def310ea5bf03e5d968754b148071df7fb303`.
- `origin/main` after fetch: `7e1def310ea5bf03e5d968754b148071df7fb303`.
- Fast-forward pull required: no; local HEAD already equaled `origin/main`.
- No active merge, rebase, cherry-pick, revert, or bisect marker: pass.
- Origin observed with `.git` suffix: `https://github.com/Kot141078/kot141078.github.io.git`.
- Remote configuration was not changed.
- `DIARY_IMPORT_PROTOCOL.md`: present and read in full.
- `DIARY_IMPORT_CHECKLIST.md`: present and read in full.
- Expected pre-import count: `190`.
- Observed pre-import count: `190`.
- Expected pre-import latest/home post: `a-small-external-comment-turned-into-a-useful-control-layer-correction` dated `2026-06-30`.
- Observed pre-import latest/home post: exact match.
- V23 date-only home/latest meta baseline: pass.
- V28 five-entry preview baseline: pass.
- ENTRY 0188 image: readable JPEG, `1536x1024`, `204199` bytes.
- ENTRY 0191 image: readable JPEG, `1122x1402`, `161302` bytes.
- ENTRY 0192 image: readable JPEG, `1122x1402`, `158662` bytes.
- All three images were visually inspected before factual alt text was written.
- ENTRY 0189 and ENTRY 0190 were confirmed intentionally image-less.

=== DIARY IMPORT V55 PREFLIGHT END ===

=== DIARY IMPORT V55 DUPLICATE GUARD START ===

- Existing diary source records searched: `190`.
- ENTRY 0188: no exact LinkedIn URL, activity ID, resolved slug, body, body-opening, image path, or image-hash collision. The nearest title was thematic only and not an exact duplicate.
- ENTRY 0189: no exact LinkedIn URL, activity ID, resolved slug, body, or body-opening collision. Existing VARFLOOR Package A DOI and publication-page references were expected non-blocking publication overlap.
- ENTRY 0190: no exact LinkedIn URL, activity ID, resolved slug, body, or body-opening collision. Existing VARFLOOR Package B DOI and publication-page references were expected non-blocking publication overlap.
- ENTRY 0191: no exact LinkedIn URL, activity ID, resolved slug, body, body-opening, image path, or image-hash collision. Existing `/install-c/` references were expected non-blocking page overlap.
- ENTRY 0192: no exact LinkedIn URL, activity ID, resolved slug, body, body-opening, image path, or image-hash collision. Existing reader-page, DOI, and GitHub metadata references were expected non-blocking publication overlap.
- No diary entry dated `2026-07-06` or `2026-07-07` existed before import.
- Exact duplicate blocker: false.

=== DIARY IMPORT V55 DUPLICATE GUARD END ===

=== DIARY IMPORT V55 SOURCE NORMALIZATION START ===

- Exactly five source records were selected: ENTRY 0188-0192.
- ENTRY 0188 title/slug: `I think we are misnaming what is happening in AI.` / `i-think-we-are-misnaming-what-is-happening-in-ai`.
- ENTRY 0189 title/slug: `VARFLOOR Package A v0.1` / `varfloor-package-a-v0-1`.
- ENTRY 0190 title/slug: `VARFLOOR Package B v0.1` / `varfloor-package-b-v0-1`.
- ENTRY 0191 title/slug: `How to install c` / `how-to-install-c`.
- ENTRY 0192 title/slug: `Entity vs. Profile: A Witness-Root Custody Criterion for Persistent Digital Entities v0.1.1` / `entity-vs-profile-a-witness-root-custody-criterion-for-persistent-digital-entities-v0-1-1`.
- Dates were normalized exactly to `2026-07-01` through `2026-07-05`.
- Source hashtags became front matter tags; supplied spellings were preserved.
- LinkedIn URLs were preserved exactly.
- DOI, publication, install-c, reader, Zenodo, and GitHub URLs were rendered as clickable Markdown links.
- ENTRY 0192 preserves separate Version DOI and Zenodo link surfaces, even though both point to the same DOI URL.
- All five normalized Markdown bodies were compared to their source bodies and passed whitespace/link-markup-equivalent comparison.
- ENTRY 0189 and ENTRY 0190 have empty `primary_image` and `image_alt`; no fake image or placeholder was introduced.
- The `2026-07-06` and `2026-07-07` posts were excluded.
- No source file under `Downloads` was modified.

=== DIARY IMPORT V55 SOURCE NORMALIZATION END ===

=== DIARY IMPORT V55 ASSET INGEST START ===

- ENTRY 0188: `assets/diary/i-think-we-are-misnaming-what-is-happening-in-ai/cover.jpg`, `204199` bytes, SHA-256 `49aaddc971d3c3b5b41804bc9f342bd5a06674cd69be0acca4892f6897085717`.
- ENTRY 0189: no image, no placeholder.
- ENTRY 0190: no image, no placeholder.
- ENTRY 0191: `assets/diary/how-to-install-c/cover.jpg`, `161302` bytes, SHA-256 `6283165b7874df16ad4a04fa8469951d170793a891c157cf17d87261929c35b6`.
- ENTRY 0192: `assets/diary/entity-vs-profile-a-witness-root-custody-criterion-for-persistent-digital-entities-v0-1-1/cover.jpg`, `158662` bytes, SHA-256 `93b2fdf1a8cefb73963f9e1832cbdaa2fc7fb7a36099c8bf9bf9cea77b5e962b`.
- Source and destination hashes matched for all three copies.
- Live asset bytes reproduced all three expected SHA-256 values.

=== DIARY IMPORT V55 ASSET INGEST END ===

=== DIARY IMPORT V55 FILES WRITTEN START ===

- Created five `content/diary/*.md` source files.
- Created three `assets/diary/<slug>/cover.jpg` image files.
- Generated five public diary entry pages.
- Updated `/`, `/diary/`, `/diary/archive/`, `/diary/tags/`, affected tag surfaces, `diary-index.json`, `diary-tags.json`, `diary-latest.json`, `diary-feed.xml`, and `diary-tag-map.json` through the canonical builder.
- Updated `sitemap.xml` through a narrow manual repair.
- Implementation commit write surface: `70` paths.
- Generated HTML paths parsed locally: `56`.
- No V55 report/artifact file was mixed into the implementation commit.

=== DIARY IMPORT V55 FILES WRITTEN END ===

=== DIARY IMPORT V55 BUILD START ===

- Canonical builder: `tools/build_diary.py`.
- Implementation build command: `python -B tools/build_diary.py`; result: pass.
- Contract-form command `python tools/build_diary.py` was also run after deployment; exit code: `0`.
- The repeat build changed only the runtime `lastBuildDate` and unordered alias-list ordering in three generated files. Those diagnostic repeat-build changes were inspected and restored to the already signed/deployed implementation output before report work.
- `git diff --check`: pass before and after staging.
- Strict JSON parsing: pass.
- XML parsing with entity/network access disabled: pass.
- Generated HTML parsing: pass.
- Local internal links checked: `10057`; broken links: `0`.
- Builder automatic sitemap update: no.
- Narrow sitemap repair: `15` additions, `0` removals.

=== DIARY IMPORT V55 BUILD END ===

=== DIARY IMPORT V55 VALIDATION START ===

- Local `diary-index.json` count: `195`.
- Remote `diary-index.json` count: `195`.
- Local and remote latest slug: `entity-vs-profile-a-witness-root-custody-criterion-for-persistent-digital-entities-v0-1-1`.
- Top chronological order after import:
  1. 2026-07-05 / `entity-vs-profile-a-witness-root-custody-criterion-for-persistent-digital-entities-v0-1-1`
  2. 2026-07-04 / `how-to-install-c`
  3. 2026-07-03 / `varfloor-package-b-v0-1`
  4. 2026-07-02 / `varfloor-package-a-v0-1`
  5. 2026-07-01 / `i-think-we-are-misnaming-what-is-happening-in-ai`
  6. 2026-06-30 / `a-small-external-comment-turned-into-a-useful-control-layer-correction`
- Existing ENTRY 0187 remained immediately below the V55 batch: pass.
- Global home latest-post became ENTRY 0192: pass.
- ENTRY 0189 and ENTRY 0190 image-less rendering without placeholders: pass.
- ENTRY 0188 renders the misnaming/bubble/infrastructure-of-continuity post: pass.
- ENTRY 0189 DOI and publication links: clickable.
- ENTRY 0190 DOI and publication links: clickable.
- ENTRY 0191 install-c link: clickable.
- ENTRY 0192 reader page, Version DOI, Zenodo, and GitHub links: clickable.
- Total supplied clickable source-link surfaces: `9`.
- V23 date-only meta fix remains intact: pass.
- V28 five-entry preview fix remains intact: pass; remote `/diary/` latest preview has `5` cards.
- Five new entry URLs: `5/5` HTTP 200.
- Three new asset URLs: `3/3` HTTP 200 and hash-verified.
- Affected tag pages: `34/34` HTTP 200.
- Core surfaces: `9/9` HTTP 200.
- Remote HTML parse: `43/43` selected pages pass.
- Remote strict JSON parse: `3/3` selected machine files pass.
- Remote XML parse: `2/2` selected machine files pass.
- Remote `sitemap.xml` contains all five V55 entry URLs and all 34 affected tag URLs: `39/39` pass.
- No index item dated `2026-07-06` or `2026-07-07` exists: pass.
- Each V55 slug occurs exactly once in the remote index: pass.
- Duplicate guard confirms no duplicate import occurred: pass.
- GitHub Pages run `29656834303`: success for `aa1f5bb973e65c61c6267a99981286229eb9c0a9`.
- In-app browser tab was unavailable; no unrelated browser backend was substituted. Required live HTTP and rendered HTML/DOM validation completed successfully.

=== DIARY IMPORT V55 VALIDATION END ===

=== DIARY IMPORT V55 SEARCH CONSOLE PLAN START ===

- Manual remainder: submit URLs from `SEARCH_CONSOLE_SUBMISSION_PLAN_V55.md` to Search Console.
- Submit the five new entry URLs first, the 34 affected tag URLs second, and the sitemap last.
- No Search Console submission is claimed by this automated run.

=== DIARY IMPORT V55 SEARCH CONSOLE PLAN END ===

=== DIARY IMPORT V55 GIT START ===

- Implementation commit: `aa1f5bb973e65c61c6267a99981286229eb9c0a9`.
- Implementation commit GPG signature: good.
- Implementation commit pushed fast-forward to `origin/main`: yes.
- Pages deployment for the implementation commit: success.
- Report/artifact commit: emitted in final terminal output after this file is committed.
- Expected final branch: `main`.
- Expected final worktree: clean after report/artifact commit and fast-forward push.

=== DIARY IMPORT V55 GIT END ===

## New Entry URLs

- https://ivankotov.eu/diary/i-think-we-are-misnaming-what-is-happening-in-ai/
- https://ivankotov.eu/diary/varfloor-package-a-v0-1/
- https://ivankotov.eu/diary/varfloor-package-b-v0-1/
- https://ivankotov.eu/diary/how-to-install-c/
- https://ivankotov.eu/diary/entity-vs-profile-a-witness-root-custody-criterion-for-persistent-digital-entities-v0-1-1/

## Manual Remainder

Submit the URLs listed in `SEARCH_CONSOLE_SUBMISSION_PLAN_V55.md` to Search Console.
