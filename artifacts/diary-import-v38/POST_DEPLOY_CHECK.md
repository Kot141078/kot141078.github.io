# POST_DEPLOY_CHECK — V38

Date: 2026-04-19  
Implementation commit: `d2f707a2008e26908f789a4004133c94adedcc06`  
Resolved entry slugs: `one-more-distinction-needs-to-be-fixed-clearly`, `that-is-why-this-package-does-not-stop-at-concepts`, `one-of-the-biggest-mistakes-in-current-ai-fear-discourse-is-the-confusion-between-infrastructural-power-and-ontological-independence`, `what-interests-me-here-is-larger-than-one-stack`, `one-of-the-deepest-blind-spots-in-current-ai-discourse-is-the-poverty-of-its-model-of-memory`  
Primary domain: `https://ivankotov.eu/`

## Deployment Readiness

- `diary-latest.json` converged to the V38 latest slug after 4 polling attempts.

## Remote Status Summary

- Core surfaces returned `200`:
  - `/`
  - `/diary/`
  - `/diary/archive/`
  - `/diary/tags/`
  - `/diary-index.json`
  - `/diary-latest.json`
  - `/diary-tags.json`
  - `/diary-feed.xml`
  - `/sitemap.xml`
- All five new entry pages returned `200`.
- All five V38 cover assets returned `200`.
- Two older V20 `10.jpg`-derived asset URLs still returned `200`.
- All 35 affected tag pages returned `200`.

## Validation Assertions

- live latest slug is `what-interests-me-here-is-larger-than-one-stack`: pass
- live home latest-post link points to `/diary/what-interests-me-here-is-larger-than-one-stack/`: pass
- live home latest-post meta line is date-only: pass
- live `/diary/` latest section top-5 is `0097, 0098, 0095, 0096, 0094`: pass
- live `/diary/` archive preview top-5 is `0097, 0098, 0095, 0096, 0094`: pass
- live `/diary/archive/` contains all five imported posts: pass
- live affected tag pages contain expected membership: pass
- `POST 0095` preserves both Zenodo URLs as clickable anchors: pass
- `POST 0097` preserves the related framing link as a clickable anchor: pass
- `POST 0098` exposes corrected `90.jpg` alt text: pass
- older V20 `10.jpg`-derived asset paths remained intact after the V38 correction: pass
- V23 date-only meta baseline remains intact live: pass
- V28 five-entry preview baseline remains intact live: pass
- no fake image or placeholder was introduced anywhere: pass

## Corrected Source Note

- The original packet for `POST 0098` named `10.jpg`.
- The user corrected that source to `90.jpg` before finalization.
- Final deployed V38 state uses `90.jpg` for `POST 0098`.
