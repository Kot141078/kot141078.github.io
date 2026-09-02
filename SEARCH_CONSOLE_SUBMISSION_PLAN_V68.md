# Search Console Submission Plan V68

This is a manual submission plan. No Search Console action was automated.

## Priority 1 - request indexing

Request indexing for exactly these seven new Diary pages:

1. `https://ivankotov.eu/diary/many-people-now-speak-of-disappointment-with-artificial-intelligence/`
2. `https://ivankotov.eu/diary/an-api-key-tells-a-provider-which-credential-made-the-call/`
3. `https://ivankotov.eu/diary/the-most-important-point-in-jerry-tworeks-new-interview-is-not-his-estimate-that-human-researchers-may-stop-being-a-meaningful-part-of-ai-research-in-roughly-two-years/`
4. `https://ivankotov.eu/diary/who-will-need-protection-and-from-whom/`
5. `https://ivankotov.eu/diary/saturday-traffic-report-from-the-ai-highway/`
6. `https://ivankotov.eu/diary/ai-will-not-create-a-generation-with-no-seniors/`
7. `https://ivankotov.eu/diary/search-advertising-largely-monetized-the-query/`

Deployment prerequisite: `PASS`. All seven URLs returned cache-busted HTTP 200, occur in the archive/feed/deployed sitemap, and correspond to exactly one remote Diary record.

## Priority 2 - Diary landing page

Optionally request re-indexing for:

- `https://ivankotov.eu/diary/`

The deployed page exposes 230 entries, a latest date of 2026-09-01, and exactly five latest cards in order ENTRY 0230, 0229, 0228, 0227, 0226.

## Priority 3 - sitemap

Resubmit:

- `https://ivankotov.eu/sitemap.xml`

The deployed root sitemap contains 322 URLs: the 315-URL V67 baseline plus exactly seven V68 Diary entry URLs, with zero removals, zero noindex tag additions, zero image additions, and zero Diary JSON/machine-endpoint additions.

## Explicit exclusions

Do not request indexing for affected tag pages. All 50 affected detail-tag routes intentionally retain `noindex, follow` and remain outside the sitemap.

Do not manually submit:

- image asset URLs;
- `diary-index.json`, `diary-tags.json`, or `diary-latest.json`;
- `diary-feed.xml`;
- any machine JSON endpoint.

## Manual remainder

- Request indexing for the seven Priority 1 Diary pages.
- Optionally request re-indexing for `/diary/`.
- Resubmit `https://ivankotov.eu/sitemap.xml`.
