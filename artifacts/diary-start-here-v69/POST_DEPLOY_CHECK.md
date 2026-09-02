# V69 Post-Deploy Check

Implementation commit: `89094c4b4dc77c7471d9316d268603949e9ab7e9`

Cache-busting used fresh query keys and no-cache request headers. Post-deploy verdict: `PASS`.

## Deployment workflows

| Workflow | Run ID | Head | Conclusion |
| --- | ---: | --- | --- |
| Pages build and deployment | `33618736403` | `89094c4b4dc77c7471d9316d268603949e9ab7e9` | success |
| Machine readability | `33618737115` | `89094c4b4dc77c7471d9316d268603949e9ab7e9` | success |

The implementation commit has a verified good GPG signature from `Ivan Kotov <kotovivan78@gmail.com>`, key `75D1828676B0D0EC`.

## Required HTTP routes

All returned HTTP 200:

1. `https://ivankotov.eu/diary/`
2. `https://ivankotov.eu/diary/start-here/`
3. `https://ivankotov.eu/world-intelligence/`
4. `https://ivankotov.eu/diary/we-are-building-a-partner/`
5. `https://ivankotov.eu/diary/why-id-put-an-ai-rack-in-my-garage/`
6. `https://ivankotov.eu/diary/the-question-behind-c-a-b-is-not-whether-an-ai-can-look-consistent-over-time/`
7. `https://ivankotov.eu/diary/the-ai-system-is-not-the-model/`
8. `https://ivankotov.eu/diary/many-people-now-speak-of-disappointment-with-artificial-intelligence/`
9. `https://ivankotov.eu/diary/published-volume-i-of-qubit-of-hope/`
10. `https://ivankotov.eu/diary-start-here.json`
11. `https://ivankotov.eu/sitemap.xml`

The external card image also returned HTTP 200 and was byte-identical to the local canonical PNG: SHA-256 `ec85ab66021963733e2de6a6ea14b6a45f3bae6dbc601d939feade31f3e38e62`.

## Remote semantic checks

- `/diary/`: exact six-card curated order, World Intelligence at position 06.
- `/diary/start-here/`: exact same six-card order.
- Section copy: exact requested V69 wording on both surfaces.
- `diary-start-here.json`: five Diary `items`, one `external_routes` record at position 6.
- World Intelligence CTA: `Open book`.
- World Intelligence canonical target: `/world-intelligence/`; no fake Diary target.
- Qubit Volume I: still reachable, absent only from Start here.
- Diary count/latest: 230 / ENTRY 0230 / 2026-09-01.
- V23: pass.
- V28: pass; latest preview remains exactly five cards.
- V59: pass.
- ENTRY 0216 gallery: pass.
- Broken loaded images: 0.
- Horizontal overflow: 0 at 1440x900 and 390x844.

## Sitemap parity

- Final local root URL count: 322.
- Final deployed root URL count: 322.
- Local/deployed sorted-set SHA-256: `1099a543afa33c1ad335278f2af0b5a8b68984618478490365463409fcac5fc1`.
- Added URLs: 0.
- Removed URLs: 0.
- Noindex tag additions: 0.
- Machine endpoint additions: 0.

## Remote visual receipts

Output root: `C:\Users\kotov\Downloads\111\diary-start-here-v69-visual\`

| Receipt | Bytes | SHA-256 |
| --- | ---: | --- |
| `final-remote-diary-start-here-desktop-1440x900.png` | 375,807 | `149c6b7d9ed790ca4ee5f656043cf701011e00e187ee75cd5aab8c7c8a09aa33` |
| `final-remote-diary-start-here-mobile-390x844.png` | 85,471 | `1bc44eb309183684af610531c7379771f060381397838ee43f6cf75cce6efdc0` |
| `final-remote-world-intelligence-card-desktop-1440x900.png` | 275,582 | `fa202de7b3008c6a460e388a3123a0131c98508f74a7f067837e6bdb0780c70e` |

All three were visually inspected. Cards, text, image proportions, numbering, CTA, mobile stacking, and V59 visual language pass.

## Regression boundary

Homepage latest, site-global Start here, Distinctions, Corpus and its status axes, Open Problems, Changes, Vision, ESTHER-RP-001, Publications, World Intelligence boundary, Qubit boundary, `robots.txt`, `llms.txt`, `llms-full.txt`, and sitemap membership remain intact. No scientific, implementation, validation, entity, personhood, B0, Theoretical Core, Living Corpus, or publication status changed.
