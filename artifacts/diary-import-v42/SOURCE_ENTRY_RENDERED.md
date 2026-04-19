# SOURCE_ENTRY_RENDERED

## Batch

- Contract namespace executed: `SITE_DIARY_IMPORT_BATCH_0114_0117_V42`
- Implementation commit: `9667c950ab75eaeabe5739dbff7d1271016826d6`
- Same-date rule used: newest date first, then slug descending
- Expected latest-post after import: `the-english-pdf-edition-of-qubit-of-hope-volume-ii-is-now-available-in-the-public-repository`
- Reused-source-image note: `0115` reused source file `101.jpg`, but received a new slug-scoped asset root
- Repeated-source-URL note: `0116` reused an already-imported `linkedin_url` and therefore used deterministic separate-entry handling with `-0116`
- Image-less note: `0117` stays strictly image-less and becomes latest-post without a placeholder image
- Sitemap update path note: manual narrow repair required again because the build step did not update `sitemap.xml`

## POST 0114

- Resolved title: `A mature AI entity should not pull a human away from other humans.`
- Resolved slug: `a-mature-ai-entity-should-not-pull-a-human-away-from-other-humans`
- Resolved tags: `AI Entities`, `Human Centered AI`, `Cybernetics`, `Soft Safety`, `L4`, `Future of Living`, `AI Architecture`
- Image handling: `105.jpg` -> `assets/diary/a-mature-ai-entity-should-not-pull-a-human-away-from-other-humans/cover.jpg`
- Alt text: `A person seen from behind approaching an outdoor dinner table where several people are gathered in warm evening light.`
- Structure note: compact source cadence preserved without invented sectioning

## POST 0115

- Resolved title: `If digital entities ever become a civilization, they will not enter Earth as its oldest intelligence.`
- Resolved slug: `if-digital-entities-ever-become-a-civilization-they-will-not-enter-earth-as-its-oldest-intelligence`
- Resolved tags: `AI Architecture`, `Cybernetics`, `Coexistence`, `L4`, `Systems Thinking`, `Advanced Global Intelligence`, `Human AI`
- Image handling: `101.jpg` -> `assets/diary/if-digital-entities-ever-become-a-civilization-they-will-not-enter-earth-as-its-oldest-intelligence/cover.jpg`
- Alt text: `A large humanoid robot looming over a podium in a dark auditorium filled with seated people.`
- Asset safety note: older V41 asset path stayed intact while the reused source image was copied to a distinct slug-scoped V42 path

## POST 0116

- Resolved title: `There is a difference between "digital immortality" and what I would call post-anchor continuity.`
- Resolved slug: `there-is-a-difference-between-digital-immortality-and-what-i-would-call-post-anchor-continuity-0116`
- Resolved tags: `AI Architecture`, `Continuity`, `L4`, `Digital Entities`, `Cybernetics`, `Human AI`, `Advanced Global Intelligence`
- Image handling: `106.jpg` -> `assets/diary/there-is-a-difference-between-digital-immortality-and-what-i-would-call-post-anchor-continuity-0116/cover.jpg`
- Alt text: `A child and an older person's hands placing a stone into a rough stone wall outdoors.`
- Repeated-source note: builder has no uniqueness rule for `linkedin_url`, repo precedent already allows repeated `linkedin_url`, so `0116` stayed as a distinct entry instead of being silently merged into V41 `0111`

## POST 0117

- Resolved title: `The English PDF edition of Qubit of Hope — Volume II is now available in the public repository.`
- Resolved slug: `the-english-pdf-edition-of-qubit-of-hope-volume-ii-is-now-available-in-the-public-repository`
- Resolved tags: `Qubit of Hope`, `English Edition`, `Book Release`, `Literary Fiction`
- Image handling: none
- `primary_image`: empty
- `image_alt`: empty
- Rendering note: no cover image, no placeholder, and latest-post still resolves correctly

## Deterministic Ordering Decisions

- `2026-04-18`: `the-english-pdf-edition-of-qubit-of-hope-volume-ii-is-now-available-in-the-public-repository` > `if-digital-entities-ever-become-a-civilization-they-will-not-enter-earth-as-its-oldest-intelligence` > `a-mature-ai-entity-should-not-pull-a-human-away-from-other-humans`
- Latest-post effect: home latest-post changes from `there-is-a-difference-between-digital-immortality-and-what-i-would-call-post-anchor-continuity` to `the-english-pdf-edition-of-qubit-of-hope-volume-ii-is-now-available-in-the-public-repository`
- Preview policy note: `/diary/` still shows only the five newest visible entries under the V28 baseline, so the V42 visible set is `0117`, `0115`, `0114`, `0116`, and prior `0111`
