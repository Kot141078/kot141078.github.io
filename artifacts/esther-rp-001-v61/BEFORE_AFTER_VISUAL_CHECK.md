# Before/After Visual Check V61

## Scope

Visual receipts for the ESTHER-RP-001 publication page style alignment.

Receipt root:

`C:\Users\kotov\Downloads\111\esther-rp-001-v61-visual`

## Before State

The target page behaved as a standalone microsite:

- no standard Ivan Kotov header
- no standard primary navigation
- no standard footer
- inline standalone theme
- dark-mode media rule
- system-ui heading typography
- standalone blue link styling
- raw `pre` archive/checksum block
- raw `pre` evidence block
- separate `.panel`, `.grid`, and `.status` component system

Dark-preference computed baseline:

- Background: `rgb(16, 18, 22)`
- Text: `rgb(237, 240, 245)`
- Link color: `rgb(121, 170, 255)`
- H1 font: system UI stack
- Header visible: false
- Footer visible: false
- Navigation visible: false
- `pre` block present: true

Before screenshots:

| Receipt | Size |
| --- | ---: |
| `before\before-desktop-1440x900.png` | 77777 bytes |
| `before\before-tablet-768x900.png` | 62144 bytes |
| `before\before-mobile-390x844.png` | 49209 bytes |
| `before\before-full-page-desktop.png` | 204900 bytes |
| `before\before-print-a4.pdf` | 82642 bytes |

Before print:

- A4
- 4 pages

## After Local State

After V61 the target page uses:

- shared `styles.css`
- shared `styles-base.css`
- standard `site-shell`
- standard `site-header`
- standard `site-nav`
- shared `hero`, `section`, `card`, and `section-links`
- compatible `site-footer`
- target-scoped layout CSS only

After-local screenshots:

| Receipt | Size |
| --- | ---: |
| `after\after-local-desktop-1440x900.png` | 161339 bytes |
| `after\after-local-tablet-768x900.png` | 96293 bytes |
| `after\after-local-mobile-390x844.png` | 63925 bytes |
| `after\after-local-narrow-mobile-320x700.png` | 47804 bytes |
| `after\after-local-full-page-desktop.png` | 456777 bytes |
| `after\after-local-print-a4.pdf` | 208336 bytes |

After-local print:

- A4
- 4 pages

## Color And Background Comparison

Before under dark preference:

- Standalone dark page background
- White text
- Custom blue links

After under dark preference:

- Shared light site gradient
- Dark readable text
- Shared site button/link-chip treatment

Remote after computed style:

- Background image: shared radial and linear light site background
- Text color: `rgb(30, 36, 41)`
- Body font: `"Segoe UI", "Trebuchet MS", system-ui, sans-serif`
- H1 font: `Georgia, "Times New Roman", serif`

## Typography Comparison

Before:

- H1 used system UI stack
- Page scale and rhythm were standalone

After:

- H1 uses shared serif heading typography
- Body text uses shared site sans-serif stack
- Section labels and headings follow the existing site rhythm

## Header And Footer Comparison

Before:

- No standard header
- No primary navigation
- Footer was a plain text line inside `main`

After:

- Standard Ivan Kotov header visible
- Primary navigation visible
- Publications current-section state visible
- Footer uses shared `site-footer`
- License line preserved exactly
- Public links present: GitHub, LinkedIn, ORCID, HAL, ivankotov.eu

## Card Comparison

Before:

- Standalone `.panel` cards with separate radius and dark-compatible styling

After:

- Shared `.card` and `.section` treatment
- Read and test cards align in desktop three-column layout
- Evidence metrics use compact shared-light cards
- Claim boundary uses restrained shared-card treatment

## Archive Overflow Before/After

Before:

- Archive filename, SHA-256, members, and CRC were combined in one raw `pre` block.

After:

- Archive uses structured semantic labels.
- Full SHA-256 remains visible and selectable.
- No ellipsis truncation.
- No archive horizontal scrollbar.

Local archive overflow checks:

- 1440 px: false
- 768 px: false
- 390 px: false
- 320 px: false

Remote archive overflow checks:

- 1440 px: false
- 390 px: false
- 320 px: false

## Verdicts

Desktop: PASS.

Tablet: PASS.

Mobile 390 px: PASS.

Narrow mobile 320 px: PASS.

Full-page desktop: PASS.

Print A4: PASS.

Comparison with homepage, Diary, Publications index, and standard publication styling: PASS.

## Remote Receipts

Remote cache token:

`v61-20260719215840`

Remote screenshots:

| Receipt | Size |
| --- | ---: |
| `after\final-remote-desktop-1440x900.png` | 161339 bytes |
| `after\final-remote-mobile-390x844.png` | 63925 bytes |
| `after\final-remote-full-page-desktop.png` | 456777 bytes |
| `after\final-remote-print-a4.pdf` | 208333 bytes |

Final remote print:

- A4
- 4 pages

## Final Visual Verdict

PASS.
