# V65 Post-Deploy Check

Implementation commit: `877ace71500feaacae8c3b174c3a0f96b7e61b64`

Cache-bust key: `v65-877ace71500f-20260901`

## Deployment runs

| Run | ID | Head | Conclusion |
| --- | ---: | --- | --- |
| Pages build and deployment | 33551658184 | `877ace71500feaacae8c3b174c3a0f96b7e61b64` | success |
| Pages deploy job | 100002389064 | `877ace71500feaacae8c3b174c3a0f96b7e61b64` | success |
| Machine readability | 33551659551 | `877ace71500feaacae8c3b174c3a0f96b7e61b64` | success |

## Required route result

Seventy-three cache-busted route checks returned HTTP 200:

- 9 core Diary/home/JSON/XML routes;
- 5 new entry routes;
- 5 new image routes;
- 46 affected tag routes;
- 8 protected regression routes.

Core results:

- `/`: latest Diary slot is ENTRY 0208.
- `/diary/`: count 211, date range through 2026-08-10, exactly five latest cards.
- `/diary/archive/`: all five V65 entries resolve from the archive.
- `/diary/tags/`: canonical tag display remains present.
- `/diary-index.json`: count 211, latest 2026-08-10 / ENTRY 0208 slug.
- `/diary-tags.json`: valid JSON.
- `/diary-latest.json`: ENTRY 0208.
- `/diary-feed.xml`: valid XML.
- `/sitemap.xml`: valid XML, 303 URLs.

## Entry routes

All returned HTTP 200 and exactly matched their signed Git blobs:

1. `https://ivankotov.eu/diary/ai-will-not-make-society-simpler/`
2. `https://ivankotov.eu/diary/ai-will-be-the-bearer-of-its-own-power/`
3. `https://ivankotov.eu/diary/what-happens-to-a-digital-system-when-the-person-who-carried-the-original-responsibility-is-no-longer-there/`
4. `https://ivankotov.eu/diary/what-exactly-are-we-entitled-to-infer-from-a-technical-signal/`
5. `https://ivankotov.eu/diary/palantir-solves-a-real-problem-large-organizations-have-data-scattered-across-dozens-or-hundreds-of-disconnected-systems/`

Remote V23: `PASS`. Remote V28: `PASS`, order 0208, 0207, 0206, 0205, 0204.

## Image routes

All returned HTTP 200, matched their signed Git blobs and supplied source bytes, and had distinct hashes:

| Entry | SHA-256 |
| --- | --- |
| 0204 | `7493db9fb42b299212b80fe95ab4f51841101562410282e829fef6e4f930edee` |
| 0205 | `2efd031d41f18987930a65d7b0f2c77700c906f8fcfcc86ba012b9796c3cd4da` |
| 0206 | `563952605b38f38fd0dd35d801a62ed5f05c33f2bfc941ffafaceab151ce5cac` |
| 0207 | `78f661f3ed9e9ab5caf8f55e31328416f9ffb202c04db99865b34e0763b81a05` |
| 0208 | `c97531558c092b1e780b0b9a7bb0396c7b58d2fe61189fcddf8e58cf69f6c77a` |

## Affected tag routes

All 46 affected tag routes returned HTTP 200, all 46 contained `noindex`, and none appeared in `sitemap.xml`:

`ai`, `ai-architecture`, `ai-ethics`, `ai-governance`, `ai-safety`, `aiagency`, `aiandsociety`, `aiarchitecture`, `aiautonomy`, `aicontinuity`, `aiethics`, `aigovernance`, `aiidentity`, `aiphilosophy`, `aisafety`, `artificial-intelligence`, `artificialintelligence`, `artificiallife`, `cocreation`, `cybernetics`, `dataarchitecture`, `digitalbeings`, `digitalcontinuity`, `digitallife`, `epistemology`, `future-of-ai`, `future-of-work`, `futureofai`, `futureofintelligence`, `futureofwork`, `governance`, `humanaicoexistence`, `humanaicollaboration`, `knowledgegraphs`, `machineintelligence`, `machineinterpretation`, `machinereadable`, `management`, `multimodalai`, `newformsoflife`, `ontology`, `palantir`, `philosophyofai`, `provenance`, `systems-thinking`, `systemsthinking`.

## Technical and publication checks

- PASC decision vocabulary: exact.
- PASC status block: exact.
- Boundaries operational list: exact.
- ENTRY 0208 permission expression: exact.
- Four publication/DOI anchors: present.
- Four publication/DOI targets: HTTP 200.
- Five LinkedIn activity IDs: each occurs once among the 211 `diary-index.json.items` records.

## Protected surfaces

The deployed responses matched the signed Git blobs:

- `/start-here/`
- `/corpus/`
- `/vision/`
- `/publications/esther-rp-001/`
- `/publications/`
- `/distinctions/`
- `/corpus/changes/`
- `/robots.txt`

No corpus JSON endpoint was added to the sitemap.

## Remote visual artifacts

Output root: `C:\Users\kotov\Downloads\111\diary-v65-visual\`

| Artifact | Dimensions | SHA-256 |
| --- | --- | --- |
| `final-remote-diary-desktop-1440x900.png` | 1440x900 | `2cf7fab9526d980226d47544e4ce1ff071f0bcb3733a0e850536294781db8789` |
| `final-remote-diary-mobile-390x844.png` | 390x844 | `ab5c5d31f1d0ab66ca54a596464aff477e439510ad1c94466683cfec05764f42` |
| `final-remote-home-desktop-1440x900.png` | 1440x900 | `0fc04ef5e7d32455541ca1edb7dbc34d7e06d8d87a9d345ce910e6900ac135ef` |
| `final-remote-entry0208-desktop-1440x900.png` | 1440x900 | `6e58e5443c677667a1a0c1765d59c2a970385caaa2878bba7f016a8b6f2bbd7d` |

All four were visually inspected. Five V65 images loaded on the remote Diary landing page, the 390 px layout had no horizontal overflow, and the latest/home/ENTRY 0208 surfaces matched the local validated state.

## Diagnostic notes

The first read-only remote script expected literal absolute-path text inside the archive; the archive correctly uses relative hrefs which resolve to the five canonical URLs. A second read-only check compared the deployed LF `vision/index.html` Git blob with a CRLF Windows worktree representation. Direct signed-Git-blob comparison proved exact deployed equality. Neither diagnostic caused a repository or deployment mutation.

Final post-deploy verdict: `PASS`.
