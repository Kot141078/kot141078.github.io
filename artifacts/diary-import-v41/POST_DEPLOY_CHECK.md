# POST_DEPLOY_CHECK

## Deployment Result

- Implementation commit pushed: `8f272426ef5071eb81788e65064c0278e5391650`
- Live convergence result: pass
- Attempts needed: `1`
- Total remote checks passed: `51`

## Live Surface Checks

- `https://ivankotov.eu/` -> `200`; latest-post now points to `there-is-a-difference-between-digital-immortality-and-what-i-would-call-post-anchor-continuity`: pass
- `https://ivankotov.eu/diary/` -> `200`; visible V28 five-entry preview includes `0111`, `0113`, `0112`, `0108`, `0109`: pass
- `https://ivankotov.eu/diary/archive/` -> `200`; all five V41 entries present: pass
- `https://ivankotov.eu/diary/tags/` -> `200`; includes new tag names such as `Experience Artifacts`, `SystemArchitec`, and `Domestic Infrastructure`: pass

## Entry Pages

- `https://ivankotov.eu/diary/most-ai-economy-talk-is-still-pricing-the-wrong-thing/` -> `200`: pass
- `https://ivankotov.eu/diary/i-watched-the-interview-with-roman-yampolskiy/` -> `200`: pass
- `https://ivankotov.eu/diary/there-is-a-difference-between-digital-immortality-and-what-i-would-call-post-anchor-continuity/` -> `200`: pass
- `https://ivankotov.eu/diary/a-new-public-layer-is-now-part-of-the-corpus-0112/` -> `200`: pass
- `https://ivankotov.eu/diary/in-the-end-i-do-not-think-the-future-of-ai-will-be-decided-only-by-model-size-orchestration-patterns-or-benchmark-performance/` -> `200`: pass

## Collision Safety

- Old entry `https://ivankotov.eu/diary/a-new-public-layer-is-now-part-of-the-corpus/` still returns `200`: pass
- New collision-safe V41 entry `https://ivankotov.eu/diary/a-new-public-layer-is-now-part-of-the-corpus-0112/` returns `200`: pass

## New Tag Pages

- `https://ivankotov.eu/diary/tags/experience-artifacts/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/traceability/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/operational-ai/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/cost-of-error/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/signal-vs-noise/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/information-economy/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/constraint-driven/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/reality-bound/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/systemarchitec/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/domestic-infrastructure/` -> `200`: pass

## Existing Affected Tag Pages

- `https://ivankotov.eu/diary/tags/ai/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/ai-safety/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/agi/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/advanced-global-intelligence/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/ai-architecture/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/ai-economy/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/audit-trail/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/auditability/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/continuity/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/cybernetics/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/digital-entities/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/human-ai/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/human-centered-ai/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/l4/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/long-lived-ai/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/provenance/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/risk-management/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/systems-engineering/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/systems-thinking/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/trust/` -> `200`: pass
- `https://ivankotov.eu/diary/tags/verification/` -> `200`: pass

## Machine-Readable Surfaces

- `https://ivankotov.eu/diary-index.json` -> `200`; count `113`: pass
- `https://ivankotov.eu/diary-latest.json` -> `200`; latest slug is `there-is-a-difference-between-digital-immortality-and-what-i-would-call-post-anchor-continuity`: pass
- `https://ivankotov.eu/diary-tags.json` -> `200`; contains `experience-artifacts`, `systemarchitec`, and `domestic-infrastructure`: pass
- `https://ivankotov.eu/diary-feed.xml` -> `200`; contains the V41 entry slugs: pass
- `https://ivankotov.eu/sitemap.xml` -> `200`; contains the five V41 entry URLs and the ten new V41 tag URLs: pass

## Asset Checks

- `https://ivankotov.eu/assets/diary/most-ai-economy-talk-is-still-pricing-the-wrong-thing/cover.jpg` -> `200`: pass
- `https://ivankotov.eu/assets/diary/i-watched-the-interview-with-roman-yampolskiy/cover.jpg` -> `200`: pass
- `https://ivankotov.eu/assets/diary/there-is-a-difference-between-digital-immortality-and-what-i-would-call-post-anchor-continuity/cover.jpg` -> `200`: pass
- `https://ivankotov.eu/assets/diary/a-new-public-layer-is-now-part-of-the-corpus-0112/cover.jpg` -> `200`: pass
- `https://ivankotov.eu/assets/diary/in-the-end-i-do-not-think-the-future-of-ai-will-be-decided-only-by-model-size-orchestration-patterns-or-benchmark-performance/cover.jpg` -> `200`: pass

## Baseline Checks

- V23 date-only meta rendering remained intact live: pass
- V28 five-entry preview remained intact live: pass
- No fake or placeholder image surfaced live: pass
