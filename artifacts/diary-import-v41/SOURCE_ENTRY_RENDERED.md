# SOURCE_ENTRY_RENDERED

## Batch

- Contract namespace executed: `SITE_DIARY_IMPORT_BATCH_0109_0113_V41`
- Implementation commit: `8f272426ef5071eb81788e65064c0278e5391650`
- Same-date rule used: newest date first, then slug descending
- Expected latest-post after import: `there-is-a-difference-between-digital-immortality-and-what-i-would-call-post-anchor-continuity`
- Slug collision note: `0112` collided with an older existing entry and therefore used `a-new-public-layer-is-now-part-of-the-corpus-0112`
- Sitemap update path note: manual narrow repair required again because the build step did not update `sitemap.xml`
- Normalization note: stale V40 artifact/marker references inside the contract were normalized to V41 so V40 outputs would not be overwritten

## POST 0109

- Resolved title: `Most AI economy talk is still pricing the wrong thing.`
- Resolved slug: `most-ai-economy-talk-is-still-pricing-the-wrong-thing`
- Resolved tags: `AI`, `AI Economy`, `Experience Artifacts`, `Verification`, `Provenance`, `Trust`, `AI Architecture`, `Systems Engineering`, `Auditability`, `Traceability`, `Operational AI`, `Risk Management`, `Cost Of Error`, `Signal Vs Noise`, `Information Economy`, `Constraint Driven`, `Reality Bound`, `L4`, `Advanced Global Intelligence`
- Image handling: `100.jpg` -> `assets/diary/most-ai-economy-talk-is-still-pricing-the-wrong-thing/cover.jpg`
- Alt text: `An industrial paper-processing machine with a conveyor full of paper and compressed paper bundles on a platform nearby.`
- Link/DOI note: GitHub URL preserved as a clickable anchor; Zenodo short link preserved as a clickable anchor
- Structure note: repeated bullet blocks preserved; `Economic Layer for Experience Artifacts` preserved as a heading-like section marker

## POST 0110

- Resolved title: `I watched the interview with Roman Yampolskiy.`
- Resolved slug: `i-watched-the-interview-with-roman-yampolskiy`
- Resolved tags: `AI`, `AI Safety`, `AGI`, `Advanced Global Intelligence`, `SystemArchitec`
- Image handling: `101.jpg` -> `assets/diary/i-watched-the-interview-with-roman-yampolskiy/cover.jpg`
- Alt text: `A large humanoid robot looming over a podium in a dark auditorium filled with seated people.`
- Malformed/truncated hashtag note: raw source hashtag `SystemArchitec` preserved literally; no guessed repair performed
- Link/DOI note: no inline external links in source
- Structure note: quoted dialogue block preserved without raw `>` leakage in rendered HTML; final three-step cycle preserved as separate paragraph blocks

## POST 0111

- Resolved title: `There is a difference between "digital immortality" and what I would call post-anchor continuity.`
- Resolved slug: `there-is-a-difference-between-digital-immortality-and-what-i-would-call-post-anchor-continuity`
- Resolved tags: `AI Architecture`, `Continuity`, `L4`, `Digital Entities`, `Cybernetics`, `Human AI`, `Advanced Global Intelligence`
- Image handling: `102.jpg` -> `assets/diary/there-is-a-difference-between-digital-immortality-and-what-i-would-call-post-anchor-continuity/cover.jpg`
- Alt text: `Ripples crossing calm water between dark tree-lined shores under a pale sky.`
- Structure note: `c = a + b`, bare `a`, bare `c`, `Earth paragraph:`, and contrasted question block all preserved cleanly

## POST 0112

- Resolved title: `A new public layer is now part of the corpus.`
- Resolved slug: `a-new-public-layer-is-now-part-of-the-corpus-0112`
- Resolved tags: `AI`, `AI Safety`, `AI Architecture`, `Cybernetics`, `L4`, `Advanced Global Intelligence`, `Systems Thinking`, `Audit Trail`
- Image handling: `103.jpg` -> `assets/diary/a-new-public-layer-is-now-part-of-the-corpus-0112/cover.jpg`
- Alt text: `A person under a desk lamp reaching toward two glass dishes on a table in a dim room.`
- Link/DOI note: GitHub URL preserved as a clickable anchor; DOI short link preserved as a clickable anchor
- Slug-collision note: older `a-new-public-layer-is-now-part-of-the-corpus` remained untouched; new V41 post used deterministic `-0112` suffix
- Structure note: `Earth paragraph:` preserved; `AGL — Actor Grounding Layer` preserved exactly

## POST 0113

- Resolved title: `In the end, I do not think the future of AI will be decided only by model size, orchestration patterns, or benchmark performance.`
- Resolved slug: `in-the-end-i-do-not-think-the-future-of-ai-will-be-decided-only-by-model-size-orchestration-patterns-or-benchmark-performance`
- Resolved tags: `AI`, `Advanced Global Intelligence`, `Human Centered AI`, `Cybernetics`, `L4`, `Domestic Infrastructure`, `Long Lived AI`, `AI Architecture`
- Image handling: `104.jpg` -> `assets/diary/in-the-end-i-do-not-think-the-future-of-ai-will-be-decided-only-by-model-size-orchestration-patterns-or-benchmark-performance/cover.jpg`
- Alt text: `A warm home interior with a steaming mug on a table and a softly lit sofa in the background.`
- Link/DOI note: ARL normative and implementation short links preserved as clickable anchors; DOI preserved visibly as `10.5281/zenodo.19406479` and linked through `doi.org`
- Structure note: `Livable.` preserved as a standalone emphasis block; ARL / Normative / Implementation / Zenodo sections preserved

## Deterministic Ordering Decisions

- `2026-04-16`: `the-quiet-upgrade-in-arq-v0-2-is-model-discipline` > `most-ai-economy-talk-is-still-pricing-the-wrong-thing` > `i-watched-the-interview-with-roman-yampolskiy`
- `2026-04-17`: `there-is-a-difference-between-digital-immortality-and-what-i-would-call-post-anchor-continuity` > `in-the-end-i-do-not-think-the-future-of-ai-will-be-decided-only-by-model-size-orchestration-patterns-or-benchmark-performance` > `a-new-public-layer-is-now-part-of-the-corpus-0112`
- Latest-post effect: home latest-post changes from `the-quiet-upgrade-in-arq-v0-2-is-model-discipline` to `there-is-a-difference-between-digital-immortality-and-what-i-would-call-post-anchor-continuity`
- Preview policy note: `/diary/` still shows only the five newest visible entries under the V28 baseline, so `0110` remains present in archive/metadata outputs but not in the `/diary/` five-entry preview
