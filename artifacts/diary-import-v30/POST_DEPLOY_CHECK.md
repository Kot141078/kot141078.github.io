# POST_DEPLOY_CHECK

## Deploy readiness

- Poll target: `https://ivankotov.eu/diary-latest.json`
- First successful ready poll: attempt `1`
- Expected latest slug: `data-harvesting-is-not-inevitable-it-s-a-design-choice`
- Result: `PASS`

## URL checks

- Total checked URLs: `106`
- HTTP `200` responses: `106`
- Failed URLs: none

Checked groups:

- Core HTML pages:
  - `https://ivankotov.eu/`
  - `https://ivankotov.eu/diary/`
  - `https://ivankotov.eu/diary/archive/`
  - `https://ivankotov.eu/diary/tags/`
- New entry pages:
  - `https://ivankotov.eu/diary/ester-clean-code-v0-2-1-is-out-with-v0-2-0-as-the-hardening-baseline/`
  - `https://ivankotov.eu/diary/the-eu-ai-act-is-landing-in-the-real-world-and-the-timing-is-not-accidental/`
  - `https://ivankotov.eu/diary/visual-experience-capsules-vxcx-why-what-you-see-matters-more-than-pixels/`
  - `https://ivankotov.eu/diary/l4-in-practice-5-reality-signals-that-kill-smart-systems-0057/`
  - `https://ivankotov.eu/diary/data-harvesting-is-not-inevitable-it-s-a-design-choice/`
- Regression anchors:
  - `https://ivankotov.eu/diary/hgi-why-am-i-only-hearing-this-now-and-why-general-is-never-a-default/`
  - `https://ivankotov.eu/diary/l4-in-practice-5-reality-signals-that-kill-smart-systems/`
- Machine-readable endpoints:
  - `https://ivankotov.eu/diary-index.json`
  - `https://ivankotov.eu/diary-tags.json`
  - `https://ivankotov.eu/diary-latest.json`
  - `https://ivankotov.eu/diary-feed.xml`
  - `https://ivankotov.eu/sitemap.xml`
- Image assets:
  - `https://ivankotov.eu/assets/diary/ester-clean-code-v0-2-1-is-out-with-v0-2-0-as-the-hardening-baseline/cover.jpg`
  - `https://ivankotov.eu/assets/diary/the-eu-ai-act-is-landing-in-the-real-world-and-the-timing-is-not-accidental/cover.jpg`
  - `https://ivankotov.eu/assets/diary/visual-experience-capsules-vxcx-why-what-you-see-matters-more-than-pixels/cover.jpg`
  - `https://ivankotov.eu/assets/diary/l4-in-practice-5-reality-signals-that-kill-smart-systems-0057/cover.jpg`
  - `https://ivankotov.eu/assets/diary/data-harvesting-is-not-inevitable-it-s-a-design-choice/cover.jpg`
- Affected tag pages: all URLs listed in [SEARCH_CONSOLE_SUBMISSION_PLAN_V30.md](/C:/Users/kotov/Desktop/AGI/kot141078.github.io/SEARCH_CONSOLE_SUBMISSION_PLAN_V30.md) under `Affected tag pages`

## Live data checks

- `diary-index.json count`: `58`
- `diary-index.json latest.slug`: `data-harvesting-is-not-inevitable-it-s-a-design-choice`
- `diary-latest.json item.slug`: `data-harvesting-is-not-inevitable-it-s-a-design-choice`
- `diary-feed.xml item count`: `58`
- `POST 0054` tag count preserved: `41`
- `POST 0057` distinct coexistence preserved with prior `l4-in-practice-5-reality-signals-that-kill-smart-systems`: `PASS`
- `cybernetics` bucket count after V30: `37`
- `vxcx` bucket count after V30: `1`
- `cloud-gaming` bucket count after V30: `1`
- `sitemap.xml` contains latest entry: `PASS`
- `sitemap.xml` contains new tag `vxcx`: `PASS`

## Live UI checks

- Home latest-post meta line date-only: `PASS`
- Diary card meta lines date-only: `PASS`
- `/diary/` preview contains all five imported posts under V28 preview-size policy: `PASS`
- `/diary/archive/` contains all five imported posts: `PASS`
- `POST 0054` structure markers preserved: `PASS`
- `POST 0055` arrow notation preserved: `PASS`
- `POST 0056` inline PDF link preserved: `PASS`
- `POST 0057` numbered structure preserved: `PASS`
- `POST 0058` numbered structure and arrow notation preserved: `PASS`
- No fake or placeholder image introduced on checked surfaces: `PASS`

## Tag membership checks

- Total tag membership checks: `143`
- Failures: `0`
- Method: for each imported post, every affected live tag page was checked for the presence of that post slug in rendered HTML

## Conclusion

V30 is live and structurally consistent:

- all five entries render
- latest-post switched correctly to `data-harvesting-is-not-inevitable-it-s-a-design-choice`
- all affected tag pages render and include their expected posts
- machine-readable surfaces, feed, sitemap, and images are live
- V23 date-only meta rendering and V28 preview-size behavior remain intact
