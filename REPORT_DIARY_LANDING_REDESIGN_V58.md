# Diary Landing Redesign V58 Report

Contract: `DIARY_LANDING_INFORMATION_ARCHITECTURE_AND_VISUAL_REDESIGN_V58`

Live target: <https://ivankotov.eu/diary/>

## Source of truth

- Generator: `tools/build_diary.py`
- Generated landing page: `diary/index.html`
- Curated route data: `content/diary/_curation.json`
- Landing CSS override layer: `styles.css`
- Base CSS intentionally unchanged: `styles-base.css`
- Public machine surfaces validated unchanged in count/identity: `diary-index.json`, `diary-tags.json`, `diary-latest.json`, `diary-feed.xml`, `sitemap.xml`

The landing page is generated. V58 changed the canonical generator and scoped CSS, then rebuilt `diary/index.html`; generated HTML was not hand-patched as the source of truth.

## Files changed

Implementation commit `c040cad9d1ce466910b9e2de74934b601d285b73` changed:

- `tools/build_diary.py`
- `styles.css`
- `diary/index.html`

Report/artifact commit: emitted in the final terminal output; this report is part of that commit.

## Non-content boundary

- Diary source entries changed: 0
- Entry assets changed: 0
- `content/diary/*.md` changed: no
- `assets/diary/**` changed: no
- Entry slugs, dates, LinkedIn URLs, bodies, raw hashtags, cover images, archive URLs, tag URLs, theme URLs, and entry URLs were not edited.

## Section order

Before V58, the generated landing page placed the curated Start here path and theme routing before the Latest entries surface. Baseline generated HTML positions recorded before implementation showed Latest entries after the curated route and theme material, with Latest around byte offset `42352`.

After V58, the generated DOM order is:

1. Hero
2. Latest entries
3. Browse/search
4. Start here
5. Themes
6. Cornerstones
7. Tags

Remote cache-busted DOM positions after deployment:

- Hero: `29610`
- Latest entries: `30387`
- Browse/search: `39463`
- Start here: `41065`
- Themes: `52517`
- Cornerstones: `55395`
- Tags: `67076`

## Archive count and date range

The hero archive-stat line is generated from the Diary dataset, not hardcoded.

Observed output:

- `206 entries · 2 January 2026–18 July 2026`

Validation:

- `diary-index.json` count: 206
- Latest slug: `the-question-behind-c-a-b-is-not-whether-an-ai-can-look-consistent-over-time`
- Latest date: `2026-07-18`

## Latest-card behavior

Latest entries are now immediately below the hero and render exactly five cards:

1. `2026-07-18`
2. `2026-07-16`
3. `2026-07-15`
4. `2026-07-14`
5. `2026-07-13`

The first latest image loads eagerly. Remaining latest images use lazy loading. Cards render thumbnails only when an entry has an image.

## Image sizing behavior

Measured local visual metrics:

- Desktop 1440x900: latest top `509px`; latest image heights `[268, 120, 120, 120, 120]`; Start here image heights `[158, 158, 158, 158, 158, 158]`
- Tablet 768x900: latest top `579px`; no horizontal overflow; Start here image max `158px`
- Mobile 390x844: latest top `710px`; no horizontal overflow; latest image height `172px`; Start here image max `158px`
- Print A4: latest starts on approximate print page 1; latest image max `160px`; Start here image max `118px`; PDF length 9 pages

## Search implementation

V58 adds a small vanilla JavaScript client-side search block:

- Uses existing `../diary-index.json`
- No external search service
- No analytics
- No tracking
- No duplicate search index
- Searches title, summary, date, canonical display tags, and raw tags
- Case-insensitive
- Debounced at 140ms
- Returns at most 10 live results
- Escape clears results
- Arrow keys select results
- Enter opens the selected result
- No local file paths or private metadata exposed

Local and remote browser checks searched for `Cleanroom` and returned the public latest entry URL.

## Start here

The curated Start here route is preserved and now rendered as a numbered compact editorial path:

- Route numbers: `01` through `06`
- Explanatory copy states that entries are not newest posts and not a ranking.
- Cards are compact, two-column on desktop where space allows, one-column on mobile.
- Landing-card tags are capped to six display chips with `+N more` when applicable.

## Themes

Theme routes are preserved. The Diary landing page now renders themes as compact cards with:

- Title
- Concise description
- Curated-entry count
- Open theme link

No large theme images or expanded full entry lists are rendered on the landing page.

## Cornerstones

The existing cornerstone set is preserved and rendered as compact cards with:

- Date
- Title
- Summary
- Up to six canonical display tags
- Open entry link

The section no longer uses oversized Start here image treatment.

## Tag canonicalization

Raw historical tags remain preserved in source Markdown and machine data. V58 adds a deterministic display-only canonicalization layer for landing-page cards and the landing top-tag surface.

Alias families mapped:

- `AISafety`, `AI Safety` => `AI Safety`
- `AIArchitecture`, `AI Architecture` => `AI Architecture`
- `AdvancedGlobalIntelligence`, `Advanced Global Intelligence`, `AGI` => `Advanced Global Intelligence`
- `SystemsThinking`, `Systems Thinking` => `Systems Thinking`
- `HumanCenteredAI`, `Human Centered AI`, `Human-Centered AI`, `Human Centric AI` => `Human-Centered AI`
- `LongLivedAI`, `Long Lived AI`, `Long-Lived AI` => `Long-Lived AI`
- `AIGovernance`, `AIgovernance`, `AI Governance` => `AI Governance`
- `DigitalEntities`, `Digital Entities` => `Digital Entities`
- `DigitalSovereignty`, `Digital Sovereignty` => `Digital Sovereignty`
- `AIInfrastructure`, `AI Infrastructure` => `AI Infrastructure`
- `HumanAI`, `Human AI` => `Human AI`
- `FutureOfAI`, `Future of AI` => `Future of AI`

Canonical counts are computed by distinct Diary entries per canonical display family. One entry contributes at most once to a canonical tag count even if it contains multiple aliases.

Landing top-tag validation:

- `AI Safety` / `AISafety` duplicate chips remaining: 0
- `AI Architecture` / `AIArchitecture` duplicate chips remaining: 0

## Card tag cap

Landing cards display no more than six canonical display tag chips. Additional tags are summarized with `+N more`. Source tags and tag-index data remain unchanged.

## Print behavior

Print CSS hides interactive-only search UI, keeps section headings, compacts cards, avoids unnecessary page breaks where practical, and caps printed images:

- Latest image max height: 160px
- Start here image max height: 120px
- Compact/cornerstone image max height: 120px

Measured local print:

- Latest begins on approximate print page 1
- PDF length: 9 pages

## Accessibility checks

Validated:

- One H1
- Semantic section order
- Search label present
- Search status uses live region
- Search results use listbox/options
- Keyboard selection works
- Escape clears search results
- Focus-visible styles exist for links, search input, and result links
- Images use existing title/metadata-based alt text without invented claims

## Responsive checks

Validated at:

- Desktop 1440x900
- Tablet 768x900
- Mobile 390x844
- Print A4

Computed browser checks showed `scrollWidth == viewport width` and zero scrollable overflow descendants on desktop/tablet/mobile.

## Performance checks

- No new framework
- No third-party dependency
- No external search API
- No analytics
- No duplicate search index
- Non-first landing images use lazy loading
- Only visible curated/latest card images are rendered on the landing page
- Existing image assets are reused; no image files duplicated

## Sitemap membership comparison

- Before sitemap URL count: 797
- After sitemap URL count: 797
- URLs added: 0
- URLs removed: 0

## V23 and V28 results

- V23 date-only metadata: PASS
- V28 five-entry latest preview: PASS

## Local validation

PASS:

- `python tools/build_diary.py`
- `git diff --check`
- No `content/diary/*.md` diff
- No `assets/diary/**` diff
- HTML parse
- JSON parse
- XML parse
- Internal link file-existence check
- Sitemap semantic comparison
- DOM section order check
- Exact latest-five check
- Browser search interaction
- Desktop/mobile/tablet/print visual checks

## Remote validation

Cache-busting token:

- `v58-c040cad9-20260718T2207Z`

HTTP 200 verified for:

- `/`
- `/diary/`
- `/diary/archive/`
- `/diary/tags/`
- `/diary/themes/`
- `/diary/start-here/`
- `/diary-index.json`
- `/diary-tags.json`
- `/diary-latest.json`
- `/diary-feed.xml`
- `/sitemap.xml`

Remote checks:

- Count 206: PASS
- Latest slug/date: PASS
- Latest before Start here: PASS
- Latest cards rendered: 5
- Search returns public entry links: PASS
- Canonical top-tag duplicates remaining: 0
- Card tag cap: PASS
- Sitemap URLs added/removed: 0/0

## Final status

Final clean status and report/artifact commit hash are emitted in the final terminal output after the report commit and final deployment validation.

## Manual Search Console remainder

No new Diary URLs were created in V58. Manual remainder: request re-indexing of the redesigned Diary landing page and optionally resubmit the sitemap.
