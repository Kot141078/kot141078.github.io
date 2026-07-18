# Post Deploy Check V55

Implementation commit validated: `aa1f5bb973e65c61c6267a99981286229eb9c0a9`

Public deployment observed at `https://ivankotov.eu/` after `origin/main` updated.

GitHub Pages run: `29656834303` (`https://github.com/Kot141078/kot141078.github.io/actions/runs/29656834303`), conclusion `success`.

## HTTP Results

- New entry pages: `5/5` HTTP 200.
- New image assets: `3/3` HTTP 200.
- Affected tag pages: `34/34` HTTP 200.
- Core surfaces: `9/9` HTTP 200:
  - `/`
  - `/diary/`
  - `/diary/archive/`
  - `/diary/tags/`
  - `/diary-index.json`
  - `/diary-tags.json`
  - `/diary-latest.json`
  - `/diary-feed.xml`
  - `/sitemap.xml`

## Parse Results

- Selected live HTML pages: `43/43` parsed (`5` entries, `34` affected tag pages, and `4` core HTML surfaces).
- Strict live JSON: `3/3` parsed without duplicate keys or UTF-8 BOM.
- Live XML: `2/2` parsed with entity resolution and network access disabled.

## State Checks

- Remote `diary-index.json` count: `195`.
- Remote latest slug: `entity-vs-profile-a-witness-root-custody-criterion-for-persistent-digital-entities-v0-1-1`.
- Remote home latest-post: ENTRY 0192, dated `2026-07-05`.
- Existing ENTRY 0187 remained immediately below the five new entries.
- Remote top order:
  1. `2026-07-05` / `entity-vs-profile-a-witness-root-custody-criterion-for-persistent-digital-entities-v0-1-1`
  2. `2026-07-04` / `how-to-install-c`
  3. `2026-07-03` / `varfloor-package-b-v0-1`
  4. `2026-07-02` / `varfloor-package-a-v0-1`
  5. `2026-07-01` / `i-think-we-are-misnaming-what-is-happening-in-ai`
  6. `2026-06-30` / `a-small-external-comment-turned-into-a-useful-control-layer-correction`
- No remote index item dated `2026-07-06` or `2026-07-07`: pass.

## Regression and Content Checks

- V23 date-only meta fix: pass.
- V28 five-entry preview fix: pass; remote `/diary/` latest preview has `5` entry cards.
- ENTRY 0189 and ENTRY 0190 image-less without placeholders: pass.
- Three image assets reproduce their source SHA-256 hashes: pass.
- ENTRY 0188 misnaming/bubble/infrastructure-of-continuity text: pass.
- ENTRY 0189 DOI/publication links: pass.
- ENTRY 0190 DOI/publication links and license split: pass.
- ENTRY 0191 install-c link and transition sequence: pass.
- ENTRY 0192 reader/DOI/Zenodo/GitHub link surfaces and custody criterion: pass.
- Supplied clickable source-link surfaces: `9/9`.
- Duplicate import check: each new slug occurs exactly once in the remote index.
- Remote `sitemap.xml` includes all five V55 entry URLs and all 34 affected tag URLs: `39/39` pass.

## Sitemap

- Builder automatic sitemap update: no.
- Manual narrow sitemap repair: yes.
- Missing URLs added before deployment: `15` (`5` entries plus `10` newly required tag URLs).
- URLs removed: `0`.

## Manual Remainder

Submit URLs from `SEARCH_CONSOLE_SUBMISSION_PLAN_V55.md` to Search Console. No Search Console submission is claimed by this run.
