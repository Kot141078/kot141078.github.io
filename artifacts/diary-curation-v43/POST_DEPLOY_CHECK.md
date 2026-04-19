# POST_DEPLOY_CHECK

## Deployment Result

- Implementation commit pushed: `6d6ddd2abc2477faf41851446def29a8710bd692`
- Live convergence result: pass
- Final validation pass: `20` remote checks passed
- Verification note: an earlier retry loop produced a false negative only because the `llms.txt` predicate omitted the leading slash in the final discovery sentence; the public surfaces themselves were already returning `200`
- Pages build metadata note: GitHub Pages latest-build API was not exposed anonymously for this repo during the check window and returned `404 Not Found`; deployment confirmation was therefore taken from public-site convergence plus direct HTTP verification

## Live Surface Checks

- `https://ivankotov.eu/` -> `200`; home diary slot includes `Open Diary` and `Start here`: pass
- `https://ivankotov.eu/diary/` -> `200`; curated landing now shows `Start here`, `Themes`, and `Cornerstones`: pass
- `https://ivankotov.eu/diary/start-here/` -> `200`; populated with six real starting entries and the required note that these are not "best posts": pass
- `https://ivankotov.eu/diary/themes/` -> `200`; populated with six real theme cards: pass
- `https://ivankotov.eu/diary/archive/` -> `200`; month-grouped archive with direct links to themes and tags: pass
- `https://ivankotov.eu/diary/tags/` -> `200`; canonical normalized tag index is live: pass

## Theme Pages

- `https://ivankotov.eu/diary/themes/agi-c-a-plus-b/` -> `200`: pass
- `https://ivankotov.eu/diary/themes/l4-ser-governance/` -> `200`: pass
- `https://ivankotov.eu/diary/themes/local-first-infrastructure/` -> `200`: pass
- `https://ivankotov.eu/diary/themes/book-layer/` -> `200`: pass
- `https://ivankotov.eu/diary/themes/practical-architecture/` -> `200`: pass
- `https://ivankotov.eu/diary/themes/oversight-evidence/` -> `200`: pass

## Representative Post Check

- `https://ivankotov.eu/diary/there-is-a-difference-between-digital-immortality-and-what-i-would-call-post-anchor-continuity/` -> `200`: pass
- Related-posts block `Continue from here` is visible live: pass
- Related-posts note `Related by normalized tags, curated themes, and nearby chronology.` is visible live: pass

## Tag Normalization Check

- `https://ivankotov.eu/diary/tags/agi/` -> `200`: pass
- Alias page points to canonical `https://ivankotov.eu/diary/tags/advanced-global-intelligence/`: pass
- Alias note `normalized under` is visible live: pass

## Machine-Readable Surfaces

- `https://ivankotov.eu/diary-index.json` -> `200`; count `117`: pass
- `https://ivankotov.eu/diary-themes.json` -> `200`; contains `agi-c-a-plus-b`: pass
- `https://ivankotov.eu/diary-cornerstones.json` -> `200`; contains `published-volume-i-of-qubit-of-hope`: pass
- `https://ivankotov.eu/diary-tag-map.json` -> `200`; contains canonical tag data including `Local-first AI`: pass
- `https://ivankotov.eu/llms.txt` -> `200`; includes diary start-here/themes discovery guidance and the new curation JSON files: pass
- `https://ivankotov.eu/sitemap.xml` -> `200`; contains `/diary/start-here/`, `/diary/themes/`, and the six theme pages: pass

## Acceptance Assertions

- `/diary/` is discovery-friendly rather than a flat dump: pass
- `/diary/start-here/` is populated with real imported posts: pass
- `/diary/themes/` is populated with real themes backed by real imported posts: pass
- Theme pages are populated with real entries: pass
- Related-post logic is visible live: pass
- Tag normalization works in public display: pass
- No fake posts or fake themes were introduced: pass
- Mobile-safe note: the served HTML uses the existing static CSS/layout system without new client-side complexity, and no broken layout markers were detected in the live HTML checks; this remains a static/live markup verification rather than a device-lab visual test
