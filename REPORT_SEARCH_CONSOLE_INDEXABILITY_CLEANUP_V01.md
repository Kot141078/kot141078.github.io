# Search Console indexability cleanup V0.1

Date: 2026-08-24  
Repository: `Kot141078/kot141078.github.io`  
Branch: `main`

## Result

PASS. The implementation removes Diary tag archives from the index-intended surface, reduces generated tag-link boilerplate, conservatively canonicalizes exact orthographic tag aliases, strengthens the six requested corpus entries, and preserves the mandatory Diary author blocks byte-for-byte.

This work changes the site's indexing architecture; it cannot guarantee that Google will index a particular URL. Google makes that decision after deployment and recrawl.

## Custody and baseline

- Initial synchronized SHA: `1993e8a3a6d567df1d63d91729b25087336f2cd5`.
- Initial branch state: clean `main`, with local `HEAD` equal to `origin/main` (`ahead=0`, `behind=0`). No user changes required merging, stashing, deletion, or overwrite.
- Initial hosted CI: Machine readability run `32746652024` was `success`; GitHub Pages was also `success`.
- Workflow checked: `.github/workflows/machine-readability.yml`; its local equivalent is `python tools/run_machine_readability_gate.py`, followed by `git diff --exit-code`.
- Final implementation SHA before this report-only commit: `2ce64687f5798ad11774494509149d2ac14eed58`.
- A commit cannot contain its own SHA. The final report commit and hosted post-push run are therefore recorded in the final handoff accompanying this file.

## Reversible implementation commits

1. `d9b701c14b8a101a8332652fcd92fbacefeeec80` — `seo: exclude diary tag archives from search indexing`
2. `0585f83b52bbb6388682bbb6716f907ffc18ae22` — `seo: reduce diary tag-link boilerplate`
3. `4e62df965ca86caaf353633e1988afb730c055ed` — `seo: normalize equivalent diary tag aliases`
4. `2ce64687f5798ad11774494509149d2ac14eed58` — `seo: strengthen core corpus entry pages`

## Before and after

| Metric | Before | After |
| --- | ---: | ---: |
| Sitemap URLs | 799 | 297 |
| `/diary/tags/` URLs in sitemap | 502 | 0 |
| Physical tag surfaces, including the tag catalog | 525 | 525 |
| Canonical tag records | 502 | 443 |
| Retained legacy alias pages | 22 | 81 |
| Average tag links per source-backed Diary page (206 pages) | 81.976 | 5.699 |
| Maximum tag links on a generated Diary page | greater than 150 in observed cases | 6 |
| Average tag links on the protected 25 pages | 94.84 | 5.96 |
| Average total anchors on the protected 25 pages | 114.32 | 25.44 |
| Average internal page links across 206 Diary pages | not used as the baseline decision metric | 23.782 |
| Tag links inside related cards | many | 0 |

The sitemap result is dynamic: `799 - 502 = 297` for the synchronized baseline. The validator derives the actual sitemap and tag-surface sets; it does not hardcode `297` as a target.

All 525 physical tag surfaces remain navigable. Every one has `noindex, follow`; none is in the sitemap. The count remains stable because legacy URLs were deliberately preserved.

## Index control and Diary generation

- `/diary/tags/` and every `/diary/tags/*/` page now carry `<meta name="robots" content="noindex, follow">`.
- Canonical tag pages retain self-canonicals. Exact legacy aliases carry `noindex, follow` and canonicalize to the selected human-readable canonical tag page.
- `sitemap.xml` contains zero tag surfaces and does not add raw `.json`, `.txt`, `.md`, checksum, package-manifest, or sitemap URLs as content pages.
- Diary hero metadata contains at most six relevance-selected canonical tags.
- Each of the 206 source-backed Diary entries has four related cards (824 cards total). Each card contains one date, one title, one summary, and exactly one `Open entry` link; related cards contain no tag links or empty link containers.
- Related selection orders curated theme, canonical topic, semantic similarity, and only then chronological proximity.
- Primary navigation and source/origin links remain present. Every generated Diary page stays below the 30-internal-page-link guardrail.

## Tag alias normalization

Normalization is deliberately narrow: Unicode casefold followed by removal of spaces and hyphens. Only exact orthographic equivalents are merged. The existing hyphenated human-readable slug is preferred where available. The build now produces:

- 443 unique canonical tag records;
- 81 retained legacy alias pages;
- zero duplicate independent canonical records under the normalized key;
- 2,225 canonical memberships across 206 source entries;
- 1,837 canonical-only tag links across generated Diary surfaces.

No thematic-nearness merges were introduced. For example, `Identity` and `Digital Identity` remain distinct. No meta refresh or JavaScript redirect was added.

## Protected author content

The validator contains the frozen SHA-256 fixture for each of the 25 affected `.post-content` byte ranges. Result: `25/25` exact matches after every regeneration. Author text, escaping, and whitespace inside those blocks did not change.

Template changes are confined to hero tags, related cards, generated navigation, canonical alias handling, and surrounding discovery surfaces.

## Strengthened corpus entries

The six requested entries were strengthened from existing public corpus claims and existing source/DOI surfaces only:

- `/ai-governance/` — 548 main-content words;
- `/long-lived-ai-entities/` — 527;
- `/qubit-state-c/` — 672;
- `/kotov-principle-l4-bound-experience/` — 615;
- `/publications/ester-theoretical-core-v0-1/` — 754;
- `/diary/themes/local-first-infrastructure/` — 709 editorial words before generated cards.

Definitions, neighboring-concept distinctions, `c = a + b`, relevant L4/SER/witness/continuity relations, claim/evidence boundaries, primary-source routes, cross-corpus transitions, and grounded engineering constraints were added without claiming new implementations, results, dates, DOI records, or operational status. Existing canonical URLs, JSON-LD, DOI/Zenodo links, releases, citations, MOT-c, Temporal AI Presence, and machine-readable surfaces remain intact.

Ten priority URLs now have 20 validator-bound contextual links: at least two links per priority URL from two different index-intended pages. Navigation menus and the sitemap do not count toward that matrix.

## Source and generator files changed

- `tools/build_diary.py`
- `tools/validate_search_indexability.py`
- `tools/run_machine_readability_gate.py`
- `content/diary/_curation.json`
- `qubit-state-c.json`
- `ai-governance/index.html`
- `long-lived-ai-entities/index.html`
- `qubit-state-c/index.html`
- `kotov-principle-l4-bound-experience/index.html`
- `publications/ester-theoretical-core-v0-1/index.html`

The local-first theme is generated from `_curation.json`; Qubit-State c keeps its JSON source and HTML surface aligned. The other named corpus entries are hand-authored source pages in the current repository architecture.

## Regenerated files

Git-detected generated changes by reversible commit:

- Index-control commit: 525 `diary/tags/**/index.html` surfaces and `sitemap.xml`; three generator/validator files were also changed (529 files total).
- Boilerplate commit: 208 `diary/*/index.html` entry surfaces, 502 changed canonical tag pages, and six theme pages; two generator/validator files were also changed (718 files total).
- Alias commit: 129 changed Diary entry pages, 130 changed tag pages, `diary/index.html`, `diary-index.json`, `diary-latest.json`, `diary-tag-map.json`, and `diary-tags.json`; two generator/validator files were also changed (266 files total).
- Corpus-entry commit: 13 changed Diary entry pages, seven theme/catalog pages, `diary/index.html`, `diary-themes.json`, the six requested corpus source/output surfaces, and generator/validator inputs (31 files total).

No generated file was hand-edited as a substitute for changing its available source or generator.

## Validation results

Final local run on `2ce64687f5798ad11774494509149d2ac14eed58`:

- `git diff --check`: PASS.
- Full Machine readability gate: PASS — 14 checks.
- JSON Schema validation: PASS — 5 contracts.
- MOT-c source pinning: PASS.
- Temporal AI Presence: `TAP_R4_CLAIM_CONSISTENCY_PASS`.
- Search indexability validator: PASS — 297 sitemap URLs, 0 tag URLs in sitemap, 525 noindex tag pages, 31/31 index-intended fixtures, 206 bounded Diary posts, 824 related cards, 25 protected hashes, 4,265 non-empty `.section-links` containers, 443 canonical tags, 81 aliases, and 20 contextual priority links.
- JSON parsing: PASS for the machine layer and changed generated JSON through the full gate.
- JSON-LD and HTML parsing: PASS through `check_html_pages` and the indexability validator.
- Canonicals: PASS for all tag surfaces and all 31 protected index-intended fixtures.
- Sitemap XML: PASS; 0 tag surfaces and no listed raw assets.
- Internal links: PASS; no canonical links to legacy tag aliases and no broken normalized-tag targets.
- Empty related/link containers: 0.
- Accidental `noindex` on the 31 saved URLs: 0.
- Generated-file freshness: PASS; the full gate left `git diff --exit-code` clean.

## Visual smoke

Playwright/Chromium was run at `1366x900` and `390x844` for all six required surfaces:

1. `/diary/from-better-chat-to-stable-presence/`
2. `/diary/the-next-ai-risk-may-not-look-like-rebellion/`
3. `/diary/saturday-thought/` (ordinary page outside the protected 25)
4. `/diary/tags/l4/`
5. `/ai-governance/`
6. `/publications/ester-theoretical-core-v0-1/`

Result: `12/12 PASS`. Navigation, headings, tag chips, images, related cards, spacing, bottom navigation/footer surfaces, and mobile wrapping were manually reviewed. There was no horizontal overflow (`scrollWidth == viewport width`), no unloaded image, and no empty `.section-links` container. Generated Diary/tag pages retain the semantic site footer. The hand-authored corpus/publication template ends with a final content/link section rather than a separate visible `<footer>`; that pre-existing structure remains visually complete.

The initial visual run found one real 390 px overflow in the Ester citation. The page now reuses the existing `long-text-block` utility; the citation computes as `white-space: pre-wrap` and `overflow-wrap: anywhere`, with a 294 px code box inside the 390 px viewport. The rerun passed. BreadcrumbList structured data remains valid; these templates do not render a separate visible breadcrumb bar.

## Why the seven raw resources stay out of the index surface

These files remain accessible and linked where appropriate, but they are machine evidence, downloadable source/checksum material, or the sitemap itself rather than canonical HTML landing pages:

1. `/downloads/article50-transparency-implementation-briefs-v0-1/PACKAGE_MANIFEST.json`
2. `/publications/a6-ctp-v0-1-4/files/SHA256SUMS_A6_CTP_v0_1_4.txt`
3. `/publications/a6-ctp-v0-1-4/files/SHA256SUMS_A6_CTP_v0_1_4_GITHUB_PLACEMENT.txt`
4. `/downloads/article50-transparency-implementation-briefs-v0-1/02_For_Engineers_CGAM_Witness_Oracle_Degradation.md`
5. `/qubit-state-c.json`
6. `/arq-cq-integration-addendum.json`
7. `/sitemap.xml`

Their availability supports downloads, verification, and machine readability. Excluding them from the content sitemap avoids presenting them as competing document pages; it does not remove them or break their links.

## Residual limits

- Index inclusion remains Google's external decision and can lag deployment/recrawl.
- The 525 tag surfaces remain crawlable by design (`noindex, follow`) so humans, links, and legacy routes keep working; Search Console counts will decay only after Google revisits them.
- GitHub Pages does not provide route-specific server redirects in this repository. Exact legacy tag aliases therefore use `noindex`, `rel=canonical`, and canonical-only internal linking rather than meta refresh or JavaScript.
- Search Console property state was not mutated by this repository run. No live indexing request can be made without the owner's authenticated property session.
- A separate visible breadcrumb component is not part of the existing templates; BreadcrumbList JSON-LD remains the structured breadcrumb surface.

No local implementation blocker remains.

## Owner actions after deployment

Do these only after GitHub Pages has deployed the final commit and both Pages and Machine readability are green:

1. In Search Console, open **Sitemaps** and submit or resubmit `https://ivankotov.eu/sitemap.xml`. Confirm that Google can read it and that the submitted set reflects the reduced index-intended surface.
2. Use **URL Inspection** on a small representative priority set. Run the live test, then click **Request indexing** for the index-intended HTML pages. Do not request indexing for tag archives or the seven raw resources. Google documents the URL Inspection request flow here: <https://support.google.com/webmasters/answer/12482179?hl=en>.
3. Use the sitemap for bulk discovery rather than attempting 31 manual requests at once. Google's recrawl guidance is: <https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl>.
4. Open **Page indexing** → the affected issue details. After the deployed live pages and sitemap are verified, click **Validate fix** once if that control is available for the issue. Do not restart validation while it is in progress. Google notes that validation commonly takes up to about two weeks and can take longer: <https://support.google.com/webmasters/answer/7440203?hl=en>.
5. Monitor the 31 index-intended fixtures, sitemap-discovered totals, selected/declared canonicals, and the declining tag-archive issue count over subsequent recrawls. A request is a recrawl signal, not an indexing guarantee.
