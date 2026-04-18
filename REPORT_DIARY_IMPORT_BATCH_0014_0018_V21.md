# Report - Diary Import Batch 0014 0018 V21

Date: 2026-04-18
Contract ID: `SITE_DIARY_IMPORT_BATCH_0014_0018_V21`
Mode: `CODEX EXECUTION CONTRACT`

## Preflight

Confirmed before any write:

- repo exists and is a git repository
- current branch was `main`
- `origin` resolved to `https://github.com/Kot141078/kot141078.github.io.git`
- note on remote comparison: the returned origin includes the optional `.git` suffix while pointing to the same GitHub repository identity named in the contract
- working tree was clean
- `DIARY_IMPORT_PROTOCOL.md` exists
- `DIARY_IMPORT_CHECKLIST.md` exists
- `content/diary/` exists
- diary pipeline files and outputs already used by the repo exist
- `C:\Users\kotov\Downloads\11.jpg` exists and is readable
- `C:\Users\kotov\Downloads\12.jpg` exists and is readable
- `C:\Users\kotov\Downloads\13.jpg` exists and is readable
- `C:\Users\kotov\Downloads\14.jpg` exists and is readable
- same-date ordering behavior was confirmed from `tools/build_diary.py`: reverse sort by `(date, slug)`
- pre-import latest visible diary entry was `why-id-put-an-ai-rack-in-my-garage`
- no-hashtag handling was confirmed from `DIARY_IMPORT_PROTOCOL.md`: tags must come from the user or explicit source labels already present in the batch, so post `0017` must remain untagged

## Resolved titles and slugs

### Post 0014

- resolved title: `Why visual perception matters only after memory exists`
- justification: the source title was absent, so the title was derived conservatively from the strongest factual clause inside the first title-like source line
- final slug: `why-visual-perception-matters-only-after-memory-exists`

### Post 0015

- resolved title: `How AI Should Live With Humans (When the World Is Already in Crisis)`
- justification: the source title was absent, so the title was derived conservatively from the first full title-like source line
- final slug: `how-ai-should-live-with-humans-when-the-world-is-already-in-crisis`

### Post 0016

- resolved title: `Why Thinking AI Won't Take Over the World`
- justification: the source title was absent, so the title was derived conservatively from the principal clause of the first title-like source line
- final slug: `why-thinking-ai-wont-take-over-the-world`

### Post 0017

- resolved title: `Reality-Bound AI (L4) - public release v1.2.0`
- justification: the source title was absent, so the title was derived conservatively from the opening release sentence by extracting the explicit release object and version without adding new claims
- final slug: `reality-bound-ai-l4-public-release-v1-2-0`

### Post 0018

- resolved title: `A home robot is not a box with a ribbon`
- justification: the source title was absent, so the title was derived conservatively from the first title-like source sentence
- final slug: `a-home-robot-is-not-a-box-with-a-ribbon`

## Final tags

- `0014`: `AI Architecture`, `AI Safety`, `L4 Boundary`, `Cybernetics`, `Complex Systems`, `AGI`, `Advanced Global Intelligence`, `Human AI`, `Protocol Design`, `Deep Tech`
- `0015`: `AI Architecture`, `AI Safety`, `L4 Boundary`, `Cybernetics`, `Complex Systems`, `AGI`, `Advanced Global Intelligence`, `Human AI`, `Protocol Design`, `Deep Tech`
- `0016`: `AI Architecture`, `AI Safety`, `L4 Boundary`, `Cybernetics`, `Complex Systems`, `AGI`, `Advanced Global Intelligence`, `Human AI`, `Deep Tech`
- `0017`: no tags
- `0018`: `AI Architecture`, `Human AI`, `L4`, `Privacy by Design`, `Affective Systems`, `Future of Living`, `Cybernetics`, `Decentralized AI`

## Exact image handling

- `0014`: copied `C:\Users\kotov\Downloads\11.jpg` to `assets/diary/why-visual-perception-matters-only-after-memory-exists/cover.jpg`
- `0015`: copied `C:\Users\kotov\Downloads\12.jpg` to `assets/diary/how-ai-should-live-with-humans-when-the-world-is-already-in-crisis/cover.jpg`
- `0016`: copied `C:\Users\kotov\Downloads\13.jpg` to `assets/diary/why-thinking-ai-wont-take-over-the-world/cover.jpg`
- `0017`: remained image-less; `primary_image:` and `image_alt:` were kept empty
- `0018`: copied `C:\Users\kotov\Downloads\14.jpg` to `assets/diary/a-home-robot-is-not-a-box-with-a-ribbon/cover.jpg`
- no placeholder or fake image was added anywhere
- no source image in `Downloads` was mutated

## Exact alt handling

- `0014`: `Illustration of a glowing blue geometric structure rising from a rock on a wooden table in a sunlit room.`
- `0015`: `Black-and-white image of a hand above a smartphone on a desk, with glowing network lines across the hand and screen.`
- `0016`: `Image of a transparent panel labeled Memory, History, Cost, Constraints, and Risk on a rainy windowsill beside a mug overlooking a city.`
- `0017`: none, because the entry is intentionally image-less
- `0018`: `Image of a glowing cube-like device with cables on a workbench, with a humanoid robot in the background.`

## Same-date ordering

The builder tie-break remains reverse sort by `(date, slug)`, so the final same-date order is deterministic:

- `2026-01-09`: `why-visual-perception-matters-only-after-memory-exists | how-ai-should-live-with-humans-when-the-world-is-already-in-crisis`
- `2026-01-10`: `why-thinking-ai-wont-take-over-the-world | reality-bound-ai-l4-public-release-v1-2-0`

Latest-post effect:

- pre-import latest: `why-id-put-an-ai-rack-in-my-garage`
- post-import latest: `a-home-robot-is-not-a-box-with-a-ribbon`

## Explicit normalization notes

- `0015` malformed hashtag note: the malformed raw token ending in `Cybernetics.` was normalized to the clean tag `Cybernetics` only; no polluted punctuation tag was emitted in HTML, JSON, RSS, or sitemap outputs
- `0017` no-hashtag note: `DIARY_IMPORT_PROTOCOL.md` requires tags to come from explicit source labels already present in the batch; the source packet for `0017` provided none, so the entry was kept untagged and no inferred tag pack was created
- `0017` inline-link note: the GitHub release URL was preserved as a normal Markdown link in the diary body and renders as a normal anchor on the public page

## Updated surfaces

- `/diary/`
- `/diary/archive/`
- `/diary/tags/`
- five new entry pages
- existing affected tag pages
- new tag pages created by the batch
- home latest-post slot in `/`
- `diary-index.json`
- `diary-latest.json`
- `diary-tags.json`
- `diary-feed.xml`
- `sitemap.xml`

## New entry URLs

- `https://ivankotov.eu/diary/why-visual-perception-matters-only-after-memory-exists/`
- `https://ivankotov.eu/diary/how-ai-should-live-with-humans-when-the-world-is-already-in-crisis/`
- `https://ivankotov.eu/diary/why-thinking-ai-wont-take-over-the-world/`
- `https://ivankotov.eu/diary/reality-bound-ai-l4-public-release-v1-2-0/`
- `https://ivankotov.eu/diary/a-home-robot-is-not-a-box-with-a-ribbon/`

## Affected tag page URLs

- `https://ivankotov.eu/diary/tags/ai-architecture/`
- `https://ivankotov.eu/diary/tags/ai-safety/`
- `https://ivankotov.eu/diary/tags/l4-boundary/`
- `https://ivankotov.eu/diary/tags/cybernetics/`
- `https://ivankotov.eu/diary/tags/complex-systems/`
- `https://ivankotov.eu/diary/tags/agi/`
- `https://ivankotov.eu/diary/tags/advanced-global-intelligence/`
- `https://ivankotov.eu/diary/tags/deep-tech/`
- `https://ivankotov.eu/diary/tags/decentralized-ai/`
- `https://ivankotov.eu/diary/tags/affective-systems/`
- `https://ivankotov.eu/diary/tags/human-ai/`
- `https://ivankotov.eu/diary/tags/protocol-design/`
- `https://ivankotov.eu/diary/tags/l4/`
- `https://ivankotov.eu/diary/tags/privacy-by-design/`
- `https://ivankotov.eu/diary/tags/future-of-living/`

## Validation outcomes

Local validation passed:

- each new entry page was generated
- each imaged entry rendered its intended supplied image
- `0017` rendered without image and without `og:image`
- `/diary/`, `/diary/archive/`, and `/diary/tags/` include the new batch
- relevant tag pages contain the expected posts
- `diary-index.json count` = `18`
- `diary-tags.json` contains the expected updated tag counts
- `diary-feed.xml` contains all five new posts
- `sitemap.xml` was synchronized manually because the diary builder does not manage sitemap
- home latest-post changed to `a-home-robot-is-not-a-box-with-a-ribbon`
- previous entries remain intact
- no fake image or placeholder was introduced
- `0017` preserved the inline GitHub release link
- no polluted `Cybernetics.` tag exists
- no `untagged` tag page was generated

Live validation passed on first check:

- all required URLs returned `200`
- home latest points to `a-home-robot-is-not-a-box-with-a-ribbon`
- `0017` remains image-less on the live site
- live same-date order matches local generated order
- live `diary-index.json`, `diary-tags.json`, `diary-feed.xml`, and `sitemap.xml` all reflect the V21 import

Key live tag counts:

- `ai-architecture`: `10`
- `ai-safety`: `7`
- `l4-boundary`: `9`
- `cybernetics`: `11`
- `complex-systems`: `4`
- `agi`: `7`
- `advanced-global-intelligence`: `4`
- `human-ai`: `4`
- `protocol-design`: `2`
- `deep-tech`: `8`
- `l4`: `1`
- `privacy-by-design`: `1`
- `affective-systems`: `2`
- `future-of-living`: `1`
- `decentralized-ai`: `2`

## Manual Search Console submission list

- `https://ivankotov.eu/`
- `https://ivankotov.eu/diary/`
- `https://ivankotov.eu/diary/archive/`
- `https://ivankotov.eu/diary/tags/`
- `https://ivankotov.eu/diary/why-visual-perception-matters-only-after-memory-exists/`
- `https://ivankotov.eu/diary/how-ai-should-live-with-humans-when-the-world-is-already-in-crisis/`
- `https://ivankotov.eu/diary/why-thinking-ai-wont-take-over-the-world/`
- `https://ivankotov.eu/diary/reality-bound-ai-l4-public-release-v1-2-0/`
- `https://ivankotov.eu/diary/a-home-robot-is-not-a-box-with-a-ribbon/`
- `https://ivankotov.eu/diary/tags/ai-architecture/`
- `https://ivankotov.eu/diary/tags/ai-safety/`
- `https://ivankotov.eu/diary/tags/l4-boundary/`
- `https://ivankotov.eu/diary/tags/cybernetics/`
- `https://ivankotov.eu/diary/tags/complex-systems/`
- `https://ivankotov.eu/diary/tags/agi/`
- `https://ivankotov.eu/diary/tags/advanced-global-intelligence/`
- `https://ivankotov.eu/diary/tags/deep-tech/`
- `https://ivankotov.eu/diary/tags/decentralized-ai/`
- `https://ivankotov.eu/diary/tags/affective-systems/`
- `https://ivankotov.eu/diary/tags/human-ai/`
- `https://ivankotov.eu/diary/tags/protocol-design/`
- `https://ivankotov.eu/diary/tags/l4/`
- `https://ivankotov.eu/diary/tags/privacy-by-design/`
- `https://ivankotov.eu/diary/tags/future-of-living/`

## Commit hashes

- implementation commit: `998608d9d001c7a3f45493a071b23202d114a2f4`
- report artifact commit: recorded in the final console git block because this report file is part of that commit

## Final clean-tree confirmation

- the working tree was clean before V21 started
- the implementation working tree was clean immediately after the implementation push
- final post-report clean-tree confirmation is recorded in the final console git block after the report artifact commit
