# POST_DEPLOY_CHECK_V29

## Live URL Status

All `61` checked production URLs returned `200` after implementation commit `0ef5639c0ffaba9afdcdf6e06ff4cde7f8a3106d` reached `origin/main`.

Checked URL groups:

- Core pages: `/`, `/diary/`, `/diary/archive/`, `/diary/tags/`
- New entry pages:
- `https://ivankotov.eu/diary/how-not-to-become-dumber-than-your-system-at-a-certain-point/`
- `https://ivankotov.eu/diary/why-oracle-ai-creates-addiction-and-why-entities-dont/`
- `https://ivankotov.eu/diary/the-future-is-not-an-event-it-is-a-process/`
- `https://ivankotov.eu/diary/l4-in-practice-5-reality-signals-that-kill-smart-systems/`
- `https://ivankotov.eu/diary/hgi-why-am-i-only-hearing-this-now-and-why-general-is-never-a-default/`
- Previous latest entry control check:
- `https://ivankotov.eu/diary/from-better-chat-to-stable-presence/`
- Machine-readable outputs:
- `https://ivankotov.eu/diary-index.json`
- `https://ivankotov.eu/diary-tags.json`
- `https://ivankotov.eu/diary-latest.json`
- `https://ivankotov.eu/diary-feed.xml`
- `https://ivankotov.eu/sitemap.xml`
- New image assets:
- `https://ivankotov.eu/assets/diary/how-not-to-become-dumber-than-your-system-at-a-certain-point/cover.jpg`
- `https://ivankotov.eu/assets/diary/why-oracle-ai-creates-addiction-and-why-entities-dont/cover.jpg`
- `https://ivankotov.eu/assets/diary/the-future-is-not-an-event-it-is-a-process/cover.jpg`
- `https://ivankotov.eu/assets/diary/l4-in-practice-5-reality-signals-that-kill-smart-systems/cover.jpg`
- `https://ivankotov.eu/assets/diary/hgi-why-am-i-only-hearing-this-now-and-why-general-is-never-a-default/cover.jpg`
- Affected tag pages:
- `https://ivankotov.eu/diary/tags/hgi/`
- `https://ivankotov.eu/diary/tags/agi/`
- `https://ivankotov.eu/diary/tags/advanced-global-intelligence/`
- `https://ivankotov.eu/diary/tags/human-oversight/`
- `https://ivankotov.eu/diary/tags/ai-safety/`
- `https://ivankotov.eu/diary/tags/ai-act/`
- `https://ivankotov.eu/diary/tags/governance/`
- `https://ivankotov.eu/diary/tags/audit-trail/`
- `https://ivankotov.eu/diary/tags/cybernetics/`
- `https://ivankotov.eu/diary/tags/information-theory/`
- `https://ivankotov.eu/diary/tags/l4/`
- `https://ivankotov.eu/diary/tags/reality-boundary/`
- `https://ivankotov.eu/diary/tags/sovereign-entities/`
- `https://ivankotov.eu/diary/tags/local-ai/`
- `https://ivankotov.eu/diary/tags/decentralized-ai/`
- `https://ivankotov.eu/diary/tags/ai-architecture/`
- `https://ivankotov.eu/diary/tags/reality-bound-ai/`
- `https://ivankotov.eu/diary/tags/agentic-ai/`
- `https://ivankotov.eu/diary/tags/systems-engineering/`
- `https://ivankotov.eu/diary/tags/edge-ai/`
- `https://ivankotov.eu/diary/tags/autonomy/`
- `https://ivankotov.eu/diary/tags/auditability/`
- `https://ivankotov.eu/diary/tags/operational-resilience/`
- `https://ivankotov.eu/diary/tags/energy-budget/`
- `https://ivankotov.eu/diary/tags/reliability-engineering/`
- `https://ivankotov.eu/diary/tags/eu-ai-act/`
- `https://ivankotov.eu/diary/tags/compliance/`
- `https://ivankotov.eu/diary/tags/gpus/`
- `https://ivankotov.eu/diary/tags/compute/`
- `https://ivankotov.eu/diary/tags/thermals/`
- `https://ivankotov.eu/diary/tags/mlops/`
- `https://ivankotov.eu/diary/tags/systems-thinking/`
- `https://ivankotov.eu/diary/tags/human-ai/`
- `https://ivankotov.eu/diary/tags/cognitive-architecture/`
- `https://ivankotov.eu/diary/tags/philosophy-of-technology/`
- `https://ivankotov.eu/diary/tags/ai-entities/`
- `https://ivankotov.eu/diary/tags/long-term-thinking/`
- `https://ivankotov.eu/diary/tags/human-in-the-loop/`
- `https://ivankotov.eu/diary/tags/continuity/`
- `https://ivankotov.eu/diary/tags/ai-audit/`
- `https://ivankotov.eu/diary/tags/ser/`

## Live Data Checks

- `diary-index.json count = 53`: pass
- `diary-index.json latest.slug = hgi-why-am-i-only-hearing-this-now-and-why-general-is-never-a-default`: pass
- `diary-latest.json item.slug = hgi-why-am-i-only-hearing-this-now-and-why-general-is-never-a-default`: pass
- live per-date ordering:
- `2026-02-08 -> how-not-to-become-dumber-than-your-system-at-a-certain-point`
- `2026-02-10 -> why-oracle-ai-creates-addiction-and-why-entities-dont`
- `2026-02-15 -> the-future-is-not-an-event-it-is-a-process`
- `2026-02-17 -> l4-in-practice-5-reality-signals-that-kill-smart-systems`
- `2026-02-20 -> hgi-why-am-i-only-hearing-this-now-and-why-general-is-never-a-default`
- `POST 0052` tag count in live `diary-index.json` = `22`: pass
- live `cybernetics` bucket count = `1`: pass
- live `cybernetics` display label = `Cybernetics`: pass
- live `cybernetics` entry count = `34`: pass
- live `diary-feed.xml` item count = `53`: pass
- live `sitemap.xml` includes `hgi-why-am-i-only-hearing-this-now-and-why-general-is-never-a-default`: pass
- live `sitemap.xml` includes `continuity` tag page: pass

## Live UI Checks

- home latest-post slot shows `HGI - why am I only hearing this now? And why "General" is never a default.`: pass
- home latest-post link points to `/diary/hgi-why-am-i-only-hearing-this-now-and-why-general-is-never-a-default/`: pass
- home latest-post meta line contains date only: pass
- `/diary/` contains all five imported posts under the current V28 preview policy: pass
- `/diary/archive/` contains all five imported posts: pass
- diary card meta lines contain date only: pass
- `POST 0049` preserves `Two quiet bridges` and both bridge notes: pass
- `POST 0050` preserves `Ask -> instant answer -> instant relief -> repeat.`: pass
- `POST 0052` preserves all numbered signal sections and the final two-line closing: pass
- `POST 0053` preserves acronym expansions and the explicit bridge sentence: pass

## Live Tag Page Checks

- Affected unique tag pages checked: `41`
- Total slug-presence checks across those pages: `57`
- Every affected live tag page contains the expected imported slug(s): pass

## Conclusion

- V29 deploy is live.
- All five posts are published as real diary entries.
- `POST 0049` mixed-case duplicate `Cybernetics` hashtags resolved cleanly into one canonical bucket with no split.
- `POST 0052` kept its full long tag set in live HTML and JSON outputs.
- The V23 date-only meta rendering fix remains intact.
- The V28 `/diary/` preview-size fix remains intact.
- No fake image or placeholder asset was introduced.
