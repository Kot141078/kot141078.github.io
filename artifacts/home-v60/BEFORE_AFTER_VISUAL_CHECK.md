# Before/After Visual Check V60

## Scope

This artifact records the visual receipts for the homepage information-architecture compression. The screenshots and PDFs are stored outside the repository in:

`C:\Users\kotov\Downloads\111\home-v60-visual`

## Before Receipts

| Receipt | Size |
| --- | ---: |
| `before\before-v60-desktop-1440x900.png` | 210069 bytes |
| `before\before-v60-tablet-768x900.png` | 132381 bytes |
| `before\before-v60-mobile-390x844.png` | 59048 bytes |
| `before\before-v60-full-page-desktop.png` | 2267373 bytes |
| `before\before-v60-print-a4.pdf` | 5990917 bytes |

Before print receipt:

- PDF pages: 17

Before homepage metrics:

| Metric | Value |
| --- | ---: |
| Top-level main sections | 18 |
| Cards | 41 |
| Publication cards | 21 |
| Words | 1969 |
| Links | 176 |
| Internal links | 106 |
| External links | 70 |
| DOM elements | 490 |
| Broken internal links | 0 |
| Duplicate IDs | 0 |
| Images | 2 |

## After Receipts

| Receipt | Size |
| --- | ---: |
| `after\after-v60-desktop-1440x900.png` | 169385 bytes |
| `after\after-v60-tablet-768x900.png` | 92108 bytes |
| `after\after-v60-mobile-390x844.png` | 61938 bytes |
| `after\after-v60-full-page-desktop.png` | 867300 bytes |
| `after\after-v60-print-a4.pdf` | 4783020 bytes |

After print receipt:

- PDF pages: 7

After homepage metrics:

| Metric | Value |
| --- | ---: |
| Top-level main sections | 10 |
| Cards | 18 |
| Publication cards | 4 |
| Words | 803 |
| Links | 73 |
| Internal links | 56 |
| External links | 17 |
| DOM elements | 243 |
| Broken internal links | 0 |
| Duplicate IDs | 0 |

## Visual Findings

Desktop 1440 x 900:

- The first viewport presents one primary hero and a visible path into the next section.
- Duplicate homepage route systems are removed.
- The latest-post card appears in the upper half of the page after the install-c layer.
- The featured-work block contains exactly four publication cards.
- The book layer is compact and does not dominate the homepage.

Tablet 768 x 900:

- Sections stack cleanly.
- Cards keep stable spacing.
- No visible clipping was observed.

Mobile 390 x 844:

- Navigation/action pills wrap without horizontal overflow.
- Hero copy and route cards fit inside the viewport.
- No clipped text was observed.

Full-page desktop:

- Final section order matches the contract order.
- Full publication catalogue and timeline are absent from the homepage.
- Public links/footer remains compact.

Print A4:

- Print output reduced from 17 pages to 7 pages.
- Print was treated as a secondary validation surface; no print-specific content changes were introduced.

## Responsive Receipt

Chrome DevTools Protocol viewport checks:

| Viewport | `innerWidth` | `clientWidth` | `scrollWidth` | Overflow |
| --- | ---: | ---: | ---: | --- |
| Desktop 1440 x 900 | 1440 | 1425 | 1425 | false |
| Tablet 768 x 900 | 768 | 753 | 753 | false |
| Mobile 390 x 844 | 390 | 390 | 390 | false |

## Verdict

PASS.
