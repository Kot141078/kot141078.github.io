# Diary Landing V58 Post-Deploy Check

Implementation commit:

- `c040cad9d1ce466910b9e2de74934b601d285b73`

Pages run:

- `29662805860`
- Conclusion: success

Cache-busting token:

- `v58-c040cad9-20260718T2207Z`

## Public URL checks

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

Remote cache-busted section order:

1. Hero
2. Latest entries
3. Browse/search
4. Start here
5. Themes
6. Cornerstones
7. Tags

Remote DOM positions:

- Hero: `29610`
- Latest entries: `30387`
- Browse/search: `39463`
- Start here: `41065`
- Themes: `52517`
- Cornerstones: `55395`
- Tags: `67076`

Latest cards rendered: 5.

## Count/latest checks

- `diary-index.json` count field: 206
- `diary-index.json` item count: 206
- Latest date: `2026-07-18`
- Latest slug: `the-question-behind-c-a-b-is-not-whether-an-ai-can-look-consistent-over-time`
- `diary-latest.json` item matches latest slug: yes

## Search checks

Remote browser search query: `Cleanroom`

Results:

- Desktop: 1 result, public latest entry URL returned
- Mobile: 1 result, public latest entry URL returned
- Result count cap: <= 10
- Keyboard ArrowDown selection: PASS
- Escape clears search: PASS

## Canonical tag checks

- Raw top-tag alias `AISafety` visible in landing top-tag surface: no
- Raw top-tag alias `AIArchitecture` visible in landing top-tag surface: no
- Canonical top-tag alias duplicates remaining: 0
- Landing-card tag cap exceeded: no

## Sitemap semantic comparison

- Remote sitemap URL count: 797
- URLs added: 0
- URLs removed: 0

## Remote visual checks

Remote screenshot artifacts:

- `C:\Users\kotov\Downloads\111\diary-v58-visual\remote-desktop-1440x900.png`
- `C:\Users\kotov\Downloads\111\diary-v58-visual\remote-mobile-390x844.png`
- `C:\Users\kotov\Downloads\111\diary-v58-visual\remote-print-a4.pdf`

Remote visual metrics:

- Desktop 1440x900 latest top: `509px`
- Desktop latest image heights: `[268, 120, 120, 120, 120]`
- Desktop Start here image heights: `[158, 158, 158, 158, 158, 158]`
- Mobile 390x844 latest top: `710px`
- Mobile `scrollWidth`: `390`
- Print latest starts on approximate page 1
- Print latest image max: `160px`
- Print Start here image max: `118px`
- Remote print PDF length: 9 pages

## Final verdict

PASS after implementation deployment. No open blocker was observed in the deployed V58 landing page.
