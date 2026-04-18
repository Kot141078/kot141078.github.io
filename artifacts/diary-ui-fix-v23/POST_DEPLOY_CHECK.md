# V23 Post-Deploy Check

Contract: `SITE_DIARY_UI_FIX_LATEST_POST_META_V23`
Date: `2026-04-18`
Deployment result: converged on first live check

## Live status

- `https://ivankotov.eu/` -> `200`
- `https://ivankotov.eu/diary/` -> `200`
- `https://ivankotov.eu/diary/archive/` -> `200`
- `https://ivankotov.eu/diary/tags/` -> `200`
- `https://ivankotov.eu/diary/a-home-robot-is-not-a-box-with-a-ribbon/` -> `200`
- `https://ivankotov.eu/diary/tags/ai-safety/` -> `200`
- `https://ivankotov.eu/diary-tags.json` -> `200`

## Live assertions

- home latest-post meta span count: `1`
- home latest-post meta equals only `2026-01-13`: `True`
- home latest-post headline remains correct: `True`
- home no longer contains the old extra text after the date: `True`
- `/diary/` first card meta span count: `1`
- `/diary/` first card meta equals only the date: `True`
- `/diary/archive/` first card meta span count: `1`
- `/diary/archive/` first card meta equals only the date: `True`
- representative tag page `/diary/tags/ai-safety/` first card meta span count: `1`
- representative tag page `/diary/tags/ai-safety/` first card meta equals only the date: `True`
- tag index page still renders correctly: `True`
- `a-home-robot-is-not-a-box-with-a-ribbon` title still renders correctly: `True`
- `a-home-robot-is-not-a-box-with-a-ribbon` canonical still renders correctly: `True`
- live tag pages checked from `diary-tags.json`: `74`
- live tag pages with bad meta blocks: `0`

## Deployment conclusion

- the visible meta line above latest-post and diary card headlines now shows only the date
- the headline remains the only title line
- no live regression was detected on the checked diary surfaces
