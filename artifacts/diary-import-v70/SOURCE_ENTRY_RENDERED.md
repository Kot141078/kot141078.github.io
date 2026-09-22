# V70 Source-to-Rendered Audit

Implementation commit: `6564b9f1691c68fd1a7e1e744e76a28c9c3d3aac`

## Intake boundary

V70 resumed from an owner-authorized pre-existing candidate at `79 staged / 0 unstaged / 0 untracked`. Exactly five Markdown sources were added. No existing Diary source was modified, and no reset, stash, clean, checkout, or restore was used.

## Mapping

| Entry | Source | Rendered route | Effective date | Primary image | Extra images |
| --- | --- | --- | --- | --- | ---: |
| 0231 | `content/diary/the-agent-is-entering-the-payment-rail.md` | `/diary/the-agent-is-entering-the-payment-rail/` | 2026-09-02 | `cover.jpg` | 0 |
| 0232 | `content/diary/meta-has-just-published-something-more-important-than-another-model-benchmark-an-ai-architecture-in-which-the-durable-part-of-the-system-lives-outside-the-model.md` | `/diary/meta-has-just-published-something-more-important-than-another-model-benchmark-an-ai-architecture-in-which-the-durable-part-of-the-system-lives-outside-the-model/` | 2026-09-04 | `cover.jpg` | 0 |
| 0233 | `content/diary/i-do-not-just-want-ai-in-a-game.md` | `/diary/i-do-not-just-want-ai-in-a-game/` | 2026-09-06 | `cover.jpg` | 2 |
| 0234 | `content/diary/ai-is-not-only-a-productivity-multiplier-it-is-a-strategy-multiplier.md` | `/diary/ai-is-not-only-a-productivity-multiplier-it-is-a-strategy-multiplier/` | 2026-09-07 | `cover.jpg` | 0 |
| 0235 | `content/diary/ai-scale-needs-three-licenses.md` | `/diary/ai-scale-needs-three-licenses/` | 2026-09-08 | `cover.jpg` | 0 |

The generator projects these sources into entry pages, the five-card Diary preview, archive, feed, machine JSON, normalized tag pages, related cards, homepage latest, and sitemap.

## Rendered-state checks

- `diary-index.json` count: 235.
- Latest: ENTRY 0235 / 2026-09-08.
- Latest five order: 0235, 0234, 0233, 0232, 0231.
- Homepage latest: ENTRY 0235.
- Feed includes all five in descending date order.
- ENTRY 0233 source declares two `extra_images`; rendered DOM contains one lead plus two gallery images in exact source order.
- ENTRY 0235 retains an empty source/social URL and renders no invented LinkedIn trace.
- Duplicate source slug count: zero.
- New-page duplicate HTML ID count: zero.
- No historical post body was rewritten.

## Regression markers

V23 date-only metadata, V28 five-card preview, V59 landing/search/tag behavior, V69 Start-here, and ENTRY 0216's existing five-image gallery all pass.
