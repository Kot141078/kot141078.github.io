# Home Information Architecture Compression V60

## Scope

Contract: `HOME_PAGE_INFORMATION_ARCHITECTURE_COMPRESSION_V60`.

Repository: `C:\Users\kotov\Desktop\AGI\kot141078.github.io`.

Public target: `https://ivankotov.eu/`.

This report covers the homepage information-architecture compression only. It does not import Diary content, rewrite the corpus, migrate URLs, change sitemap membership, change metadata policy, or alter the scientific or conceptual meaning of the site.

## Source Of Truth

The homepage source of truth is the checked-in static site:

- `index.html`: homepage section order, hero copy, audience route cards, install-c card, featured-public-work cards, core-concept cards, Explore routes, book-layer card, reality paragraph, and public-links section.
- `tools/build_diary.py`: dynamic homepage latest-post slot renderer. The latest Diary entry is still taken from `diary-latest.json`; it was not hardcoded into the homepage as a permanent manual card.
- `styles.css`: homepage-specific layout compression, responsive constraints, compact image/card rules, and mobile overflow fixes.
- `styles-base.css`: shared visual language and base styling. This file was present and remained unchanged.

Implementation commit:

`07bde9f2fdc6fa18221e2e89944c5228fe285b44`

Commit message:

`Homepage information-architecture compression, latest-post promotion, curated featured work, compact book layer, and duplicate-route removal.`

## Information Architecture

Final homepage order:

1. Header/nav
2. Primary hero
3. Three ways in
4. How to install c
5. Latest post
6. Featured public work
7. Core concepts
8. Explore corpus
9. Qubit of Hope
10. Reality before rhetoric
11. Public links/footer

Removed or merged duplicate surfaces:

- Split intro and AGI hero were merged into one primary hero.
- Repeated route clusters were compressed into `Three ways in` and `Explore corpus`.
- The full publication catalogue was removed from the homepage and replaced by exactly four featured publication cards.
- The timeline block was removed from the homepage.
- The duplicate standalone `c = a + b` bridge was folded into the core-concepts layer.
- The book layer was reduced to a compact `Qubit of Hope` card.

## Content Compression

Measured from the local source before and after V60:

| Metric | Before | After |
| --- | ---: | ---: |
| Top-level main sections | 18 | 10 |
| Cards | 41 | 18 |
| Publication cards | 21 | 4 |
| Words | 1969 | 803 |
| Links | 176 | 73 |
| DOM elements | 490 | 243 |
| Print PDF pages | 17 | 7 |

The homepage keeps all required entry routes while reducing repeated explanation and catalogue density.

## Link Coverage

Required routes retained:

- `./start-here/`
- `./what-is-running/`
- `./publications/`
- `./evidence/`
- `./diary/`
- `./library/`
- `./corpus-map/`
- `./services/`
- `./about/`
- `./contact/`
- `./c-a-plus-b/`
- `./l4/`
- `./ser/`
- `./qubit-of-hope/`
- `./publications/cleanroom-arm-p-open-verification-v1-0-1/`
- `./install-c/`
- `https://github.com/Kot141078/ester-clean-code`

Local and remote internal homepage links resolved successfully.

## Diary And Sitemap Invariants

Protected Diary and sitemap files were not changed by the implementation:

- `content/diary/*.md`: no diff
- `assets/diary/**`: no diff
- `diary/index.html`: no diff
- `diary-index.json`: no diff
- `diary-latest.json`: no diff
- `sitemap.xml`: no diff
- `robots.txt`: no diff

Diary receipt:

- Diary public count: 206
- Latest date: `2026-07-18`
- Latest slug: `the-question-behind-c-a-b-is-not-whether-an-ai-can-look-consistent-over-time`
- Latest title: `The question behind c = a + b is not whether an AI can look consistent over time.`

Sitemap receipt:

- Local sitemap URL count: 797
- Remote sitemap URL count: 797
- Added sitemap URLs: 0
- Removed sitemap URLs: 0

## Responsive And Accessibility

Validated viewports:

- Desktop: 1440 x 900
- Tablet: 768 x 900
- Mobile: 390 x 844

Checks passed:

- One `h1`.
- Logical section heading structure preserved.
- Header/nav visual language preserved.
- No horizontal overflow in validated desktop, tablet, or mobile viewports.
- Mobile navigation/action pills wrap without text clipping.
- Latest-post and book images are constrained by aspect-ratio and max-height rules.
- No new JavaScript framework, external script, analytics script, or tracking script was introduced.
- Existing keyboard focus styling is preserved.

## Build And Validation

Local build command:

```powershell
C:\Python310\python.exe tools\build_diary.py
```

Local validation passed:

- `git diff --check`
- JSON parse checks for 43 JSON files
- `sitemap.xml` XML parse check
- `diary-feed.xml` XML parse check
- Homepage structure/order validator
- Internal homepage link validator
- Duplicate ID validator
- Broken local image validator
- Local path and placeholder scan

External probe note:

- DOI, GitHub, HAL, and ORCID probes returned HTTP 200.
- LinkedIn returned HTTP 999, consistent with anti-automation blocking; the existing public link was preserved and this was not treated as a homepage regression.

## Visual Receipts

Before receipts:

- `C:\Users\kotov\Downloads\111\home-v60-visual\before\before-v60-desktop-1440x900.png`
- `C:\Users\kotov\Downloads\111\home-v60-visual\before\before-v60-tablet-768x900.png`
- `C:\Users\kotov\Downloads\111\home-v60-visual\before\before-v60-mobile-390x844.png`
- `C:\Users\kotov\Downloads\111\home-v60-visual\before\before-v60-full-page-desktop.png`
- `C:\Users\kotov\Downloads\111\home-v60-visual\before\before-v60-print-a4.pdf`

After receipts:

- `C:\Users\kotov\Downloads\111\home-v60-visual\after\after-v60-desktop-1440x900.png`
- `C:\Users\kotov\Downloads\111\home-v60-visual\after\after-v60-tablet-768x900.png`
- `C:\Users\kotov\Downloads\111\home-v60-visual\after\after-v60-mobile-390x844.png`
- `C:\Users\kotov\Downloads\111\home-v60-visual\after\after-v60-full-page-desktop.png`
- `C:\Users\kotov\Downloads\111\home-v60-visual\after\after-v60-print-a4.pdf`

Remote receipts:

- `C:\Users\kotov\Downloads\111\home-v60-visual\after\final-remote-v60-desktop-1440x900.png`
- `C:\Users\kotov\Downloads\111\home-v60-visual\after\final-remote-v60-mobile-390x844.png`
- `C:\Users\kotov\Downloads\111\home-v60-visual\after\final-remote-v60-full-page-desktop.png`
- `C:\Users\kotov\Downloads\111\home-v60-visual\after\final-remote-v60-print-a4.pdf`

## Deployment

GitHub Pages deployment for the implementation commit completed successfully.

- Workflow: `pages-build-deployment`
- Run ID: `29692675430`
- Head SHA: `07bde9f2fdc6fa18221e2e89944c5228fe285b44`
- Conclusion: success
- Build job: `88208043890`, success
- Report-build-status job: `88208091299`, success
- Deploy job: `88208091338`, success

Remote validation cache token:

`v60-20260719172234`

Remote homepage, required routes, Diary JSON, and sitemap checks passed.

## Verdict

PASS.

V60 compresses the homepage information architecture while preserving the site's visual language, public routes, Diary count/latest-entry invariants, sitemap membership, and dynamic latest-post extraction.
