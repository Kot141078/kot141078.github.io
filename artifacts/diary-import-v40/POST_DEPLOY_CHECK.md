# POST_DEPLOY_CHECK

## Deployment

- Domain: `https://ivankotov.eu`
- Implementation commit checked live: `533ec0e7452d8576fd0342d02b7797ab84adc2c2`
- Live validation result: pass on first post-push check

## Remote Status Checks

- `https://ivankotov.eu/` -> `200`
- `https://ivankotov.eu/diary/` -> `200`
- `https://ivankotov.eu/diary/archive/` -> `200`
- `https://ivankotov.eu/diary/tags/` -> `200`
- `https://ivankotov.eu/diary/a-review-layer-can-fail-in-two-opposite-ways/` -> `200`
- `https://ivankotov.eu/diary/a-release-is-not-serious-if-it-lives-only-in-theory/` -> `200`
- `https://ivankotov.eu/diary/a-protocol-is-not-serious-if-it-cannot-survive-packaging/` -> `200`
- `https://ivankotov.eu/diary/not-every-anomaly-deserves-memory/` -> `200`
- `https://ivankotov.eu/diary/the-quiet-upgrade-in-arq-v0-2-is-model-discipline/` -> `200`
- `https://ivankotov.eu/diary/tags/bounded-authority/` -> `200`
- `https://ivankotov.eu/diary/tags/runtime-discipline/` -> `200`
- `https://ivankotov.eu/diary/tags/witnesstra/` -> `200`
- `https://ivankotov.eu/diary/tags/advancedglobalintelligencefety/` -> `200`
- `https://ivankotov.eu/diary/tags/systems-engineering/` -> `200`
- `https://ivankotov.eu/diary/tags/protocol-design/` -> `200`
- `https://ivankotov.eu/diary/tags/structural-honesty/` -> `200`
- `https://ivankotov.eu/diary-index.json` -> `200`
- `https://ivankotov.eu/diary-tags.json` -> `200`
- `https://ivankotov.eu/diary-latest.json` -> `200`
- `https://ivankotov.eu/diary-feed.xml` -> `200`
- `https://ivankotov.eu/sitemap.xml` -> `200`
- `https://ivankotov.eu/assets/diary/a-review-layer-can-fail-in-two-opposite-ways/cover.jpg` -> `200`
- `https://ivankotov.eu/assets/diary/a-release-is-not-serious-if-it-lives-only-in-theory/cover.jpg` -> `200`
- `https://ivankotov.eu/assets/diary/a-protocol-is-not-serious-if-it-cannot-survive-packaging/cover.jpg` -> `200`
- `https://ivankotov.eu/assets/diary/not-every-anomaly-deserves-memory/cover.jpg` -> `200`
- `https://ivankotov.eu/assets/diary/the-quiet-upgrade-in-arq-v0-2-is-model-discipline/cover.jpg` -> `200`

## Content Assertions

- Home latest-post points to `the-quiet-upgrade-in-arq-v0-2-is-model-discipline`: pass
- Home latest-post meta remains date-only: pass
- `/diary/` top five order is `0108 > 0107 > 0106 > 0104 > 0105`: pass
- `/diary/` preview still exposes five recent entries: pass
- `/diary/archive/` contains all five imported posts: pass
- `diary-index.json` count is `108`: pass
- `diary-latest.json` latest slug is `the-quiet-upgrade-in-arq-v0-2-is-model-discipline`: pass
- `POST 0104-0108` preserve clickable GitHub links and clickable DOI lines: pass
- Live tag propagation preserves `WitnessTra` literally: pass
- Live tag propagation preserves `AdvancedGlobalIntelligencefety` literally: pass
- `sitemap.xml` includes all five V40 entry URLs and four new V40 tag URLs: pass
- No placeholder/fake image detected in live outputs: pass

## Baseline Checks

- V23 date-only meta fix intact on live home and diary cards: pass
- V28 five-entry preview fix intact on live `/diary/`: pass
- No unrelated public layer changes detected in this pass: pass
