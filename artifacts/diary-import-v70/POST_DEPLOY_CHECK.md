# V70 Post-Deploy Check

Implementation commit: `6564b9f1691c68fd1a7e1e744e76a28c9c3d3aac`

## Workflows

| Workflow | Run ID | Head | Result |
| --- | ---: | --- | --- |
| Pages build and deployment | `35772117125` | `6564b9f1691c68fd1a7e1e744e76a28c9c3d3aac` | success |
| Machine readability | `35772117479` | `6564b9f1691c68fd1a7e1e744e76a28c9c3d3aac` | success |

## Remote canonical state

- Diary count: 235.
- Latest: ENTRY 0235 / 2026-09-08.
- Homepage latest: ENTRY 0235.
- Latest-card count: 5.
- Latest-card order: 0235, 0234, 0233, 0232, 0231.
- New entry routes: 5/5 HTTP 200.
- New image routes: 7/7 HTTP 200, `image/jpeg`, byte-identical to local assets.
- JSON endpoints: `diary-index.json`, `diary-latest.json`, `diary-start-here.json` parse and return HTTP 200.
- XML endpoints: `diary-feed.xml`, `sitemap.xml` parse and return HTTP 200.
- Qubit Volume I Diary page: HTTP 200.

## Regression state

- V23: pass; visible card metadata is date-only.
- V28: pass; exactly five latest cards.
- V59: pass; compact landing/search/tag behavior and literal `L4` retained; `L 4` count zero.
- V69: pass; six positions, five Diary items plus one external World Intelligence route at position 06; CTA `Open book`; no Qubit card.
- ENTRY 0216: five-image gallery intact.
- ENTRY 0233: exact three-image order intact.
- ENTRY 0235: no invented LinkedIn trace.
- Windows local-path leak: zero.

## Sitemap parity

Local and deployed sets are equal at 333 URLs. Relative to baseline HEAD, exactly five new Diary HTML routes were added and zero URLs were removed. No noindex tag, image, or JSON URL was added.

## Visual state

Receipts are stored at `C:\Users\kotov\Downloads\111\diary-v70-visual\`.

- Diary desktop/mobile: pass.
- Home latest desktop: pass.
- ENTRY 0231-0235: pass.
- ENTRY 0233 desktop/mobile gallery: pass.
- Diary Start-here / World Intelligence card: pass.
- A4 print: 7 pages, no blank page, clipping, overlap, or broken image.
- Remote screenshots: 6/6 byte-identical to corresponding local screenshots.
- Remote browser metrics: document/client widths 1440/1440 and 390/390; broken images zero.

Remote verdict: `PASS`.
