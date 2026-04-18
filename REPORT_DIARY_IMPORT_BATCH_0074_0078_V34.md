# REPORT_DIARY_IMPORT_BATCH_0074_0078_V34

## Contract

- Contract: `SITE_DIARY_IMPORT_BATCH_0074_0078_V34`
- Repo: `C:\Users\kotov\Desktop\AGI\kot141078.github.io`
- Branch: `main`
- Scope: Diary import only
- Implementation commit: `c4e968350bdc0a47ff270b1e4197f4816f42015b`
- Report artifacts commit: self-referential at authoring time; captured in the final console block after the report commit is created

## Preflight

- Repo exists and is a git repository: `PASS`
- Current branch is `main`: `PASS`
- `origin` resolves to `https://github.com/Kot141078/kot141078.github.io.git`
  - same canonical repository as the contract target, with the conventional `.git` suffix
- Working tree was clean before any write: `PASS`
- `DIARY_IMPORT_PROTOCOL.md` exists: `PASS`
- `DIARY_IMPORT_CHECKLIST.md` exists: `PASS`
- `content/diary/` exists: `PASS`
- Current diary build outputs already existed in repo root: `diary-index.json`, `diary-latest.json`, `diary-tags.json`, `diary-feed.xml`, `sitemap.xml`
- Source images passed existence/readability checks:
  - `C:\Users\kotov\Downloads\68.jpg`
  - `C:\Users\kotov\Downloads\69.jpg`
  - `C:\Users\kotov\Downloads\70.jpg`
  - `C:\Users\kotov\Downloads\71.jpg`
- `POST 0076` was confirmed intentionally image-less: `PASS`
- Pre-import diary count: `73`
- Pre-import latest slug: `this-is-not-a-studio-render`
- Ordering baseline before import:
  - builder sorts by `(date, slug)` with `reverse=True`
  - same-date tie-breaker is therefore deterministic by slug
- V23 date-only meta rendering fix was intact in the pre-import baseline: `PASS`
- V28 preview-size baseline check surfaced a regression in the current builder:
  - `render_latest_entries()` had drifted back to `entries[:3]`
  - this would have violated the V34 success criteria
  - a narrow follow-up repair was therefore applied in `tools/build_diary.py`, restoring the latest section to `entries[:5]`
  - the repair was rebuilt and revalidated locally and live
- Protocol rule used for `POST 0076` no-hashtag case:
  - protocol forbids inventing tags
  - the entry remained untagged
- Protocol rule used for `POST 0075` awkward hashtag case:
  - raw source label `Trusts` is awkward, but not clearly broken and still normalizes to valid ASCII slug `trusts`
  - protocol forbids silent semantic repair
  - the tag was preserved literally as `Trusts`
- Slug collision inspection result:
  - deterministic collision precedent exists in repo (`-0029`, `-0057`, `-0068`)
  - V34 did not require collision suffixing

## Per-Post Resolution

### POST 0074

- Resolved title: `Agents are not the subject.`
  - justification: first clear factual heading line in source text
- Final slug: `agents-are-not-the-subject`
- Final tags: `AI Architecture`, `Cybernetics`, `Continuity`, `Sovereign AI`, `Advanced Global Intelligence`
- Image handling:
  - source: `C:\Users\kotov\Downloads\68.jpg`
  - final asset: `assets/diary/agents-are-not-the-subject/cover.jpg`
- Alt handling:
  - `Rows of humanoid robots at desks facing a large glowing screen with the letter C in a dark blue control room.`
- Structure preserved:
  - backticked `c = a + b`
  - backticked `c`
  - DOI block as visible citation text

### POST 0075

- Resolved title: `A good AI should be difficult to manipulate - even by its owner`
  - justification: first clear factual heading line in source text
- Final slug: `a-good-ai-should-be-difficult-to-manipulate-even-by-its-owner`
- Final tags:
  - `AGI`
  - `Advanced Global Intelligence`
  - `AI Ethics`
  - `AI Architecture`
  - `Human Centered AI`
  - `Cybernetics`
  - `Digital Identity`
  - `Long Term Memory`
  - `Coexistence`
  - `AI Safety`
  - `Systems Thinking`
  - `L4`
  - `Sovereign AI`
  - `Future of AI`
  - `Trusts`
- Awkward hashtag handling:
  - raw source `Trusts` preserved literally
  - normalized tag slug: `trusts`
- Image handling:
  - source: `C:\Users\kotov\Downloads\69.jpg`
  - final asset: `assets/diary/a-good-ai-should-be-difficult-to-manipulate-even-by-its-owner/cover.jpg`
- Alt handling:
  - `Red pixelated hands reaching toward a glass cube that contains a glowing white branching network.`
- Structure preserved:
  - both quoted question blocks
  - owner-capture contrast
  - compass analogy

### POST 0076

- Resolved title: `ARQ is now published on Zenodo.`
  - justification: first clear factual heading line in source text
- Final slug: `arq-is-now-published-on-zenodo`
- Final tags: none
- No-hashtag protocol handling:
  - source packet contained no explicit hashtags
  - protocol forbids invented tags
  - final front matter kept `tags:` empty
- Image handling:
  - intentionally image-less
  - `primary_image:` empty
  - `image_alt:` empty
- Structure preserved:
  - DOI block
  - bridge line `correction logic -> SER continuity -> L4 bounded accountability`
  - inline GitHub reading-context link kept as a normal usable link

### POST 0077

- Resolved title: `Most people look at AI systems from the outside.`
  - justification: first clear factual heading line in source text
- Final slug: `most-people-look-at-ai-systems-from-the-outside`
- Final tags: `Continuity`, `AI Architecture`, `Sovereign AI`, `Advanced Global Intelligence`, `L4`
- Image handling:
  - source: `C:\Users\kotov\Downloads\70.jpg`
  - final asset: `assets/diary/most-people-look-at-ai-systems-from-the-outside/cover.jpg`
- Alt handling:
  - `A glowing humanoid figure suspended in a dark room and surrounded by robotic arms and floating components.`
- Structure preserved:
  - single-word emphasis paragraph `Presence.`
  - backticked `c = a + b`

### POST 0078

- Resolved title: `A lot of AI discussion still assumes the main demand will come from offices:`
  - justification: first clear factual heading line in source text
- Final slug: `a-lot-of-ai-discussion-still-assumes-the-main-demand-will-come-from-offices`
- Final tags:
  - `AGI`
  - `Advanced Global Intelligence`
  - `AI Architecture`
  - `Human Centered AI`
  - `Local AI`
  - `Private AI`
  - `Domestic Engineering`
  - `Home AI`
  - `Future of Living`
  - `Cybernetics`
  - `Systems Thinking`
  - `Cognitive Infrastructure`
  - `Digital Continuity`
  - `L4`
  - `Future of AI`
- Image handling:
  - source: `C:\Users\kotov\Downloads\71.jpg`
  - final asset: `assets/diary/a-lot-of-ai-discussion-still-assumes-the-main-demand-will-come-from-offices/cover.jpg`
- Alt handling:
  - `A wall-mounted device and control panel in a home kitchen nook with glowing lines reaching toward a phone and tablet.`
- Structure preserved:
  - office/home contrast block
  - household question block
  - domestic-infrastructure analogy

## Same-Date Ordering

- Same-date group: `2026-03-25`
- Final slugs in that group:
  - `arq-is-now-published-on-zenodo`
  - `a-good-ai-should-be-difficult-to-manipulate-even-by-its-owner`
- Deterministic explanation:
  - builder sorts by `(date, slug)` descending
  - `arq-is-now-published-on-zenodo` sorts ahead of `a-good-ai-should-be-difficult-to-manipulate-even-by-its-owner`

## Latest-Post Effect

- Home latest-post changed: `YES`
- Previous latest slug: `this-is-not-a-studio-render`
- New latest slug: `a-lot-of-ai-discussion-still-assumes-the-main-demand-will-come-from-offices`

## Files and Assets Written

- New source entries:
  - `content/diary/2026-03-24-agents-are-not-the-subject.md`
  - `content/diary/2026-03-25-a-good-ai-should-be-difficult-to-manipulate-even-by-its-owner.md`
  - `content/diary/2026-03-25-arq-is-now-published-on-zenodo.md`
  - `content/diary/2026-03-26-most-people-look-at-ai-systems-from-the-outside.md`
  - `content/diary/2026-03-27-a-lot-of-ai-discussion-still-assumes-the-main-demand-will-come-from-offices.md`
- New asset paths:
  - `assets/diary/agents-are-not-the-subject/cover.jpg`
  - `assets/diary/a-good-ai-should-be-difficult-to-manipulate-even-by-its-owner/cover.jpg`
  - `assets/diary/most-people-look-at-ai-systems-from-the-outside/cover.jpg`
  - `assets/diary/a-lot-of-ai-discussion-still-assumes-the-main-demand-will-come-from-offices/cover.jpg`
- Builder repair:
  - `tools/build_diary.py`
  - latest preview restored from `entries[:3]` to `entries[:5]`
- Regenerated surfaces and metadata:
  - `/diary/`
  - `/diary/archive/`
  - `/diary/tags/`
  - five new entry pages
  - affected tag pages
  - `diary-index.json`
  - `diary-latest.json`
  - `diary-tags.json`
  - `diary-feed.xml`
  - `sitemap.xml`
  - home latest-post slot in `index.html`

## New Entry URLs

- `https://ivankotov.eu/diary/agents-are-not-the-subject/`
- `https://ivankotov.eu/diary/a-good-ai-should-be-difficult-to-manipulate-even-by-its-owner/`
- `https://ivankotov.eu/diary/arq-is-now-published-on-zenodo/`
- `https://ivankotov.eu/diary/most-people-look-at-ai-systems-from-the-outside/`
- `https://ivankotov.eu/diary/a-lot-of-ai-discussion-still-assumes-the-main-demand-will-come-from-offices/`

## Affected Tag Pages

- `https://ivankotov.eu/diary/tags/ai-architecture/`
- `https://ivankotov.eu/diary/tags/cybernetics/`
- `https://ivankotov.eu/diary/tags/continuity/`
- `https://ivankotov.eu/diary/tags/sovereign-ai/`
- `https://ivankotov.eu/diary/tags/advanced-global-intelligence/`
- `https://ivankotov.eu/diary/tags/agi/`
- `https://ivankotov.eu/diary/tags/ai-ethics/`
- `https://ivankotov.eu/diary/tags/human-centered-ai/`
- `https://ivankotov.eu/diary/tags/digital-identity/`
- `https://ivankotov.eu/diary/tags/long-term-memory/`
- `https://ivankotov.eu/diary/tags/coexistence/`
- `https://ivankotov.eu/diary/tags/ai-safety/`
- `https://ivankotov.eu/diary/tags/systems-thinking/`
- `https://ivankotov.eu/diary/tags/l4/`
- `https://ivankotov.eu/diary/tags/future-of-ai/`
- `https://ivankotov.eu/diary/tags/trusts/`
- `https://ivankotov.eu/diary/tags/local-ai/`
- `https://ivankotov.eu/diary/tags/private-ai/`
- `https://ivankotov.eu/diary/tags/domestic-engineering/`
- `https://ivankotov.eu/diary/tags/home-ai/`
- `https://ivankotov.eu/diary/tags/future-of-living/`
- `https://ivankotov.eu/diary/tags/cognitive-infrastructure/`
- `https://ivankotov.eu/diary/tags/digital-continuity/`

## Validation Outcomes

### Local

- Build command: `python tools/build_diary.py`
- Result: `PASS`
- Diary count: `78`
- Latest slug: `a-lot-of-ai-discussion-still-assumes-the-main-demand-will-come-from-offices`
- Same-date `2026-03-25` order: `arq-is-now-published-on-zenodo` -> `a-good-ai-should-be-difficult-to-manipulate-even-by-its-owner`
- `/diary/` latest preview count after repair: `5`
- `/diary/` latest preview slugs:
  - `a-lot-of-ai-discussion-still-assumes-the-main-demand-will-come-from-offices`
  - `most-people-look-at-ai-systems-from-the-outside`
  - `arq-is-now-published-on-zenodo`
  - `a-good-ai-should-be-difficult-to-manipulate-even-by-its-owner`
  - `agents-are-not-the-subject`
- V23 date-only meta rendering still intact: `PASS`
- V28 preview-size fix restored and now intact: `PASS`
- `POST 0076` no-hashtag propagation consistent across content/page/JSON: `PASS`
- `POST 0075` literal `Trusts` propagation consistent across content/page/JSON: `PASS`
- No placeholder/fake image introduced: `PASS`
- Previously imported entry `this-is-not-a-studio-render` still exists: `PASS`
- New sitemap URLs were missing after build and were added explicitly: `PASS`

### Live

- Readiness poll attempts until latest slug matched: `1`
- Live URL checks: `41/41` returned `200`
- Live index count: `78`
- Live latest slug: `a-lot-of-ai-discussion-still-assumes-the-main-demand-will-come-from-offices`
- Live latest preview count on `/diary/`: `5`
- Live same-date `2026-03-25` order: `arq-is-now-published-on-zenodo` -> `a-good-ai-should-be-difficult-to-manipulate-even-by-its-owner`
- Live tag counts:
  - `AI Ethics = 1`
  - `Trusts = 1`
  - `Home AI = 1`
  - `Digital Continuity = 1`
- `POST 0076` live page remained image-less and tag-less: `PASS`
- `POST 0074` DOI and `c = a + b` text survived rendering: `PASS`
- `POST 0075` quoted question block and `Trusts` tag survived rendering: `PASS`
- `POST 0076` DOI and inline GitHub link survived rendering: `PASS`
- `POST 0077` `Presence.` and `c = a + b` survived rendering: `PASS`
- `POST 0078` household question block survived rendering: `PASS`
- No fake placeholder image introduced live: `PASS`

## Manual Search Console Submission List

- `https://ivankotov.eu/`
- `https://ivankotov.eu/diary/`
- `https://ivankotov.eu/diary/archive/`
- `https://ivankotov.eu/diary/tags/`
- `https://ivankotov.eu/diary/agents-are-not-the-subject/`
- `https://ivankotov.eu/diary/a-good-ai-should-be-difficult-to-manipulate-even-by-its-owner/`
- `https://ivankotov.eu/diary/arq-is-now-published-on-zenodo/`
- `https://ivankotov.eu/diary/most-people-look-at-ai-systems-from-the-outside/`
- `https://ivankotov.eu/diary/a-lot-of-ai-discussion-still-assumes-the-main-demand-will-come-from-offices/`
- `https://ivankotov.eu/diary/tags/ai-ethics/`
- `https://ivankotov.eu/diary/tags/trusts/`
- `https://ivankotov.eu/diary/tags/home-ai/`
- `https://ivankotov.eu/diary/tags/digital-continuity/`

## Final Status

- All five posts imported as real entries: `PASS`
- Supplied-image rule respected: `PASS`
- `POST 0076` no-hashtag handling followed protocol exactly: `PASS`
- `POST 0075` awkward tag handling followed protocol exactly: `PASS`
- Slug collisions requiring suffixes: none in this batch
- No unrelated public layers changed beyond regenerated diary surfaces: `PASS`
- Working tree clean at report authoring time: pending final report-artifact commit
