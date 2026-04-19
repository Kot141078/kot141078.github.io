# POST_DEPLOY_CHECK

## Deployment Result

- Implementation commit pushed: `9667c950ab75eaeabe5739dbff7d1271016826d6`
- Live convergence result: pass
- Attempts needed: `1`
- Total remote checks passed: `37`

## Live Surface Checks

- `https://ivankotov.eu/` -> `200`; latest-post now points to `the-english-pdf-edition-of-qubit-of-hope-volume-ii-is-now-available-in-the-public-repository`: pass
- `https://ivankotov.eu/diary/` -> `200`; visible V28 five-entry preview includes `0117`, `0115`, `0114`, `0116`, and prior `0111`: pass
- `https://ivankotov.eu/diary/archive/` -> `200`; all four V42 entries present: pass
- `https://ivankotov.eu/diary/tags/` -> `200`; includes the new `English Edition` tag and updated existing tag memberships: pass

## Entry Pages

- `https://ivankotov.eu/diary/a-mature-ai-entity-should-not-pull-a-human-away-from-other-humans/` -> `200`: pass
- `https://ivankotov.eu/diary/if-digital-entities-ever-become-a-civilization-they-will-not-enter-earth-as-its-oldest-intelligence/` -> `200`: pass
- `https://ivankotov.eu/diary/there-is-a-difference-between-digital-immortality-and-what-i-would-call-post-anchor-continuity-0116/` -> `200`: pass
- `https://ivankotov.eu/diary/the-english-pdf-edition-of-qubit-of-hope-volume-ii-is-now-available-in-the-public-repository/` -> `200`: pass

## Repeated Source Safety

- Older entry `https://ivankotov.eu/diary/there-is-a-difference-between-digital-immortality-and-what-i-would-call-post-anchor-continuity/` still returns `200`: pass
- New V42 repeated-source entry `https://ivankotov.eu/diary/there-is-a-difference-between-digital-immortality-and-what-i-would-call-post-anchor-continuity-0116/` returns `200`: pass

## Affected Tag Pages

- `https://ivankotov.eu/diary/tags/ai-entities/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/human-centered-ai/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/cybernetics/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/soft-safety/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/l4/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/future-of-living/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/ai-architecture/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/coexistence/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/systems-thinking/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/advanced-global-intelligence/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/human-ai/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/continuity/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/digital-entities/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/qubit-of-hope/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/english-edition/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/book-release/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/literary-fiction/` -> `200`: pass

## Machine-Readable Surfaces

- `https://ivankotov.eu/diary-index.json` -> `200`; count `117`: pass
- `https://ivankotov.eu/diary-latest.json` -> `200`; latest slug is `the-english-pdf-edition-of-qubit-of-hope-volume-ii-is-now-available-in-the-public-repository`: pass
- `https://ivankotov.eu/diary-tags.json` -> `200`; contains `english-edition`, `qubit-of-hope`, `book-release`, and `literary-fiction`: pass
- `https://ivankotov.eu/diary-feed.xml` -> `200`; contains the four V42 entry slugs: pass
- `https://ivankotov.eu/sitemap.xml` -> `200`; contains the four V42 entry URLs and the V42 `english-edition` tag URL: pass

## Asset Checks

- `https://ivankotov.eu/assets/diary/a-mature-ai-entity-should-not-pull-a-human-away-from-other-humans/cover.jpg` -> `200`: pass
- `https://ivankotov.eu/assets/diary/if-digital-entities-ever-become-a-civilization-they-will-not-enter-earth-as-its-oldest-intelligence/cover.jpg` -> `200`: pass
- `https://ivankotov.eu/assets/diary/there-is-a-difference-between-digital-immortality-and-what-i-would-call-post-anchor-continuity-0116/cover.jpg` -> `200`: pass
- `https://ivankotov.eu/assets/diary/i-watched-the-interview-with-roman-yampolskiy/cover.jpg` -> `200`; reused-source-image baseline remained intact: pass
- `https://ivankotov.eu/assets/diary/there-is-a-difference-between-digital-immortality-and-what-i-would-call-post-anchor-continuity/cover.jpg` -> `200`; older repeated-source baseline remained intact: pass

## Baseline Checks

- V23 date-only meta rendering remained intact live: pass
- V28 five-entry preview remained intact live: pass
- `0117` stayed image-less live and no placeholder surfaced: pass
- No fake or placeholder image surfaced live: pass
