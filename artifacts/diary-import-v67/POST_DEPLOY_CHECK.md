# V67 Post-Deploy Check

Implementation commit: `3496009a4fbc5516d46166a83e7354d4220d2663`

Cache-bust key: `3496009a4fbc5516d46166a83e7354d4220d2663`

## Deployment runs

| Workflow | Run ID | Head | Conclusion |
| --- | ---: | --- | --- |
| Pages build and deployment | `33567098380` | `3496009a4fbc5516d46166a83e7354d4220d2663` | success |
| Machine readability | `33567099767` | `3496009a4fbc5516d46166a83e7354d4220d2663` | success |

The implementation commit's GPG signature verified successfully before deployment validation.

## Cache-busted HTTP result

All 82 required cache-busted requests returned HTTP 200:

- 19 home, Diary, JSON/XML, publication, and protected regression routes;
- 6 new entry routes;
- 6 new image routes;
- 51 affected detail-tag routes.

Core semantic results:

- `/`: homepage latest Diary slot is ENTRY 0223.
- `/diary/`: count 223, latest date 2026-08-24, exactly five latest cards.
- `/diary/archive/`: all six V67 entries are present.
- `/diary/tags/`: canonical display remains present and the page retains `noindex`.
- `/diary-index.json`: 223 items; latest ENTRY 0223 / 2026-08-24.
- `/diary-tags.json`: valid JSON.
- `/diary-latest.json`: ENTRY 0223 / 2026-08-24.
- `/diary-feed.xml`: valid XML.
- `/sitemap.xml`: valid XML with 315 URLs, exactly equal to the final local set.

## Entry routes

All six returned HTTP 200 and passed their required semantic-anchor checks:

1. `https://ivankotov.eu/diary/ai-is-eating-all-the-memory/`
2. `https://ivankotov.eu/diary/today-i-watched-my-cat-proudly-riding-the-robot-vacuum/`
3. `https://ivankotov.eu/diary/the-second-missing-layer-in-home-robotics-repair-without-identity-capture/`
4. `https://ivankotov.eu/diary/we-may-be-solving-ai-safety-at-the-wrong-level/`
5. `https://ivankotov.eu/diary/people-keep-asking-whether-ai-will-make-humanity-better-or-worse/`
6. `https://ivankotov.eu/diary/a-goal-can-be-installed/`

- Remote V23: `PASS`; visible card/home metadata is date-only.
- Remote V28: `PASS`; exact five-card order is ENTRY 0223, 0222, 0221, 0220, 0219. ENTRY 0218 remains sixth-most-recent.
- Remote V59: `PASS`; compact landing cards, search, canonical tag labels, six-tag display cap, and protected `L4` remain intact.
- Remote duplicate guard: `PASS`; each V67 slug and activity ID occurs once in the 223-record remote index.

## Image routes

All six returned HTTP 200, decoded successfully, used the expected media type, and matched supplied/local bytes:

| Entry | Asset | Bytes | SHA-256 | Remote type |
| --- | --- | ---: | --- | --- |
| 0218 | `assets/diary/ai-is-eating-all-the-memory/cover.jpg` | 209751 | `0b0be05f81a949916f3861552e1c705bd27fff02dec0077c81667d97124e01bd` | `image/jpeg` |
| 0219 | `assets/diary/today-i-watched-my-cat-proudly-riding-the-robot-vacuum/cover.png` | 2180640 | `80a8d2a81107146a7908034703b24541ee119af0f2dc524cdd225f75e271ec57` | `image/png` |
| 0220 | `assets/diary/the-second-missing-layer-in-home-robotics-repair-without-identity-capture/cover.png` | 2066866 | `b835bcfffbd00cad4c3c925485e6f89e203b5cd5fffd3de00c5c4a92fb5ada24` | `image/png` |
| 0221 | `assets/diary/we-may-be-solving-ai-safety-at-the-wrong-level/cover.png` | 2847712 | `b42943f3dde0faa62043502a4fdd763cbf2669777c4b3e274c36c2e2c32870f8` | `image/png` |
| 0222 | `assets/diary/people-keep-asking-whether-ai-will-make-humanity-better-or-worse/cover.jpg` | 265678 | `4199c9115b891d7c827e2a5b9c4abc462eacc6a088faadbbb7d3d704361df1fe` | `image/jpeg` |
| 0223 | `assets/diary/a-goal-can-be-installed/cover.jpg` | 180357 | `838d7c0e1c46a9056f851f4e3aaaf99c4bcca8dc08c7409dcf54f1b05b162d1f` | `image/jpeg` |

ENTRY 0219, 0220, and 0221 begin with valid PNG signatures and display normally. Remote asset verdict: 6/6 byte-identical; transformed count 0.

## Affected tag routes

All 51 affected detail-tag routes returned HTTP 200, contained `noindex`, and remained absent from `sitemap.xml`:

`ai-agents`, `ai-alignment`, `ai-architecture`, `ai-governance`, `ai-infrastructure`, `ai-safety`, `aiagents`, `aialignment`, `aiarchitecture`, `aigovernance`, `aiinfrast`, `aiinfrastructure`, `aiinsurance`, `aimotivation`, `aisafety`, `antitrust`, `artificialintelligence`, `cequalsaplusb`, `cybernetics`, `digital-entities`, `digital-identity`, `digital-sovereignty`, `digitalentities`, `digitalidentity`, `digitalsovereignty`, `dram`, `embodied-ai`, `embodiedai`, `future-of-ai`, `futureofai`, `governance`, `human-ai`, `humanai`, `l4-boundary`, `l4-witness`, `l4`, `localai`, `long-lived-ai`, `long-lived-systems`, `longlivedai`, `multi-agent-systems`, `multiagentsystems`, `persistent-ai`, `persistentai`, `reality-bound-ai`, `reality-bound`, `reality-boundary`, `righttorepair`, `robotics`, `semiconductors`, `temporalaipresence`.

Tag-page sitemap additions: 0.

## Sitemap and protected surfaces

- Pre-V67 local/deployed set: 309/309 and equal.
- Final local/deployed set: 315/315 and equal.
- Added: exactly six V67 Diary HTML routes.
- Removed: 0.
- Noindex tag additions: 0.
- Machine endpoint additions: 0.

The following protected routes returned HTTP 200 and remained semantically intact: `/start-here/`, `/distinctions/`, `/corpus/`, `/corpus/current-state/`, `/corpus/open-problems/`, `/corpus/changes/`, `/vision/`, `/publications/`, `/publications/esther-rp-001/`, and `/publications/motivational-formation-c-v0-1/`. Protocol Map, Failures, install-c, robots.txt, llms.txt, and llms-full.txt were also regression-checked locally; V67 changed none of those tracked surfaces.

Living Corpus counts and statuses, Baseline B0, Theoretical Core, V63 agent/c sentence counts, Vision status, and publication maturity remain unchanged. No Living Corpus status transition was generated.

## Remote visual receipts

Output root: `C:\Users\kotov\Downloads\111\diary-v67-visual\`

| Artifact | Dimensions | SHA-256 |
| --- | --- | --- |
| `final-remote-diary-desktop-1440x900.png` | 1440x900 | `71e3821a72cdee4bfb02cfab05a6d98fd45543ed007300d89c875bdad6dc7d5f` |
| `final-remote-diary-mobile-390x844.png` | 390x844 | `c433e4aeb5ce934c18a985961961e11476f0e86469546aac4547a382a89fc3be` |
| `final-remote-home-desktop-1440x900.png` | 1440x900 | `cd1002271f254174e84952e323f4a79d0fe00441d56de23f2c83c388d0133a9c` |
| `final-remote-entry0219-desktop-1440x900.png` | 1440x900 | `3bfc2a7b44def35675df8bbd47f89f28c75c08457851b869bd803d726a6161e8` |
| `final-remote-entry0220-desktop-1440x900.png` | 1440x900 | `4744fb1a97c2ad2326e9ac492b3c6249370ddd509023d22d256387791f4baf79` |
| `final-remote-entry0223-desktop-1440x900.png` | 1440x900 | `96184edffba1e627e648da05a984b35bf2789fc1cee4226fe35364504c912b87` |

All six remote receipts show normal covers and structured text, with no horizontal overflow, broken images, tag-display regression, or corrupted PNG backgrounds. Remote visual verdict: `PASS`.
