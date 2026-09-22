# V72 Post-Deploy Check

Implementation commit: `775f3482c7ca660b565d351e6e4294f0d85d9b40`.

## Workflow gates

- GitHub Pages run `35789095304`: success.
- Machine readability run `35789095854`: success.

## Production state

- Cache-busted non-asset route checks: 72 / 72 HTTP 200.
- New image route checks: 7 / 7 HTTP 200 and byte-identical to local.
- Affected canonical tag routes: 44 / 44 HTTP 200, `noindex`, absent from sitemap.
- Diary count: 247.
- Latest: ENTRY 0247, 2026-09-22.
- Homepage latest: ENTRY 0247.
- Latest-card count: five.
- Latest-card order: 0247, 0246, 0245, 0244, 0243.
- 2026-09-17 order: 0244, 0243.
- 2026-09-16 order: 0242, 0241.
- V69: five Diary entries plus World Intelligence external position 06 with `Open book`.
- Sitemap: 345 URLs; complete local and deployed sets equal.

All required root, Diary, archive, tags, Start-here, JSON, feed, sitemap, V72 entry, V72 asset, affected tag, World Intelligence, corpus, Vision, publications, and Embodiment routes passed. ENTRY 0242 retains the resolved LinkedIn source link. ENTRY 0246 retains its Zenodo and first-party publication links. ENTRY 0247 retains the exact `EUAIAIAct` entry-page token.

Six required production screenshots were created under `C:\Users\kotov\Downloads\111\diary-v72-visual\` and inspected. Desktop and mobile layouts have no horizontal overflow or broken images.

Remote deployment verdict: pass. Open blockers: none.
