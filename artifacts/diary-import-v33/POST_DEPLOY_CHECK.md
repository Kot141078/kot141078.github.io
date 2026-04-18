# POST_DEPLOY_CHECK

## Deploy readiness

- Poll target: `https://ivankotov.eu/diary-latest.json`
- First successful ready poll: attempt `1`
- Expected latest slug: `this-is-not-a-studio-render`
- Result: `PASS`

## URL checks

- Total checked URLs: `43`
- HTTP `200` responses: `43`
- Failed URLs: none

Checked groups:

- Core HTML pages:
  - `https://ivankotov.eu/`
  - `https://ivankotov.eu/diary/`
  - `https://ivankotov.eu/diary/archive/`
  - `https://ivankotov.eu/diary/tags/`
- New entry pages:
  - `https://ivankotov.eu/diary/i-think-many-people-still-underestimate-one-of-the-softest-and-strongest-signals-in-ai/`
  - `https://ivankotov.eu/diary/the-future-of-long-lived-ai-may-be-heterogeneous/`
  - `https://ivankotov.eu/diary/sometimes-i-think-the-current-agi-race-looks-less-like-science-and-more-like-cervantes/`
  - `https://ivankotov.eu/diary/this-is-not-a-studio-render/`
  - `https://ivankotov.eu/diary/freedom-of-thought-is-not-the-same-as-freedom-of-action/`
- Regression anchor:
  - `https://ivankotov.eu/diary/the-future-is-not-an-event-it-is-a-process-0068/`
- Machine-readable endpoints:
  - `https://ivankotov.eu/diary-index.json`
  - `https://ivankotov.eu/diary-tags.json`
  - `https://ivankotov.eu/diary-latest.json`
  - `https://ivankotov.eu/diary-feed.xml`
  - `https://ivankotov.eu/sitemap.xml`
- Image assets:
  - `https://ivankotov.eu/assets/diary/i-think-many-people-still-underestimate-one-of-the-softest-and-strongest-signals-in-ai/cover.jpg`
  - `https://ivankotov.eu/assets/diary/the-future-of-long-lived-ai-may-be-heterogeneous/cover.jpg`
  - `https://ivankotov.eu/assets/diary/sometimes-i-think-the-current-agi-race-looks-less-like-science-and-more-like-cervantes/cover.jpg`
  - `https://ivankotov.eu/assets/diary/this-is-not-a-studio-render/cover.jpg`
  - `https://ivankotov.eu/assets/diary/freedom-of-thought-is-not-the-same-as-freedom-of-action/cover.jpg`
- Affected tag pages: all URLs listed in [SEARCH_CONSOLE_SUBMISSION_PLAN_V33.md](/C:/Users/kotov/Desktop/AGI/kot141078.github.io/SEARCH_CONSOLE_SUBMISSION_PLAN_V33.md) under `Affected tag pages`

## Live data checks

- `diary-index.json count`: `73`
- `diary-latest.json item.slug`: `this-is-not-a-studio-render`
- `diary-feed.xml item count`: `73`
- top five live diary slugs reflect deterministic same-date ordering: `PASS`
- `Liya` bucket count after V33: `1`
- `Photonics` bucket count after V33: `1`
- `Quantum Computing` bucket count after V33: `1`
- `AIInfrast` bucket count after V33: `1`
- `sitemap.xml` contains all five new entry URLs: `PASS`
- `sitemap.xml` contains the new V33 tag URLs `liya`, `photonics`, `quantum-computing`, and `aiinfrast`: `PASS`

## Live UI checks

- Home latest-post meta line date-only: `PASS`
- Diary card meta lines date-only: `PASS`
- `/diary/` preview contains all five imported posts under V28 preview-size policy: `PASS`
- `/diary/archive/` contains all five imported posts: `PASS`
- `POST 0069` preserves `Attachment.` and `Earth paragraph:`: `PASS`
- `POST 0070` preserves `Not:` / `But:` contrast, substrate list, and excludes standalone `dary` noise: `PASS`
- `POST 0071` preserves the Don Quixote / Sancho Panza / Venus de Milo metaphor structure: `PASS`
- `POST 0071` literal `AIInfrast` handling is visible on live tag page `/diary/tags/aiinfrast/`: `PASS`
- `POST 0072` preserves the two-line opening and `Earth paragraph:`: `PASS`
- `POST 0073` preserves the contrast block and motor / drivetrain analogy: `PASS`
- Regression anchor `/diary/the-future-is-not-an-event-it-is-a-process-0068/` still renders live: `PASS`
- No fake or placeholder image introduced on checked surfaces: `PASS`

## Tag membership checks

- Total tag membership checks: `42`
- Failures: `0`
- Method: for each imported post, every affected live tag page was checked for the presence of that post slug in rendered HTML

## Conclusion

V33 is live and structurally consistent:

- all five entries render
- latest-post switched correctly to `this-is-not-a-studio-render`
- all affected tag pages render and include their expected posts
- machine-readable surfaces, feed, sitemap, and images are live
- malformed tag `AIInfrast` was preserved literally according to protocol and propagated consistently
- V23 date-only meta rendering and V28 preview-size behavior remain intact
