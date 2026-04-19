# POST_DEPLOY_CHECK

## Deployment

- Domain: `https://ivankotov.eu`
- Implementation commit checked live: `1a6d557213f55ff87055be2e8446c9d82f43ea74`
- Live validation result: pass on first post-push check

## Remote Status Checks

- `https://ivankotov.eu/` -> `200`
- `https://ivankotov.eu/diary/` -> `200`
- `https://ivankotov.eu/diary/archive/` -> `200`
- `https://ivankotov.eu/diary/tags/` -> `200`
- `https://ivankotov.eu/diary/continuity-bundle-cold-wake-v0-1/` -> `200`
- `https://ivankotov.eu/diary/today-im-publishing-volume-i-of-qubit-of-hope/` -> `200`
- `https://ivankotov.eu/diary/published-volume-i-of-qubit-of-hope/` -> `200`
- `https://ivankotov.eu/diary/most-ai-systems-are-still-built-around-a-dangerous-social-illusion/` -> `200`
- `https://ivankotov.eu/diary/one-of-the-most-harmful-habits-in-current-ai-systems-is-this/` -> `200`
- `https://ivankotov.eu/diary/tags/qubit-of-hope/` -> `200`
- `https://ivankotov.eu/diary/tags/book-release/` -> `200`
- `https://ivankotov.eu/diary/tags/continuity-bundle/` -> `200`
- `https://ivankotov.eu/diary/tags/cold-wake/` -> `200`
- `https://ivankotov.eu/diary/tags/ser/` -> `200`
- `https://ivankotov.eu/diary/tags/structural-honesty/` -> `200`
- `https://ivankotov.eu/diary-index.json` -> `200`
- `https://ivankotov.eu/diary-tags.json` -> `200`
- `https://ivankotov.eu/diary-latest.json` -> `200`
- `https://ivankotov.eu/diary-feed.xml` -> `200`
- `https://ivankotov.eu/sitemap.xml` -> `200`
- `https://ivankotov.eu/assets/diary/continuity-bundle-cold-wake-v0-1/cover.jpg` -> `200`
- `https://ivankotov.eu/assets/diary/published-volume-i-of-qubit-of-hope/cover.jpg` -> `200`
- `https://ivankotov.eu/assets/diary/most-ai-systems-are-still-built-around-a-dangerous-social-illusion/cover.jpg` -> `200`
- `https://ivankotov.eu/assets/diary/one-of-the-most-harmful-habits-in-current-ai-systems-is-this/cover.jpg` -> `200`

## Content Assertions

- Home latest-post points to `one-of-the-most-harmful-habits-in-current-ai-systems-is-this`: pass
- Home latest-post meta remains date-only: pass
- `/diary/` top five order is `0103 > 0102 > 0101 > 0100 > 0099`: pass
- `/diary/` preview still exposes five recent entries: pass
- `/diary/archive/` contains all five imported posts: pass
- `diary-index.json` count is `103`: pass
- `diary-latest.json` latest slug is `one-of-the-most-harmful-habits-in-current-ai-systems-is-this`: pass
- `POST 0100` remains image-less on the live page: pass
- `POST 0099` live page preserves clickable Zenodo link: pass
- `POST 0101` live page preserves clickable repo link: pass
- `POST 0102` live page preserves GitHub and Zenodo blocks: pass
- `POST 0103` live page preserves GitHub and Zenodo blocks: pass
- `sitemap.xml` includes all five entry URLs and new tag URLs added for V39: pass
- No placeholder/fake image detected in live outputs: pass

## Baseline Checks

- V23 date-only meta fix intact on live home and diary cards: pass
- V28 five-entry preview fix intact on live `/diary/`: pass
- No unrelated public layer changes detected in this pass: pass
