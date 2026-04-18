# POST_DEPLOY_CHECK

## Deploy readiness

- Poll target: `https://ivankotov.eu/diary-latest.json`
- First successful ready poll: attempt `1`
- Expected latest slug: `the-future-is-not-an-event-it-is-a-process-0068`
- Result: `PASS`

## URL checks

- Total checked URLs: `58`
- HTTP `200` responses: `58`
- Failed URLs: none

Checked groups:

- Core HTML pages:
  - `https://ivankotov.eu/`
  - `https://ivankotov.eu/diary/`
  - `https://ivankotov.eu/diary/archive/`
  - `https://ivankotov.eu/diary/tags/`
- New entry pages:
  - `https://ivankotov.eu/diary/you-cant-take-ai-away-anymore-so-we-need-circuit-breakers-not-slogans/`
  - `https://ivankotov.eu/diary/beacon-profile-v0-1-why-ai-entities-need-recognition-not-just-identity/`
  - `https://ivankotov.eu/diary/ai-is-slowly-outgrowing-the-old-language-used-to-describe-it/`
  - `https://ivankotov.eu/diary/for-years-the-ai-race-was-framed-the-same-way/`
  - `https://ivankotov.eu/diary/the-future-is-not-an-event-it-is-a-process-0068/`
- Regression anchor:
  - `https://ivankotov.eu/diary/the-future-is-not-an-event-it-is-a-process/`
- Machine-readable endpoints:
  - `https://ivankotov.eu/diary-index.json`
  - `https://ivankotov.eu/diary-tags.json`
  - `https://ivankotov.eu/diary-latest.json`
  - `https://ivankotov.eu/diary-feed.xml`
  - `https://ivankotov.eu/sitemap.xml`
- Image assets:
  - `https://ivankotov.eu/assets/diary/you-cant-take-ai-away-anymore-so-we-need-circuit-breakers-not-slogans/cover.jpg`
  - `https://ivankotov.eu/assets/diary/beacon-profile-v0-1-why-ai-entities-need-recognition-not-just-identity/cover.jpg`
  - `https://ivankotov.eu/assets/diary/ai-is-slowly-outgrowing-the-old-language-used-to-describe-it/cover.jpg`
  - `https://ivankotov.eu/assets/diary/for-years-the-ai-race-was-framed-the-same-way/cover.jpg`
  - `https://ivankotov.eu/assets/diary/the-future-is-not-an-event-it-is-a-process-0068/cover.jpg`
- Affected tag pages: all URLs listed in [SEARCH_CONSOLE_SUBMISSION_PLAN_V32.md](/C:/Users/kotov/Desktop/AGI/kot141078.github.io/SEARCH_CONSOLE_SUBMISSION_PLAN_V32.md) under `Affected tag pages`

## Live data checks

- `diary-index.json count`: `68`
- `diary-latest.json item.slug`: `the-future-is-not-an-event-it-is-a-process-0068`
- `diary-feed.xml item count`: `68`
- `Recognition` bucket count after V32: `1`
- `Artificial Intelligence` bucket count after V32: `2`
- `AgentOS` bucket count after V32: `1`
- `AI Engineering` bucket count after V32: `1`
- `Inference` bucket count after V32: `1`
- `sitemap.xml` contains all five new entry URLs: `PASS`
- `sitemap.xml` contains the new V32 tag URLs `recognition`, `artificial-intelligence`, `agentos`, `ai-engineering`, and `inference`: `PASS`

## Live UI checks

- Home latest-post meta line date-only: `PASS`
- Diary card meta lines date-only: `PASS`
- `/diary/` preview contains all five imported posts under V28 preview-size policy: `PASS`
- `/diary/archive/` contains all five imported posts: `PASS`
- `POST 0064` preserves `Constraints-by-design.` and the ending question structure: `PASS`
- `POST 0065` inline external link preserved: `PASS`
- `POST 0065` numbered stack and recognition framing preserved: `PASS`
- `POST 0066` industrial-stack list preserved: `PASS`
- `POST 0066` foundry-stage framing preserved: `PASS`
- `POST 0067` quoted threshold question preserved: `PASS`
- `POST 0067` short two-line ending preserved: `PASS`
- `POST 0068` quoted opening premise preserved exactly: `PASS`
- `POST 0068` `Earth paragraph:` label preserved: `PASS`
- Older quote entry `/diary/the-future-is-not-an-event-it-is-a-process/` still renders live: `PASS`
- No fake or placeholder image introduced on checked surfaces: `PASS`

## Tag membership checks

- Total tag membership checks: `67`
- Failures: `0`
- Method: for each imported post, every affected live tag page was checked for the presence of that post slug in rendered HTML

## Conclusion

V32 is live and structurally consistent:

- all five entries render
- latest-post switched correctly to `the-future-is-not-an-event-it-is-a-process-0068`
- all affected tag pages render and include their expected posts
- machine-readable surfaces, feed, sitemap, and images are live
- `POST 0068` slug collision was resolved without damaging the older quote entry
- V23 date-only meta rendering and V28 preview-size behavior remain intact
