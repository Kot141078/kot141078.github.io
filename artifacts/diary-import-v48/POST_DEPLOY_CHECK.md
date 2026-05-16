# Post Deploy Check V48

Implementation commit checked: `e76d24390542cb49a17332e5e42a3525eaf73450`

Deployment target: `https://ivankotov.eu`

## Remote HTTP Results

- Entry URLs: 6 checked, 6 returned 200.
- Asset URLs: 5 checked, 5 returned 200.
- Affected tag URLs: 56 checked, 0 non-200.
- Diary home: 200.
- Site home: 200.
- `diary-index.json`: 200.
- `diary-feed.xml`: 200.
- `sitemap.xml`: 200.

## Remote Data Results

- `diary-index.json` count: 151.
- `diary-index.json` latest: `2026-05-16` / `i-was-an-only-child`.
- Home latest-post points to `i-was-an-only-child`.
- Top remote ordering:
  - `2026-05-16` / `i-was-an-only-child`
  - `2026-05-15` / `what-should-a-child-facing-ai-be-allowed-to-remember`
  - `2026-05-15` / `grief-is-not-a-user-error`
  - `2026-05-14` / `a-serious-ai-future-should-not-make-human-experience-socially-disposable-0146`
  - `2026-05-13` / `the-central-question-is-no-longer-only-what-exactly-are-we-scaling`
  - `2026-05-12` / `arq-cq-integration-addendum-v0-1-is-now-public`
- Sitemap contains all six new entry URLs and all affected tag URLs checked in this pass.

## Contract-Specific Checks

- V23 date-only meta fix: intact on all six new entries.
- V28 five-entry preview fix: intact, latest section has 5 entry cards.
- ENTRY 0144 image-less rendering: no `entry-cover` and no placeholder text.
- ENTRY 0147 no-source URL handling: no LinkedIn origin trace rendered.
- ENTRY 0148 links: public archive DOI, full technical DOI, and GitHub release render as anchors.
- ENTRY 0149 links: Research archive and Technical corpus render as anchors.
- Duplicate guard: no exact duplicate import occurred; ENTRY 0146 is the explicitly authorized same-title / near-body variant.

## Remote Entry URLs

- https://ivankotov.eu/diary/arq-cq-integration-addendum-v0-1-is-now-public/
- https://ivankotov.eu/diary/the-central-question-is-no-longer-only-what-exactly-are-we-scaling/
- https://ivankotov.eu/diary/a-serious-ai-future-should-not-make-human-experience-socially-disposable-0146/
- https://ivankotov.eu/diary/grief-is-not-a-user-error/
- https://ivankotov.eu/diary/what-should-a-child-facing-ai-be-allowed-to-remember/
- https://ivankotov.eu/diary/i-was-an-only-child/

## Remote Asset URLs

- https://ivankotov.eu/assets/diary/the-central-question-is-no-longer-only-what-exactly-are-we-scaling/cover.jpg
- https://ivankotov.eu/assets/diary/a-serious-ai-future-should-not-make-human-experience-socially-disposable-0146/cover.jpg
- https://ivankotov.eu/assets/diary/grief-is-not-a-user-error/cover.jpg
- https://ivankotov.eu/assets/diary/what-should-a-child-facing-ai-be-allowed-to-remember/cover.jpg
- https://ivankotov.eu/assets/diary/i-was-an-only-child/cover.jpg
