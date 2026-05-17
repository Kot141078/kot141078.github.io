# CGAM v0.1.1 Website Integration Report

## Summary

CGAM v0.1.1 was integrated into the website as a discoverable publication surface.

## Repository

- Repo root: `kot141078.github.io`
- Branch: `main`
- Commit hash: assigned after commit; final hash is reported in the execution response

## Page

- Dedicated page path: `publications/c-governed-cli-agent-mesh/index.html`
- Expected public URL: https://ivankotov.eu/publications/c-governed-cli-agent-mesh/

## Files Changed

- `index.html`
- `publications/index.html`
- `publications/c-governed-cli-agent-mesh/index.html`
- `library/index.html`
- `works-index.json`
- `library-index.json`
- `canonical-map.json`
- `sitemap.xml`
- `reports/CGAM_V0_1_1_WEBSITE_INTEGRATION_REPORT.md`
- `reports/CGAM_V0_1_1_WEBSITE_INTEGRATION_REPORT.json`

## Integration Status

- Homepage update status: updated with a concise CGAM card.
- Publications index update status: updated with visible entry and JSON-LD entry.
- Sitemap update status: updated with the dedicated CGAM page URL.
- Metadata update status: `works-index.json`, `library-index.json`, and `canonical-map.json` updated.

## QA

- Build/check result: static site; no package/build command present. HTML parse, JSON parse, XML parse, sitemap, and local file-link checks passed before commit.
- Restricted-claim scan result: context-reviewed; matches are status boundaries or existing negative/gate language, not affirmative claims.
- Local path scan result: no Windows local path markers found in changed public site files or new report files.

## Warnings

- The GitHub Pages deployment may lag behind the pushed commit.
- The website records DOI/release links only; it does not modify GitHub release or Zenodo records.
- A repository-wide scan still finds pre-existing local path strings in historical root reports/artifacts outside this change set; this patch did not add or modify those files.
- Restricted terms appear in required negative/status language and existing CCDP boundary text; no affirmative restricted claim was added.

## Blockers

None.

## Recommendation

After push, verify https://ivankotov.eu/publications/c-governed-cli-agent-mesh/ and the homepage/publications links after GitHub Pages deployment completes.
