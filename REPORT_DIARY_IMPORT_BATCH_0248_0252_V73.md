# Diary import batch 0248–0252 V73

Contracts: SITE_DIARY_IMPORT_BATCH_0248_0252_V73 and SITE_DIARY_V73_RESUME_AFTER_READONLY_BUILD_STOP. Existing partial V73 candidate recovered; no V74, source re-import, new post, image transformation, architecture change or unrelated refactor.

## Git, authority and chronology

- Exact origin: https://github.com/Kot141078/kot141078.github.io.git ; branch main.
- Original initial local HEAD / V72 report: `fb13be8291b96b9315bf74d3eadd0d56ed39989f`. Merge-base before original fast-forward: same SHA.
- Original observed remote and synchronized HEAD: `39ab5db276fa998b56debc5272888ebe2ffde51d`. Original admission was clean before fetch; three intervening accepted October commits were retained.
- Recovery admission local and read-only ls-remote HEAD: `39ab5db276fa998b56debc5272888ebe2ffde51d`; no dirty-tree fetch/pull. Exact admitted partial state: 0 staged / 2 unstaged / 10 untracked. Full paths in RECOVERY_INTEGRITY_MANIFEST.md.
- Implementation local and pushed remote commit: `f22dd11d7d706fcbe13fddbfa59fef114c7c7b10` (`feat(diary): import entries 0248-0252 v73`). Scope: 95 inspected source/asset/generated/sitemap paths.
- Signing: commit.gpgsign=false, preserved; unsigned commits are correct.
- Report commit: immutable commit containing this report, with full SHA and final workflow/clean-state proof emitted in terminal after push; no self-reference or amend.
- Baseline Diary 247 / ENTRY 0247 / 2026-09-22 / the-human-in-the-loop-also-needs-a-budget. Final local and verified production Diary 252 / ENTRY 0252 / 2026-09-27 / maybe-uncle-jensen-huang-simply-forgot-to-mention-that-he-was-using-my-terminology.

| Entry | Effective date | Slug / canonical URL |
| --- | --- | --- |
| 0248 | 2026-09-23 | [speaking-the-same-language-does-not-mean-seeing-the-same-world](https://ivankotov.eu/diary/speaking-the-same-language-does-not-mean-seeing-the-same-world/) |
| 0249 | 2026-09-24 | [i-have-often-argued-that-personal-ai-memory-should-remain-local](https://ivankotov.eu/diary/i-have-often-argued-that-personal-ai-memory-should-remain-local/) |
| 0250 | 2026-09-25 | [when-ai-multiplies-hypotheses-scientific-taste-becomes-a-practical-problem](https://ivankotov.eu/diary/when-ai-multiplies-hypotheses-scientific-taste-becomes-a-practical-problem/) |
| 0251 | 2026-09-26 | [i-bought-a-5-000-graphics-card](https://ivankotov.eu/diary/i-bought-a-5-000-graphics-card/) |
| 0252 | 2026-09-27 | [maybe-uncle-jensen-huang-simply-forgot-to-mention-that-he-was-using-my-terminology](https://ivankotov.eu/diary/maybe-uncle-jensen-huang-simply-forgot-to-mention-that-he-was-using-my-terminology/) |

No post was invented for 2026-09-28 onward. All five posts have exactly one valid JPEG cover.

## Initial STOP and narrow recovery

Initial V73_STOP_BUILD_PERMISSION_DENIED: normal builder deleted generated diary/a-goal-can-be-installed/index.html, then WinError 5 prevented removal of its ReadOnly directory. No commit/push occurred in that attempt. Prior external diagnostics were preserved.

Read-only admission established exact known paths, source correspondence to original session, intact baseline publications/October files, +5/-0 sitemap set, remote equality and no active Git operation. It scanned 1711 generated paths, no junction/symlink/reparse point, no generated untracked/ignored content. Owner ACL was FullControl; 856 generated directories actually carried FILE_ATTRIBUTE_READONLY.

All ten existing candidate files were SHA-256-bound before repair. Only their generated-subtree ReadOnly flags were changed via standard SetFileAttributesW: 856/856 operations 0x11 -> 0x10; zero failures, zero remaining flags, all other bits preserved, immediate realpath/ancestor reparse checks for every operation. No ACL/ownership/elevation/AV changes, manual deletion, source/asset mutation or permanent builder patch. Exact paths and before/after attributes are in artifacts/diary-import-v73/READONLY_RECOVERY_AUDIT.md (copy of outside-repo audit).

The authorized first resumed build succeeded and itself restored the missing generated page. Second stabilization build yielded zero changes across 881 surfaces. All ten pre/post hashes remained identical through full local and remote validation.

## Source fidelity, duplicates and claim ceilings

No duplicate same-post identity: original preflight checked exact and near titles, opening/body, supplied URLs, alternative slugs/dates, publication linkage, full image SHA-256 and destination collisions across the 247-post baseline. No activity ID was available; none inferred. Recurring topics were not treated as duplicates. No private biography or household data was added.

Five preserved original bodies, titles, effective dates, short URLs and raw tags match this session’s authoritative V73 contract. Only indentation/paragraph normalization and clickable links were introduced before STOP; recovery changed none of the ten candidate bytes. Tag counts in order: 12,13,12,10,6. All raw hashtag capitalization and order retained; existing display aliases continue.

URL_RESOLUTION=BLOCKED_BY_POLICY / SHORT_URL_PRESERVED: original shell attempt rejected, bounded web opens unavailable, exact supplied URLs retained; no recovery retry or canonical fabrication.

Original text basename `Вставленный текст(20261104-204651).txt`, supplied 14549 bytes, SHA-256 `ba4abb2867a89dcf3bf3acf686ee70d8fcd91a434150ad817b16ac63cd03d7d3`; supplied complete original contract SHA-256 `77c2a17e12611888c3b0819ac6f32dcdcf4754677ab0639a529814fcd4731f35`. These identify provenance only, not locally verified original attachment bytes. All image hashes were actually measured on Windows and appear in IMAGE_AUDIT.md.

- 0248: information-loss thought experiment; 98 cm and 102 cm openings, 99 cm object; no inference about which opening was observed. Missing measurements remain missing; no digital-personhood claim.
- 0249: historical Google/Meta architectural descriptions, explicitly not privacy/independence guarantees. Storage location, custody, keys, recovery, continued access, permitted use and action authority remain distinct. Recall permission is not action permission.
- 0250: historical third-party Anthropic reporting, roughly 950 Claude agents / 21 hours / ART. Biological function explicitly remains unresolved. The thousand-candidate/ten-experiment example and overheating motor analogy remain hypothetical. No discovery by this author, independent validation, new c effect or peer-review claim.
- 0251: editorial, hypothetical consumer story. Ross and Nika are conditional future c characters, not deployed entities, consciousness, lawful identity or operational integrations. €5,000, GeForce NOW, DGX Spark-like, Telegram, Ray-Ban Meta, NVIDIA framing, jokes and conditional voice retained. No private household inventory, sponsorship or product endorsement added.
- 0252: humorous Jensen Huang reference, not plagiarism/priority evidence, endorsement, external recognition or achieved AGI/c. Advanced Global Intelligence and Artificial General Intelligence remain distinct; model/agent/memory/tool does not automatically become c. Emoji, five future questions and both first-party links retained.

## Gates and preserved site work

V23/V28/V59/V69, five latest in exact descending order, home latest, raw/canonical tags, responsive search, 0216 five-image and 0233 three-image galleries: PASS. Build determinism, source/front matter schema, all changed HTML/JSON/JSON-LD/XML, local links/images, no duplicate IDs/private-path leaks, canonical/OG and Unicode/emoji: PASS. Parsed 958 HTML, 125 JSON/JSON-LD files, 970 inline JSON-LD blocks, 5 XML; 3440 changed-page internal links checked. Full machine-readability gate: PASS, 8 Python stages and 5 schemas.

All protected publication and discovery files remain byte-identical to synchronized HEAD; homepage differs only in latest slot. October 18 ongoing-R&D wording, October 25 CI publication/DOIs/rights/qualification/discovery and PR #25 contextual links retained. Seventeen old post-page changes are related-card selection only, with remainder equal to baseline. No publication/evidence/research-status/rights/legal/corpus transition.

Sitemap membership: 346 -> 351, exactly +5 authorized Diary HTML URLs, -0 original URLs, +0 tags/images/JSON. Full added/removed sets in SITEMAP_DELTA.md; complete before/after sets in SITEMAP_URL_SETS.json. Continuity Instrument and all named protected routes retained. Local/deployed semantic set equality PASS.

## Visuals, production and workflows

Ten local PNGs and seven-page A4 PDF plus six remote PNGs created at C:/Users/kotov/Downloads/111/diary-v73-visual/ and inspected. Required 1440x900 and 390x844 viewport checks found zero horizontal overflow, failed image decodes or JavaScript errors; search by date and raw tag plus Escape pass. V69 external card is World Intelligence at 06, Open book.

Cache-busted production verification: 100 non-asset routes and 5/5 cover assets. Correct count/latest/body/canonical/source/tags/images and sitemap; all 54 affected noindex tag surfaces checked. Covers byte-identical. Text is identical after only CRLF/LF transport normalization on four pre-existing routes, documented in POST_DEPLOY_CHECK.md; no semantic loss.

- Machine readability: `41916466680`, completed/success ([run](https://github.com/Kot141078/kot141078.github.io/actions/runs/41916466680)).
- pages build and deployment: `41916465522`, completed/success ([run](https://github.com/Kot141078/kot141078.github.io/actions/runs/41916465522)).

Report-commit Pages/Machine workflow IDs, final HEAD==origin/main, 0 staged/unstaged/untracked and no active Git operation are checked and emitted in final terminal closeout after report push. This immutable report does not pre-claim those future checks.

## Blockers and manual remainder

At implementation production verification: no unresolved local/source/sitemap/deployment blocker; original filesystem STOP resolved within owner-authorized scope. No rollback needed.

DRIVE_JOURNAL=NOT_UPDATED: bounded Drive discovery did not identify an unambiguous owning site/Diary journal. Topical Ester wording, CGDR, perception and semantic-watch journals were not repurposed. No parallel journal or routine-release research-ledger entry created.

Search Console remains manual: request the five canonical entries (priority 1), optionally Diary (priority 2), optionally resubmit sitemap (priority 3). Never submit noindex tags, image URLs, feed or JSON. See SEARCH_CONSOLE_SUBMISSION_PLAN_V73.md.

Audit JSON copies use repository LF line endings; their external original receipts remain untouched and parsed content is identical. ReadOnly Markdown audit copy is byte-identical to its external original.
