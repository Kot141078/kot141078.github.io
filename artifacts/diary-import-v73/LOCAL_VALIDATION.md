# V73 local and regression validation

First resumed standard build succeeded; it recreated diary/a-goal-can-be-installed/index.html. Second stabilization build changed zero bytes across 881 generated surfaces. Full normal machine-readability gate passed (8 Python stages, 5 JSON schema contracts); its builder invocation also succeeded. tools/build_diary.py remains byte-identical to baseline.

| Check | Result |
| --- | --- |
| html | 958 |
| json | 125 |
| jsonld | 970 |
| xml | 5 |
| local_links | 3440 |
| images | 258 |

All changed/generated links resolve locally; duplicate HTML IDs, Windows private-path leaks in HTML, broken local images and parse failures are zero. New Markdown schema, body-to-render correspondence, title/date/source URL, canonical/OG, raw tag order, all ten recovery hashes, and five source/destination image byte identities pass.

V23 date-only; V28 exactly five latest in 0252,0251,0250,0249,0248 order; home latest 0252; V59 layout/search/raw-tag lookup/aliases, six-chip cap and noindex; V69 five Diary cards plus external World Intelligence at position 06 with Open book: PASS. ENTRY 0216 five-image and ENTRY 0233 three-image galleries: PASS.

The 2026-10-18 Ester wording is unchanged outside the generated latest slot. The 2026-10-25 CI route, DOIs, rights, qualification limits, machine discovery and PR #25 contextual links remain byte-identical. Full machine gate additionally verified 20 contextual priority links. Publications, B0, Theoretical Core, Living Corpus, Vision status, legal status, licensing and CI gates were not edited. No runtime/formation/corpus-maturity claim was advanced.

Seventeen existing post files changed only in their generated Continue from here related-card section; every other HTML component was compared to baseline and remains equal. No legitimate original cross-link was lost outside this expected selection.

- `diary/a-serious-ai-future-should-not-make-human-experience-socially-disposable/index.html`
- `diary/a-system-can-speak-fluently-remember-fragments-imitate-continuity-survive-a-restart-or-even-sound-emotionally-consistent-and-still-not-have-enough-evidence-for-a-personality-formation-claim/index.html`
- `diary/ai-as-a-camera-of-thought/index.html`
- `diary/ai-will-not-make-everyone-a-billionaire/index.html`
- `diary/c-calculus-governed-binding-stack-v0-1/index.html`
- `diary/every-now-and-then-between-my-usual-thoughts-on-ai-infrastructure-and-machine-intelligence-the-old-pc-geek-in-me-stages-a-small-rebellion/index.html`
- `diary/grief-is-not-a-user-error/index.html`
- `diary/i-do-not-just-want-ai-in-a-game/index.html`
- `diary/llms-are-not-the-ai/index.html`
- `diary/palantir-solves-a-real-problem-large-organizations-have-data-scattered-across-dozens-or-hundreds-of-disconnected-systems/index.html`
- `diary/pavel-durovs-original-speech-english-oslo-freedom-forum-june-2026/index.html`
- `diary/saturday-traffic-report-from-the-ai-highway/index.html`
- `diary/the-ai-transition-is-not-about-chatbots/index.html`
- `diary/the-question-behind-c-a-b-is-not-whether-an-ai-can-look-consistent-over-time/index.html`
- `diary/tokens-are-becoming-the-billable-unit-of-ai/index.html`
- `diary/what-body-should-an-ai-have/index.html`
- `diary/why-robots-should-be-raised-not-deployed/index.html`
