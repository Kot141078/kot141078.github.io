# Search Console Submission Plan V67

This is a manual submission plan. No Search Console action was automated.

## Priority 1 - request indexing

Request indexing for exactly these six new Diary pages:

1. `https://ivankotov.eu/diary/ai-is-eating-all-the-memory/`
2. `https://ivankotov.eu/diary/today-i-watched-my-cat-proudly-riding-the-robot-vacuum/`
3. `https://ivankotov.eu/diary/the-second-missing-layer-in-home-robotics-repair-without-identity-capture/`
4. `https://ivankotov.eu/diary/we-may-be-solving-ai-safety-at-the-wrong-level/`
5. `https://ivankotov.eu/diary/people-keep-asking-whether-ai-will-make-humanity-better-or-worse/`
6. `https://ivankotov.eu/diary/a-goal-can-be-installed/`

Deployment prerequisite: `PASS`. All six URLs returned cache-busted HTTP 200, occur in the archive and deployed sitemap, and correspond to exactly one remote Diary record.

## Priority 2 - Diary landing page

Optionally request re-indexing for:

- `https://ivankotov.eu/diary/`

The deployed page exposes 223 entries, a latest date of 2026-08-24, and exactly five latest cards in order ENTRY 0223, 0222, 0221, 0220, 0219.

## Priority 3 - sitemap

Resubmit:

- `https://ivankotov.eu/sitemap.xml`

The deployed root sitemap contains 315 URLs: the reconciled 309-URL V66 baseline plus exactly six V67 Diary entry URLs, with no removals, no tag-page additions, and no machine-endpoint additions.

## Explicit exclusions

Do not request indexing for affected tag pages. All 51 affected detail-tag routes intentionally retain `noindex` and remain outside the sitemap.

Do not manually submit:

- image asset URLs;
- `diary-index.json`, `diary-tags.json`, or `diary-latest.json`;
- `diary-feed.xml`;
- any machine JSON endpoint.

## Manual remainder

- Request indexing for the six Priority 1 Diary pages.
- Optionally request re-indexing for `/diary/`.
- Resubmit `https://ivankotov.eu/sitemap.xml`.
