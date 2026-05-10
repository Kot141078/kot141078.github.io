# Post Deploy Check V46

Implementation commit checked: `5dbed14132fea46437a595c9bd8046fe594a18bc`

Deployment target: `https://ivankotov.eu`

## Remote HTTP Results

- Entry URLs: 6 checked, 6 returned 200.
- Asset URLs: 5 checked, 5 returned 200.
- Affected tag URLs: 48 checked, 0 non-200.
- Home page: 200.
- `diary-index.json`: 200.
- `diary-feed.xml`: 200.
- `sitemap.xml`: 200.

## Remote Data Results

- `diary-index.json` count: 141.
- `diary-index.json` latest: `2026-05-09` / `the-next-ai-risk-may-not-look-like-rebellion`.
- Home latest-post points to entry 0139.
- Sitemap contains all six new entry URLs and all affected tag URLs checked in this pass.

## Contract-Specific Checks

- V23 date-only meta fix: intact.
- V28 five-entry preview fix: intact, latest section has 5 entry cards.
- 0136 image-less render: no `<img>` tag on the entry page.
- 0137 release links: all three GitHub release/download links render as clickable anchors.
- 0138 hashtags parsed: `ArtificialIntelligence`, `OpenScience`, `AIAdmissibility`, `KnowledgeInfrastructure`, `FutureOfScience`.
- 0139 effective date: `2026-05-09`.
- 0139 raw typo recorded: `08-09-2026`.
- Duplicate guard: no pre-existing duplicate LinkedIn URL found before import; each supplied LinkedIn URL appears exactly once in `content/diary` after import.

## Remote Entry URLs

- https://ivankotov.eu/diary/one-of-the-most-important-tests-of-any-serious-architecture-is-simple/
- https://ivankotov.eu/diary/humanoid-robotics-shows-that-ai-safety-is-becoming-operational-and-physical/
- https://ivankotov.eu/diary/today-i-am-sharing-qubit-of-hope-volume-iii/
- https://ivankotov.eu/diary/qubit-of-hope-volume-iii-is-now-available/
- https://ivankotov.eu/diary/some-people-will-not-enter-science-through-the-usual-door/
- https://ivankotov.eu/diary/the-next-ai-risk-may-not-look-like-rebellion/
