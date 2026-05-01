# POST_DEPLOY_CHECK V45

## Implementation

- Implementation commit: `a845aae7bcb04af71166ed2542a9b798efd181a1`
- Push target: `origin/main`
- Deploy readiness check: pass
- Readiness URL: `https://ivankotov.eu/diary/there-is-a-point-where-fluent-output-stops-being-impressive-and-responsibility-begins/`

## Live Validation

- `https://ivankotov.eu/`: pass
- `https://ivankotov.eu/diary/`: pass
- `https://ivankotov.eu/diary/archive/`: pass
- `https://ivankotov.eu/diary/tags/`: pass
- V45 entry pages returning `200`: `6`
- V45 cover assets returning `200` with image content type: `6`
- Affected canonical tag pages returning `200`: `36`
- `https://ivankotov.eu/diary-index.json`: pass, `count=135`
- Latest post: `there-is-a-point-where-fluent-output-stops-being-impressive-and-responsibility-begins`
- `https://ivankotov.eu/diary-latest.json`: pass
- `https://ivankotov.eu/diary-feed.xml`: pass
- `https://ivankotov.eu/sitemap.xml`: pass
- Same-date ordering for `2026-04-30`: `0130` before `0129`
- Same-date ordering for `2026-05-01`: `0131` before `0132`
- POST 0130 duplicate `Continuity`: deduped to one raw/canonical tag
- POST 0131 link rendering: pass
- POST 0132 multi-line hashtag parsing: pass
- V23 date-only rendering: pass
- V28 latest preview count: `5`

## V45 Entry URLs

- `https://ivankotov.eu/diary/one-of-the-strangest-habits-of-our-time-is-the-assumption-that-silence-means-absence/`
- `https://ivankotov.eu/diary/there-is-a-childish-version-of-future-thinking-that-assumes-if-something-survives-longer-it-has-somehow-escaped-time/`
- `https://ivankotov.eu/diary/when-people-hear-the-word-aging-they-usually-imagine-biology/`
- `https://ivankotov.eu/diary/one-of-the-quiet-shifts-in-ai-is-not-about-larger-models/`
- `https://ivankotov.eu/diary/one-of-the-missing-dimensions-in-most-ai-systems-is-not-intelligence/`
- `https://ivankotov.eu/diary/there-is-a-point-where-fluent-output-stops-being-impressive-and-responsibility-begins/`

## Manual Remainder

- Send URLs from `SEARCH_CONSOLE_SUBMISSION_PLAN_V45.md` to Search Console.
