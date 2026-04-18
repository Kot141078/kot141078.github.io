# V23 Root Cause and Fix

Contract: `SITE_DIARY_UI_FIX_LATEST_POST_META_V23`
Date: `2026-04-18`

## Root cause

The redundant text was emitted by renderer code, not by diary content.

### Shared diary cards

In [tools/build_diary.py](/C:/Users/kotov/Desktop/AGI/kot141078.github.io/tools/build_diary.py), `render_entry_card()` used:

- `entry.date_iso`
- `entry.slug`

inside the same `.entry-meta` block above `<h3>`.

Exact pre-fix lines:

- line `446`: `<span>{entry.date_iso}</span>`
- line `447`: `<span>{html.escape(entry.slug)}</span>`

Effect:

- `/diary/` cards showed `date + slug`
- `/diary/archive/` cards showed `date + slug`
- per-tag diary pages showed `date + slug`

### Home latest-post slot

In the same file, `render_home_slot_from_state()` used:

- `date`
- `tags_text`
- total entry count

inside the `.entry-meta` block above the latest-post headline.

Exact pre-fix lines:

- line `1076`: `<span>{date}</span>`
- line `1077`: `<span>{tags_text}</span>`
- line `1078`: `<span>{count} entries total</span>`

Effect:

- the home latest-post line rendered date plus extra metadata instead of date only

## Fix

Applied the narrowest renderer-only fix:

- removed the slug span from `render_entry_card()`
- removed tags/count spans from `render_home_slot_from_state()`
- simplified the home-slot helper signature by removing the unused `count` argument

## Scope decision

- shared fix: `render_entry_card()` because the same bad meta pattern appeared across multiple diary card surfaces
- local fix: `render_home_slot_from_state()` because the home latest-post slot had its own dedicated meta renderer
- no fix was applied to entry content files because the bug was not in markdown/front matter
- no fix was applied to entry-page hero meta because that is a separate renderer and not the card/latest-post line targeted by the contract

## Result

After rebuild:

- the small meta line above latest-post and diary card headlines contains only the date
- the main headline remains the only visible title line
- no slug-like duplicate remains above diary card headlines
