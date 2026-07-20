# Search Console Submission Plan V64

Status: prepared; manual Search Console action remains.

Submit/request:

- Request indexing for `https://ivankotov.eu/vision/`.
- Resubmit sitemap `https://ivankotov.eu/sitemap.xml`.

Reason:

- V64 creates one new public HTML route: `https://ivankotov.eu/vision/`.
- V64 creates two machine-readable Vision endpoints:
  - `https://ivankotov.eu/vision/index.json`
  - `https://ivankotov.eu/vision/schemaorg.jsonld`
- Sitemap includes only the new HTML URL, not the JSON endpoints.

Post-submission checks:

- Confirm `/vision/` is eligible for indexing.
- Confirm canonical URL is `https://ivankotov.eu/vision/`.
- Confirm sitemap fetch succeeds after resubmission.
- Do not submit a Russian Vision route; V64 has none.

