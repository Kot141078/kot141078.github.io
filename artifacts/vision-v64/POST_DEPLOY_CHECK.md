# Vision V64 Post Deploy Check

Verdict: PASS.

Implementation commit:

`49e83dc0cbade14f7449ff22244beb76d979eb48`

Pages deployment:

- Run ID: `29763915974`
- Workflow: `pages-build-deployment`
- Status: completed
- Conclusion: success
- Created: `2026-07-20T17:30:10Z`
- Updated: `2026-07-20T17:31:21Z`
- URL: `https://github.com/Kot141078/kot141078.github.io/actions/runs/29763915974`

Remote validation SHA-256 receipts:

- `/vision/` 200, SHA-256 `27d880b297ad560efd1cddc2924a196036b047cb47367c9aada0e27e9604dbb2`
- `/vision/index.json` 200, SHA-256 `09c7942e69cceeeb683c9b6eeee0f8052c0814dbff36b3b472a93acc6efdcb1a`
- `/vision/schemaorg.jsonld` 200, SHA-256 `7dbf119aa2cf99d11415479838a1fb80d8ff750caea79774ceeff1aec75ec123`
- `/sitemap.xml` 200, SHA-256 `04bb0c279c32ff8eacfc2f03946419d0795259004db758602ac8af09cea9e814`
- `/llms.txt` 200, SHA-256 `24f5c33fce6c74708d33959325fe1bc668d9a9c8d54da96d74c4205148daa7bc`
- `/llms-full.txt` 200, SHA-256 `cde545b2e5d9c866b4fb2fadbfe0113c1898a8783cef758e7e3013297e8e2614`

Remote semantic checks:

- `/vision/` live: PASS.
- `/vision/index.json` parses and declares route `/vision/`: PASS.
- `/vision/schemaorg.jsonld` parses and preserves Article semantics: PASS.
- Sitemap has 805 HTML URLs: PASS.
- Sitemap contains `https://ivankotov.eu/vision/` exactly once: PASS.
- Sitemap contains no Vision JSON endpoints: PASS.
- `llms.txt` contains Vision: PASS.
- `llms-full.txt` exists and contains Vision: PASS.
- Exact agent/c sentence counts: Start here 1, Distinctions 1, Vision 1, llms 0: PASS.
- Required inbound nav/link surfaces: PASS.

