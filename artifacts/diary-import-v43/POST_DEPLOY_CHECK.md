# POST_DEPLOY_CHECK

## Deployment

- Implementation commit pushed: `71de00e7106cea345cce7188205da225e8f32651`
- Readiness URL: `https://ivankotov.eu/diary/not-every-continuity-deserves-to-be-called-a-subject/`
- Readiness result: `200`

## Corrected Live Validation

- Initial live validation had one over-broad local check for `diary-feed.xml`: it required tag URLs in the feed. This was corrected because the feed is required to contain entry URLs, not tag URLs.
- Corrected validation result: pass

## Remote Checks

- `/`: `200`, latest post checked
- `/diary/`: `200`, all V43 entries checked
- `/diary/archive/`: `200`, all V43 entries checked
- `/diary/tags/`: `200`, new tag links checked
- Five V43 entry pages: `200`
- Five V43 cover assets: `200`, image content type
- `diary-index.json`: `200`, `count=124`, latest POST 0122
- `diary-latest.json`: `200`, latest POST 0122
- `diary-tags.json`: `200`, new tags present
- `diary-feed.xml`: `200`, all V43 entry URLs present
- `sitemap.xml`: `200`, all V43 entry URLs and new tag URLs present
- Affected tag pages checked: `31`
- V23 live checks: pass on home, `/diary/`, and `/diary/archive/`
- V28 live check: `/diary/` preview count `5`
