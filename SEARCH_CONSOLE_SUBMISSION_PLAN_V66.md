# Search Console Submission Plan V66

This is a manual plan. No Search Console submission was automated.

## Priority 1 - request indexing

Request indexing for all six new Diary pages:

1. `https://ivankotov.eu/diary/published-pasc-f0-gap-closure-scaffold-and-structural-templates-v0-1-1/`
2. `https://ivankotov.eu/diary/every-now-and-then-between-my-usual-thoughts-on-ai-infrastructure-and-machine-intelligence-the-old-pc-geek-in-me-stages-a-small-rebellion/`
3. `https://ivankotov.eu/diary/what-do-we-really-expect-from-ai/`
4. `https://ivankotov.eu/diary/sooner-or-later-we-will-have-to-negotiate-with-ai/`
5. `https://ivankotov.eu/diary/sometimes-useful-reading-for-ai-can-be-found-in-places-where-nobody-thinks-to-look/`
6. `https://ivankotov.eu/diary/the-ai-system-is-not-the-model/`

Deployment prerequisite: `PASS`. All six URLs return cache-busted HTTP 200, occur in the archive and sitemap, and correspond to exactly one remote Diary record.

## Priority 2 - Diary landing page

Optionally request re-indexing for:

- `https://ivankotov.eu/diary/`

The deployed page shows 217 entries, latest date 2026-08-16, and exactly five latest cards in order ENTRY 0217, 0216, 0215, 0214, 0213.

## Priority 3 - sitemap

Resubmit:

- `https://ivankotov.eu/sitemap.xml`

The deployed sitemap contains 309 URLs: the 303-URL baseline plus exactly six V66 entry URLs, with no removals and no tag-page additions.

## Explicit exclusions

Do not request indexing for affected tag pages. All 57 affected detail-tag routes intentionally retain `noindex` and remain outside the sitemap.

Do not manually submit:

- the ten image asset URLs;
- `diary-index.json`;
- `diary-tags.json`;
- `diary-latest.json`;
- any other JSON endpoint.

## Manual remainder

- Request indexing for the six Priority 1 Diary pages.
- Optionally request re-indexing for `/diary/`.
- Resubmit the sitemap after the V66 URL additions.
