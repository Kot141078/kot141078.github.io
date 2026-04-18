# Report - Diary UI Fix Latest Post Meta V23

Date: 2026-04-18
Contract ID: `SITE_DIARY_UI_FIX_LATEST_POST_META_V23`
Mode: `CODEX EXECUTION CONTRACT`

## Preflight

Confirmed before any write:

- repo exists and is a git repository
- current branch was `main`
- `origin` resolved to `https://github.com/Kot141078/kot141078.github.io.git`
- note on remote comparison: the returned origin includes the optional `.git` suffix while pointing to the same GitHub repository identity named in the contract
- working tree was clean
- root cause source file was identified as [tools/build_diary.py](/C:/Users/kotov/Desktop/AGI/kot141078.github.io/tools/build_diary.py)
- the redundant text does not come from entry content, front matter, or JSON state payloads
- the broken meta appears in two render paths:
  - shared diary card renderer used by `/diary/`, `/diary/archive/`, and per-tag diary pages
  - dedicated home latest-post renderer used by `/`
- entry markdown/front matter did not need changes

## Root Cause

The redundant text came from template logic, not from content.

Exact source:

- `render_entry_card()` in [tools/build_diary.py](/C:/Users/kotov/Desktop/AGI/kot141078.github.io/tools/build_diary.py) rendered:
  - `<span>{entry.date_iso}</span>`
  - `<span>{entry.slug}</span>`
- that made shared diary cards render a small line equivalent to `date + slug` above the real headline
- `render_home_slot_from_state()` in the same file rendered:
  - `<span>{date}</span>`
  - `<span>{tags_text}</span>`
  - `<span>{count} entries total</span>`
- that made the home latest-post meta line render date plus extra text instead of date only

This was therefore a shared template/render bug with one additional dedicated home-slot variant, not a data problem.

## Fix

Implemented the narrowest correct fix in [tools/build_diary.py](/C:/Users/kotov/Desktop/AGI/kot141078.github.io/tools/build_diary.py):

- removed the `entry.slug` span from `render_entry_card()`
- simplified `render_home_slot_from_state()` so the meta line renders only the date
- removed the now-unneeded `count` argument from `render_home_slot_from_state()`

No content entries, slugs, titles, dates, tags, or diary data payloads were changed.

## Build and Regeneration

Commands and tasks run:

- `python tools/build_diary.py`
- rebuilt committed public outputs affected by the renderer:
  - `/`
  - `/diary/`
  - `/diary/archive/`
  - per-tag diary entry pages under `/diary/tags/*/`
- `diary-feed.xml` was regenerated transiently by the builder, but its only difference was `lastBuildDate`; that timestamp-only noise was intentionally not carried into the final patch

## Validation Outcomes

Local validation passed:

- home latest-post meta line renders only the date
- home latest-post headline remains `Why Superintelligence Is Not What Sci-Fi Promised`
- `/diary/` entry cards render only the date above each title
- `/diary/archive/` entry cards render only the date above each title
- per-tag diary entry cards render only the date above each title
- `a-home-robot-is-not-a-box-with-a-ribbon` still renders correctly on its entry page
- canonical for `a-home-robot-is-not-a-box-with-a-ribbon` is intact
- `content/diary/` had no changes
- mechanical scan checked `77` local surfaces with entry-card meta blocks and found `0` blocks with more than one `<span>`

Live validation passed after push:

- `https://ivankotov.eu/` -> `200`
- `https://ivankotov.eu/diary/` -> `200`
- `https://ivankotov.eu/diary/archive/` -> `200`
- `https://ivankotov.eu/diary/tags/` -> `200`
- `https://ivankotov.eu/diary/a-home-robot-is-not-a-box-with-a-ribbon/` -> `200`
- representative tag page `https://ivankotov.eu/diary/tags/ai-safety/` -> `200`
- `https://ivankotov.eu/diary-tags.json` -> `200`
- live home latest-post meta line now has exactly one span containing only `2026-01-13`
- live home no longer contains the old extra text after the date
- live `/diary/`, `/diary/archive/`, and representative tag page cards all render only the date above the headline
- live tag index remained healthy
- all `74` live tag pages listed in `diary-tags.json` were checked and `0` had bad meta blocks

## Affected Files

Implementation touched:

- [tools/build_diary.py](/C:/Users/kotov/Desktop/AGI/kot141078.github.io/tools/build_diary.py)
- [index.html](/C:/Users/kotov/Desktop/AGI/kot141078.github.io/index.html)
- [diary/index.html](/C:/Users/kotov/Desktop/AGI/kot141078.github.io/diary/index.html)
- [diary/archive/index.html](/C:/Users/kotov/Desktop/AGI/kot141078.github.io/diary/archive/index.html)
- multiple generated per-tag pages under [diary/tags](/C:/Users/kotov/Desktop/AGI/kot141078.github.io/diary/tags)

Unaffected by design:

- `content/diary/*.md`
- slugs
- dates
- titles
- tag logic
- entry-page content markup

## Commit Hashes

- implementation commit: `235946277f1d330217abb3b1c61fc3283fb31047`
- report artifact commit: recorded in the final console git block because this report file is part of that commit

## Final Clean-Tree Confirmation

- the working tree was clean before V23 started
- the implementation working tree was clean before report artifacts were written
- final post-report clean-tree confirmation is recorded in the final console git block after the report artifact commit
