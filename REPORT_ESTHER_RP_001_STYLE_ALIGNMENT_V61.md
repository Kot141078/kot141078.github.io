# ESTHER-RP-001 Style Alignment V61

## Baseline

Original V61 attempt stopped before edits because the first contract carried a truncated SHA-256. The amendment names the full repository-agreed hash as authoritative.

Accepted baseline for this resumed run:

- Branch: `main`
- Baseline HEAD: `cbe41a0759ef0759aee2fcb58a3546813ef9b651`
- `HEAD == origin/main`: true at preflight
- Worktree clean before edits: true
- Target URL: `https://ivankotov.eu/publications/esther-rp-001/`
- Target page exists locally: true
- Sitemap URL count at baseline: 798
- Target URL in sitemap at baseline: 1
- Diary count: 206
- Diary latest: `2026-07-18`, `the-question-behind-c-a-b-is-not-whether-an-ai-can-look-consistent-over-time`

## Source Of Truth

Canonical target-page source:

- `publications/esther-rp-001/index.html`

Publication metadata sources used for fidelity checks:

- `esther-rp-001.json`
- `publications/esther-rp-001/PUBLICATION_STATUS.json`

Shared visual sources reused:

- `styles.css`
- `styles-base.css`
- Existing `.site-shell`, `.site-header`, `.site-nav`, `.hero`, `.section`, `.card`, `.section-links`, and `.site-footer` patterns from homepage, Diary, Publications index, and standard publication pages.

## Cause Of Standalone Dark Design

The standalone design came from inline CSS in `publications/esther-rp-001/index.html`.

Before V61 the page used:

- inline `<style>`
- `color-scheme: light dark`
- `@media (prefers-color-scheme: dark)`
- standalone CSS variables for `--bg`, `--fg`, `--panel`, `--line`, and `--accent`
- standalone `body`, `main`, `h1`, `h2`, `a`, `pre`, `.panel`, `.grid`, `.status`, and `footer` rules
- no shared site header
- no shared navigation
- no shared footer
- raw `pre` blocks for archive and evidence

Dark-preference computed baseline:

- Body background: `rgb(16, 18, 22)`
- Body text: `rgb(237, 240, 245)`
- Link color: `rgb(121, 170, 255)`
- H1 font: system UI stack
- Header/nav/footer: absent
- `pre`: present

## Files Changed

Implementation commit changed exactly:

- `publications/esther-rp-001/index.html`

No changes were made to:

- `esther-rp-001.json`
- `publications/esther-rp-001/PUBLICATION_STATUS.json`
- `sitemap.xml`
- `sitemap-esther-rp-001.xml`
- `robots.txt`
- `diary-index.json`
- `diary-latest.json`
- `content/diary/*`
- `assets/diary/*`
- homepage
- Diary
- Publications index
- comparison publication page

## CSS Removed, Reused, And Added

Removed:

- standalone dark/light variable theme
- page-owned body/background/font/link system
- page-owned panel/status/pre visual system
- standalone dark-mode media rule

Reused:

- shared site background and neutral palette
- shared serif heading typography
- shared sans-serif body typography
- shared header/navigation
- shared card, border, radius, button/chip, spacing, and print behavior

Page-specific CSS added:

- `.esther-rp001` scoped publication context layout
- wrapped status-chip list
- three-card Read and test grid
- structured archive and identifier definition lists
- archive/hash `overflow-wrap: anywhere` behavior
- compact evidence grid
- restrained claim-boundary border
- footer public-link layout
- responsive breakpoints for 980 px and 680 px
- print break-avoid rules for small evidence/archive cards

No new framework, external CSS, external JavaScript, external font, tracking, analytics, or image asset was introduced.

## Before And After Structure

Before:

1. Main-only page
2. Eyebrow
3. H1
4. Deck
5. Author line
6. Standalone status panel
7. The question
8. Read and test
9. Raw archive `pre`
10. Raw evidence `pre`
11. Reviewer list
12. Identifier paragraphs
13. Claim boundary paragraph
14. Plain footer line

After:

1. Standard site header and navigation
2. Publication breadcrumb/context
3. Publication hero
4. The question
5. Read and test
6. Canonical English DOI archive
7. Bounded evidence
8. What reviewers should test
9. Persistent identifiers
10. Claim boundary
11. Standard compatible footer

## Integration Results

Header integration: PASS. The page now uses the shared `site-header` brand and primary `site-nav`, with Publications marked as current.

Navigation integration: PASS. Visible labels are Home, Start here, Publications, Diary, Topics, Library, Services, About, and Contact.

Publication context: PASS. The page shows `Publications / ESTHER-RP-001 v0.8.1` and actions for Back to Publications, Open DOI archive, and Open GitHub release.

Hero alignment: PASS. The hero uses the shared `.hero` card, shared heading typography, light site background, and exact H1.

Status-chip behavior: PASS. All four status statements remain exact and wrap without overflow.

Read and test layout: PASS. Three cards render in a three-column desktop grid, adapt to tablet/mobile, and preserve the original card text and destination URLs.

Archive evidence restructuring: PASS. The archive moved from a raw `pre` line into a structured evidence card with semantic labels.

SHA-256 overflow fix: PASS. The full hash remains visible, selectable, and wrapped safely with no archive scrollbar at 1440, 768, 390, or 320 px.

Evidence layout: PASS. Seven evidence items render as compact shared-light cards.

Identifiers layout: PASS. DOI and Zenodo identifiers render as a wrapping definition list with visible link text.

Claim-boundary treatment: PASS. The exact non-claim sentence is preserved in a restrained boundary card, not an alert.

Footer integration: PASS. The page now uses `site-footer`, preserves `Ivan Kotov · 2026 · Documentation CC BY 4.0 · Code MIT`, and includes GitHub, LinkedIn, ORCID, HAL, and primary-domain links.

## Content Fidelity

Authoritative SHA-256 source:

- `publications/esther-rp-001/index.html`
- `esther-rp-001.json`
- `publications/esther-rp-001/PUBLICATION_STATUS.json`

Full SHA-256 preserved:

`83e71e2fab938e3110293a61967a85440969d8d7eb78a69bf4c1ae40afd4a9d7`

Content values changed: 0.

Verified exact preservation:

- Title
- Release identifier
- Eyebrow
- Deck
- Ivan Kotov / ORCID / Independent Researcher / Brussels metadata
- Four status statements
- Question paragraph
- Selective Operational Commitment paragraph
- Three Read and test cards
- Archive filename
- Full SHA-256
- Members `116`
- CRC `PASS`
- Archive explanatory paragraph
- Seven bounded-evidence values
- Reviewer test list
- Published version DOI
- Concept DOI
- Zenodo record
- Previous DOI-backed release
- Claim boundary
- License line

Truncated hash present: false.

## Link Fidelity

Existing target-page hrefs missing after implementation: 0.

Local target-page link validation:

- Total unique target anchors: 21
- HTTP PASS: 20
- LinkedIn automation block: 1
- Failures: 0

Remote target-page link validation:

- Total unique target anchors: 21
- HTTP PASS: 20
- LinkedIn automation block: 1
- Failures: 0

The LinkedIn URL returns HTTP 999 to automation while the public URL itself is preserved.

## Metadata Fidelity

Unchanged:

- `<title>`
- meta description
- canonical URL
- Open Graph title
- Open Graph description
- Open Graph type
- Open Graph URL
- JSON-LD payload
- English language declaration

Canonical URL remains:

`https://ivankotov.eu/publications/esther-rp-001/`

## Responsive And Print Results

Local CDP checks:

- Desktop 1440 x 900: PASS
- Wide desktop 1920 x 1080: PASS
- Tablet 768 x 900: PASS
- Mobile 390 x 844: PASS
- Narrow mobile 320 x 700: PASS
- Archive overflow: false at every checked viewport
- Page overflow: false at every checked viewport
- H1 count: 1
- Header/nav/footer visible: true

After-local print:

- A4
- 4 pages
- Light readable output
- No clipped SHA-256 observed

Remote CDP checks:

- Desktop 1440 x 900: PASS
- Mobile 390 x 844: PASS
- Narrow mobile 320 x 700: PASS
- Final remote print: A4, 4 pages

## Regression Results

Homepage V60: PASS.

Diary V59: PASS.

Publications index: PASS.

Comparison publication page `publications/cleanroom-arm-p-open-verification-v1-0-1/`: PASS.

Diary count: 206.

Diary latest: `2026-07-18`, `the-question-behind-c-a-b-is-not-whether-an-ai-can-look-consistent-over-time`.

## Sitemap Semantic Comparison

Baseline sitemap URL count: 798.

Current local sitemap URL count: 798.

Remote sitemap URL count: 798.

URLs added: 0.

URLs removed: 0.

Target URL present exactly once: true.

## Deployment

Implementation commit:

`a9e6fa19a37168134b4c813df8240c94474e3328`

Commit message:

`Align ESTHER-RP-001 publication page with the shared ivankotov.eu visual system.`

Implementation Pages run:

- Run ID: `29701587490`
- Conclusion: success
- Build job: `88231418197`, success
- Report-build-status job: `88231467690`, success
- Deploy job: `88231467693`, success
- Non-failing annotation: GitHub Actions Node.js 20 deprecation warning

Report/artifact commit:

To be emitted in the final terminal output after these report files are committed.

## Search Console Remainder

Manual Search Console action remains:

- Request re-indexing for `https://ivankotov.eu/publications/esther-rp-001/`
- Review `https://ivankotov.eu/publications/`
- Optional sitemap resubmission for `https://ivankotov.eu/sitemap.xml`

## Final Clean Status

Final clean status is verified after the report/artifact commit and emitted in the final terminal output.

## Verdict

PASS.

The target page no longer forces a standalone dark microsite design and now belongs visually to the shared ivankotov.eu site system while preserving the authoritative full SHA-256, research text, DOI values, evidence values, links, metadata, canonical URL, Diary state, and sitemap membership.
