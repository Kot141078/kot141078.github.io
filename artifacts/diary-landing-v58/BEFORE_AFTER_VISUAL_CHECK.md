# Diary Landing V58 Before/After Visual Check

## Current problems observed before V58

- Latest entries were buried below the curated Start here path and theme routes.
- Old curated cards used oversized images and visually dominated the landing page.
- The landing page did not prominently show the 206-entry archive size or date range.
- Start here appeared accidentally non-chronological because the editorial order was not numbered.
- Visible landing tags exposed raw CamelCase and alias duplication such as `AISafety` / `AI Safety` and `AIArchitecture` / `AI Architecture`.
- Landing cards displayed too many tags.
- Print output reproduced the wrong hierarchy, with fresh posts starting late in the capture.

Baseline generated HTML positions recorded before implementation:

- Curated archive surface: `29585`
- Curated entry path: `30054`
- Themes: `29836`
- Latest entries: `42352`
- Cornerstones: `48728`
- Tags: `59788`

## Desktop before/after comparison

Before:

- Latest entries appeared after curated route material.
- Curated old-entry images consumed primary visual attention before the fresh posts.

After:

- Desktop screenshot: `C:\Users\kotov\Downloads\111\diary-v58-visual\after-desktop-1440x900.png`
- Latest section top: `509px` at 1440x900
- Latest appears immediately below the hero and is visible in the first viewport.
- Latest image heights: `[268, 120, 120, 120, 120]`
- Start here image heights: `[158, 158, 158, 158, 158, 158]`
- No horizontal overflow.

## Mobile result

- Mobile screenshot: `C:\Users\kotov\Downloads\111\diary-v58-visual\after-mobile-390x844.png`
- Latest section top: `710px` at 390x844
- Mobile `scrollWidth`: `390`
- Horizontal overflow: none
- Navigation and hero actions wrap cleanly.
- Latest image heights: `[172, 172, 172, 172, 172]`
- Start here image heights: `[158, 158, 158, 158, 158, 158]`

## Print result

- Print PDF: `C:\Users\kotov\Downloads\111\diary-v58-visual\after-print-a4.pdf`
- Latest starts on approximate print page 1.
- Latest image heights in print CSS: `[160, 160, 160, 160, 160]`
- Start here image heights in print CSS: `[118, 118, 118, 118, 118, 118]`
- PDF page count: 9
- Interactive search controls are hidden in print.
- Section headings remain present.

Remote print artifact:

- `C:\Users\kotov\Downloads\111\diary-v58-visual\remote-print-a4.pdf`

## Exact latest-section position

After remote deployment, cache-busted DOM positions were:

- Hero: `29610`
- Latest entries: `30387`
- Browse/search: `39463`
- Start here: `41065`
- Themes: `52517`
- Cornerstones: `55395`
- Tags: `67076`

## Maximum rendered image heights

Measured after V58:

- Desktop latest max: `268px`
- Desktop Start here max: `158px`
- Mobile latest max: `172px`
- Mobile Start here max: `158px`
- Print latest max: `160px`
- Print Start here max: `118px`

## Tag duplication before/after

Before:

- The landing tag surface could show alias variants as separate visible labels.

After:

- `AI Safety` / `AISafety` separate visible top-tag chips remaining: 0
- `AI Architecture` / `AIArchitecture` separate visible top-tag chips remaining: 0
- Landing-card tags are canonicalized and capped to six chips.
- Source raw tags and historical tag pages remain preserved.

## Visual tooling limitation

No blocking visual tooling limitation remained. Local Chrome/Playwright was available for desktop, tablet, mobile, print PDF, browser search, and live cache-busted checks.
