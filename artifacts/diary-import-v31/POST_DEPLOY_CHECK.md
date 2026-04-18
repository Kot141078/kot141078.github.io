# POST_DEPLOY_CHECK

## Deploy readiness

- Poll target: `https://ivankotov.eu/diary-latest.json`
- First successful ready poll: attempt `1`
- Expected latest slug: `ai-isnt-expensive-its-becoming-infrastructure`
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
  - `https://ivankotov.eu/diary/ai-horror-stories-sell-emotion-the-real-ai-shift-is-boring-responsibility-limits-and-proof/`
  - `https://ivankotov.eu/diary/most-ai-talk-is-still-stuck-on-capability-what-can-it-do/`
  - `https://ivankotov.eu/diary/experience-economy-why-verified-experience-will-outprice-raw-intelligence/`
  - `https://ivankotov.eu/diary/when-tokens-become-electricity-terms-of-use-become-physics/`
  - `https://ivankotov.eu/diary/ai-isnt-expensive-its-becoming-infrastructure/`
- Regression anchor:
  - `https://ivankotov.eu/diary/data-harvesting-is-not-inevitable-it-s-a-design-choice/`
- Machine-readable endpoints:
  - `https://ivankotov.eu/diary-index.json`
  - `https://ivankotov.eu/diary-tags.json`
  - `https://ivankotov.eu/diary-latest.json`
  - `https://ivankotov.eu/diary-feed.xml`
  - `https://ivankotov.eu/sitemap.xml`
- Image assets:
  - `https://ivankotov.eu/assets/diary/ai-horror-stories-sell-emotion-the-real-ai-shift-is-boring-responsibility-limits-and-proof/cover.jpg`
  - `https://ivankotov.eu/assets/diary/most-ai-talk-is-still-stuck-on-capability-what-can-it-do/cover.jpg`
  - `https://ivankotov.eu/assets/diary/experience-economy-why-verified-experience-will-outprice-raw-intelligence/cover.jpg`
  - `https://ivankotov.eu/assets/diary/when-tokens-become-electricity-terms-of-use-become-physics/cover.jpg`
  - `https://ivankotov.eu/assets/diary/ai-isnt-expensive-its-becoming-infrastructure/cover.jpg`
- Affected tag pages: all URLs listed in [SEARCH_CONSOLE_SUBMISSION_PLAN_V31.md](/C:/Users/kotov/Desktop/AGI/kot141078.github.io/SEARCH_CONSOLE_SUBMISSION_PLAN_V31.md) under `Affected tag pages`

## Live data checks

- `diary-index.json count`: `63`
- `diary-index.json latest.slug`: `ai-isnt-expensive-its-becoming-infrastructure`
- `diary-latest.json item.slug`: `ai-isnt-expensive-its-becoming-infrastructure`
- `diary-feed.xml item count`: `63`
- repeated-question motif packets remained distinct: `PASS`
- `human-agency` bucket count after V31: `1`
- `verification` bucket count after V31: `3`
- `trust` bucket count after V31: `2`
- `resilience` bucket count after V31: `2`
- `reliability` bucket count after V31: `1`
- `sitemap.xml` contains latest entry: `PASS`
- `sitemap.xml` contains new tag `verification`: `PASS`

## Live UI checks

- Home latest-post meta line date-only: `PASS`
- Diary card meta lines date-only: `PASS`
- `/diary/` preview contains all five imported posts under V28 preview-size policy: `PASS`
- `/diary/archive/` contains all five imported posts: `PASS`
- `POST 0059` preserves `c=a+b` and two-line closing: `PASS`
- `POST 0060` inline GitHub repo link preserved: `PASS`
- `POST 0060` `Facts` / `My frame` / explicit bridge structure preserved: `PASS`
- `POST 0061` `Earth paragraph:` label preserved: `PASS`
- `POST 0061` repeated closing question preserved without collapse: `PASS`
- `POST 0062` `Local motor, external oracle.` and numbered outcomes preserved: `PASS`
- `POST 0063` short opener and `My operational takeaway is simple` preserved: `PASS`
- No fake or placeholder image introduced on checked surfaces: `PASS`

## Tag membership checks

- Total tag membership checks: `45`
- Failures: `0`
- Method: for each imported post, every affected live tag page was checked for the presence of that post slug in rendered HTML

## Conclusion

V31 is live and structurally consistent:

- all five entries render
- latest-post switched correctly to `ai-isnt-expensive-its-becoming-infrastructure`
- all affected tag pages render and include their expected posts
- machine-readable surfaces, feed, sitemap, and images are live
- repeated closing-question motifs did not trigger overwrite or collapse
- V23 date-only meta rendering and V28 preview-size behavior remain intact
