# Diary Landing V59 Post-Deploy Check

Implementation commit:

- `1465eb26da376de5127b2d48542ba600cd3f0447`

Pages run:

- `29665386676`
- Conclusion: success

Cache-busting token:

- `v59-1465eb2-20260718T2333Z`

## Public HTTP checks

HTTP 200 verified:

- <https://ivankotov.eu/>
- <https://ivankotov.eu/diary/>
- <https://ivankotov.eu/diary/archive/>
- <https://ivankotov.eu/diary/tags/>
- <https://ivankotov.eu/diary/themes/>
- <https://ivankotov.eu/diary/start-here/>
- <https://ivankotov.eu/diary-index.json>
- <https://ivankotov.eu/diary-tags.json>
- <https://ivankotov.eu/diary-latest.json>
- <https://ivankotov.eu/diary-feed.xml>
- <https://ivankotov.eu/sitemap.xml>

## Public DOM checks

Remote section order:

1. Hero
2. Latest
3. Browse/search
4. Start here
5. Themes
6. Cornerstones
7. Tags

Remote positions:

- Hero: `29610`
- Latest: `30387`
- Browse/search: `39467`
- Start here: `41069`
- Themes: `52518`
- Cornerstones: `55396`
- Tags: `67075`

Latest cards rendered: 5.

## Protected-token checks

Remote generated content:

- `L 4`: 0
- `A 6`: 0
- `D 4`: 0
- `A G I`: 0
- `L L M`: 0
- `L4`: visible
- Top tag surface includes `L4 (127)`

Alias collapse remained intact for `AI Safety` / `AISafety` and `AI Architecture` / `AIArchitecture`.

## Featured-image checks

Remote normal web:

- Featured latest wrapper height: 270px desktop, 174px mobile
- Featured latest image height: 268px desktop, 172px mobile
- `object-fit`: `cover`
- `object-position`: `50% 0%`
- `display`: `block`
- wrapper overflow: `hidden`

Remote print:

- Featured wrapper height: 160px
- Featured image height: 158px
- Compact latest image heights: 118px
- Internal blank-image-space verdict: PASS

## Remote print checks

Remote print PDF:

- `C:\Users\kotov\Downloads\111\diary-v59-visual\final-remote-v59-print-a4.pdf`

Measured:

- Page count: 7
- Latest heading page: 1
- First latest-card page: 1
- Browse/search print display: `none`
- Standalone Browse/search page: no

## Search checks

Remote browser query: `Cleanroom`

- Desktop: returned 1 public Diary entry link
- Mobile: returned 1 public Diary entry link
- Result cap: <= 10
- Keyboard ArrowDown active selection: PASS
- Escape clear: PASS

## Count/latest checks

- `diary-index.json` count field: 206
- `diary-index.json` item count: 206
- Latest date: `2026-07-18`
- Latest slug: `the-question-behind-c-a-b-is-not-whether-an-ai-can-look-consistent-over-time`

## Sitemap semantic comparison

- Sitemap URL count: 797
- URLs added: 0
- URLs removed: 0

## Final verdict

PASS after V59 implementation deployment. No open blocker was observed.
