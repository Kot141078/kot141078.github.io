# Diary Landing Correction V59 Report

Contract: `DIARY_LANDING_PRINT_AND_CANONICAL_TOKEN_CORRECTION_V59`

Live target: <https://ivankotov.eu/diary/>

## Baseline

- Baseline commit: `3cdebae90f166b568266b891db53204abed4ca0f`
- Diary count: 206
- Latest date: `2026-07-18`
- Latest slug: `the-question-behind-c-a-b-is-not-whether-an-ai-can-look-consistent-over-time`
- V58 information architecture preserved: Hero -> Latest -> Browse/search -> Start here -> Themes -> Cornerstones -> Tags
- Latest cards: 5
- Source entry changes: 0
- Entry asset changes: 0
- Sitemap URLs added: 0
- Sitemap URLs removed: 0

## Source-of-truth files

- `tools/build_diary.py`: canonical display-token formatting, landing card rendering, latest image loading policy
- `styles.css`: landing image frame rules, responsive image caps, print layout, hero print compaction, Browse/search print behavior
- `diary/index.html`: generated output rebuilt by `python tools/build_diary.py`

No generated HTML was patched as the sole fix.

## Changed files

Implementation commit `1465eb26da376de5127b2d48542ba600cd3f0447` changed:

- `tools/build_diary.py`
- `styles.css`
- `diary/index.html`

The report/artifact commit is emitted in the final terminal output.

## Protected-token implementation

V59 adds `PROTECTED_DISPLAY_TOKENS` before generic CamelCase / letter-digit splitting. Protected tokens are matched as complete display tokens only; the implementation does not blindly replace substrings inside unrelated words.

Exact protected-token checks passed for:

- `L4`, `A6`, `D4`, `ARQ`, `SER`, `CCDP`, `AMDR`, `PAMDC`, `CGAM`, `VXCX`, `WDC`, `BCEC`, `SRLM`, `AI`, `LLM`, `EU`, `WBGT`, `CPAP`, `PF`, `EA`, `LA`

`AGI` remains governed by the V58 alias family and displays as `Advanced Global Intelligence`, preserving the required V58 alias collapse while avoiding `A G I`.

## Exact L4 fix

- Before: visible landing chips rendered `L 4`
- After: visible landing chips render `L4`
- Top tag surface: `L4 (127)`
- Incorrect protected-token displays remaining: 0

## Generic token-splitting regression checks

Generated and live landing content were checked for:

- `L 4`: 0
- `A 6`: 0
- `D 4`: 0
- `A G I`: 0
- `L L M`: 0

V58 alias behavior remains intact:

- No separate visible top-tag chips for `AI Safety` and `AISafety`
- No separate visible top-tag chips for `AI Architecture` and `AIArchitecture`

## Featured-image cause

The V58 CSS capped image height but not every image wrapper height consistently. In print, this could leave the wrapper taller than the image and create internal blank image-frame space. A separate print/PDF issue also appeared because lazy latest images below the first print viewport could remain unloaded during PDF capture.

## Featured-image fix

V59 sets the landing image wrapper and image to coordinated dimensions:

- Wrapper has aspect ratio and max height
- Image uses `display: block`
- Image uses `width: 100%`
- Image uses `height: 100%`
- Image uses `object-fit: cover`
- Image uses `object-position: center top`
- Wrapper uses `overflow: hidden`
- Latest five images are loaded eagerly so print/PDF capture does not emit blank lazy placeholders

Measured remote result:

- Featured print wrapper height: 160px
- Featured print image height: 158px
- Featured object-fit: `cover`
- Featured object-position: `50% 0%`
- Internal blank image-space verdict: PASS

## Hero print cause

V58 print CSS applied `break-inside: avoid` broadly to the hero/sections. Combined with printed navigation and hero spacing, this caused an avoidable blank region after the hero and pushed Latest to the next page in the observed PDF.

## Hero print fix

V59 print CSS:

- Hides the full interactive site navigation in print
- Keeps site identity/title visible
- Reduces print shell/header/hero spacing
- Makes hero height content-driven
- Removes section-level forced `break-inside: avoid`
- Keeps card-level `break-inside: avoid` where practical
- Renders hero actions as compact inline text links

## Browse/search print cause

V58 hid only the interactive search controls, while the Browse/search section and grid remained in print flow. That left an almost empty standalone Browse/search page.

## Browse/search print fix

V59 hides the entire Browse/search section in print. Normal web search remains unchanged and passed local and remote browser checks.

Standalone Browse/search print-page verdict: PASS; no standalone page remains.

## Before/after print result

Before reference:

- `C:\Users\kotov\Downloads\111\diary-v58-visual\final-remote-print-a4.pdf`
- Observed page count: 9 pages in the preserved local reference file
- Observed defects: Latest heading on page 2, Browse/search standalone page, `L 4` visible, blank/lazy image frame in latest compact card

After V59 local:

- `C:\Users\kotov\Downloads\111\diary-v59-visual\after-v59-print-a4.pdf`
- Page count: 7
- Latest heading page: 1
- First latest-card page: 1

After V59 remote:

- `C:\Users\kotov\Downloads\111\diary-v59-visual\final-remote-v59-print-a4.pdf`
- Page count: 7
- Latest heading page: 1
- First latest-card page: 1

## Image height measurements

Remote print:

- Featured latest image height: 158px
- Featured latest wrapper height: 160px
- Compact latest image heights: 118px
- Start here image heights: 118px

Remote normal web:

- Desktop latest image heights: `[268, 120, 120, 120, 120]`
- Mobile latest image heights: `[172, 172, 172, 172, 172]`
- No horizontal overflow on desktop or mobile

## Verdicts

- Desktop verdict: PASS
- Mobile verdict: PASS
- Print verdict: PASS
- Search verdict: PASS
- Alias-collapse verdict: PASS
- V23 date-only metadata: PASS
- V28 five-entry latest preview: PASS
- Source entry changes: 0
- Entry asset changes: 0
- Sitemap added: 0
- Sitemap removed: 0

## Final clean status

Final clean status is emitted after the report/artifact commit and final deployment validation.

## Manual Search Console remainder

No URLs were added or removed. Manual remainder: request re-indexing of `https://ivankotov.eu/diary/`; sitemap resubmission is optional.
