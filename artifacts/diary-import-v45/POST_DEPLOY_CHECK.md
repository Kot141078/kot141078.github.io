# POST_DEPLOY_CHECK

## Deployment

- Implementation commit pushed: `28590a6f05a4fef7010aeeb812b3dfc2a340656c`
- First new-entry probe: `404`
- Deployment convergence: attempt `2`
- New-entry readiness URL: `https://ivankotov.eu/diary/volume-ii-of-qubit-of-hope-is-now-public/`

## Remote Checks

- `https://ivankotov.eu/`: `200`, latest post checked
- `https://ivankotov.eu/diary/`: `200`, both V45 entries checked
- `https://ivankotov.eu/diary/archive/`: `200`, both V45 entries checked
- `https://ivankotov.eu/diary/tags/`: `200`, affected tag links checked
- `https://ivankotov.eu/diary/volume-ii-of-qubit-of-hope-is-now-public/`: `200`, title and image-less rendering checked
- `https://ivankotov.eu/diary/one-of-the-easiest-mistakes-in-ai-discourse-is-to-imagine-a-digital-entity-as-a-faster-human/`: `200`, title and image-less rendering checked
- `https://ivankotov.eu/diary-index.json`: `200`, `count=119`, `latest=volume-ii-of-qubit-of-hope-is-now-public`
- `https://ivankotov.eu/diary-tags.json`: `200`
- `https://ivankotov.eu/diary-latest.json`: `200`, `latest=volume-ii-of-qubit-of-hope-is-now-public`
- `https://ivankotov.eu/diary-feed.xml`: `200`, both new slugs present
- `https://ivankotov.eu/sitemap.xml`: `200`, both new slugs present
- Affected canonical tag pages checked: `27`
- Total remote URL checks passed after readiness: `38`

## Baseline Checks

- Live V23 date-only meta on `/`: pass
- Live V23 date-only meta on `/diary/`: pass
- Live V23 date-only meta on `/diary/archive/`: pass
- Live V28 `/diary/` latest preview count: `5`
