# Search Console Submission Plan V60

## Scope

This plan is for manual Google Search Console follow-up after the homepage information-architecture compression in V60.

No Search Console submission was performed by this run.

## Indexing Priority

Priority 1:

- `https://ivankotov.eu/`

Priority 2:

- `https://ivankotov.eu/start-here/`
- `https://ivankotov.eu/publications/`
- `https://ivankotov.eu/diary/`

Priority 3:

- `https://ivankotov.eu/sitemap.xml`

## Reason

V60 changes the homepage structure, prominence, and crawl path density. It does not create new public URLs, remove public URLs, or change sitemap membership.

The homepage should be requested for re-indexing first because it is the changed entry surface. The route pages should be inspected afterward because they are now the primary next-click surfaces from the compressed homepage.

## Manual Procedure

1. Open Google Search Console for `https://ivankotov.eu/`.
2. Use URL Inspection for `https://ivankotov.eu/`.
3. Confirm the live URL is available and renders the V60 homepage.
4. Request indexing for the homepage.
5. Inspect the Priority 2 URLs if Search Console reports crawl or canonical warnings.
6. Resubmit `https://ivankotov.eu/sitemap.xml` only if Search Console shows stale sitemap state or delayed discovery.

## Validation Receipts To Compare

Remote validation used cache token:

`v60-20260719172234`

Remote route checks returned HTTP 200 for:

- `https://ivankotov.eu/`
- `https://ivankotov.eu/start-here/`
- `https://ivankotov.eu/what-is-running/`
- `https://ivankotov.eu/publications/`
- `https://ivankotov.eu/diary/`
- `https://ivankotov.eu/library/`
- `https://ivankotov.eu/services/`
- `https://ivankotov.eu/about/`
- `https://ivankotov.eu/contact/`
- `https://ivankotov.eu/install-c/`
- `https://ivankotov.eu/diary-index.json`
- `https://ivankotov.eu/diary-latest.json`
- `https://ivankotov.eu/sitemap.xml`

Sitemap membership check:

- Local sitemap URL count: 797
- Remote sitemap URL count: 797
- Added URLs: 0
- Removed URLs: 0

## Completion Criteria

Search Console follow-up is complete when:

- Homepage live inspection sees the V60 homepage.
- Homepage indexing request is accepted or Search Console reports that indexing is already current.
- Sitemap remains accepted with the expected URL count.
- No new coverage warnings appear for the Priority 2 routes.
