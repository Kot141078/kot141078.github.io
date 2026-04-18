# kot141078.github.io

Static user-site repository for `ivankotov.eu`.

## What this is

This repository serves a minimal public entry page for:

- `advanced-global-intelligence`
- `sovereign-entity-recursion`
- `ester-reality-bound`
- `ester-clean-code`

It also includes canonical, identity, authority/evidence, distinctions, and entry layers through:

- `start-here`
- `diary`
- `diary archive`
- `diary tags`
- `questions`
- `topics`
- `ai-governance`
- `local-first-ai`
- `long-lived-ai-entities`
- `library`
- `downloads`
- `services`
- `use-cases`
- `contact`
- `about`
- `corpus-map`
- `distinctions`
- `misreadings`
- `c = a + b`
- `L4`
- `Actor Grounding Layer`
- `SER`
- `Qubit of Hope — Volume I`
- `Qubit of Hope — Volume II`
- `glossary`
- `reading-path`
- `publications`
- `releases`
- `evidence`
- `llms.txt`
- `diary-index.json`
- `diary-latest.json`
- `diary-tags.json`
- `diary-feed.xml`
- `actor-grounding-layer.json`
- `qubit-of-hope-volume-ii.json`
- `canonical-map.json`
- `works-index.json`
- `library-index.json`
- `downloads-index.json`
- `services.json`
- `use-cases.json`
- `contact.json`
- `about.json`
- `start-here.json`
- `questions.json`
- `topics-index.json`
- `distinctions.json`
- `misreadings.json`
- `humans.txt`

Current site layer: `v1.5` diary engine + archive surfaces layer on top of `v1.4` diary foundation + visual tightening, `v1.3` AGL + Volume II integration, topics/query-intent layer `v1.0`, services/use-cases/contact layer `v0.9`, library/downloads layer `v0.8`, entry/questions layer `v0.7`, distinctions/misreadings layer `v0.6`, identity/corpus-map layer `v0.5`, authority/evidence layer `v0.4`, and canonical layer `v0.3`.

It is a plain static site: HTML + CSS + JSON/JSON-LD + XML + plain text, with small Python stdlib helpers for generated diary surfaces. There is no package manager, framework, backend, or CMS.

Diary engine surfaces are prepared through plain Markdown source files in `content/diary/`, image folders in `assets/diary/`, and the stdlib-only helper `tools/build_diary.py`, which generates `diary/index.html`, `diary/archive/index.html`, `diary/tags/index.html`, per-post pages, `diary-index.json`, `diary-tags.json`, `diary-feed.xml`, and the home latest-post slot state.

## Primary domain

- Primary custom domain: `ivankotov.eu`
- GitHub Pages source: branch `main`, path `/`

## Canonical, identity, evidence, distinctions, and entry pages

- `index.html`
- `start-here/index.html`
- `diary/index.html`
- `diary/archive/index.html`
- `diary/tags/index.html`
- `questions/index.html`
- `topics/index.html`
- `ai-governance/index.html`
- `local-first-ai/index.html`
- `long-lived-ai-entities/index.html`
- `library/index.html`
- `downloads/index.html`
- `services/index.html`
- `use-cases/index.html`
- `contact/index.html`
- `about/index.html`
- `corpus-map/index.html`
- `distinctions/index.html`
- `misreadings/index.html`
- `advanced-global-intelligence/index.html`
- `c-a-plus-b/index.html`
- `l4/index.html`
- `actor-grounding-layer/index.html`
- `ser/index.html`
- `qubit-of-hope/index.html`
- `qubit-of-hope-volume-ii/index.html`
- `glossary/index.html`
- `reading-path/index.html`
- `publications/index.html`
- `releases/index.html`
- `evidence/index.html`

## Machine-readable layer

- `llms.txt` — compact machine-facing site guide
- `diary-index.json` — machine-readable diary archive index
- `diary-latest.json` — machine-readable latest diary slot state
- `diary-tags.json` — machine-readable diary tag index
- `diary-feed.xml` — machine-readable RSS feed for the diary archive
- `actor-grounding-layer.json` — machine-readable grounding layer node
- `qubit-of-hope-volume-ii.json` — machine-readable narrative continuation node
- `canonical-map.json` — canonical term and node map
- `works-index.json` — machine-readable public works index
- `library-index.json` — machine-readable primary source index
- `downloads-index.json` — machine-readable release and download index
- `services.json` — machine-readable practical review directions
- `use-cases.json` — machine-readable practical situations map
- `contact.json` — machine-readable public contact anchors
- `about.json` — machine-readable author identity and work entry points
- `start-here.json` — machine-readable first-pass entry sequence
- `questions.json` — machine-readable basic question layer
- `topics-index.json` — machine-readable topic and query-intent layer
- `distinctions.json` — machine-readable distinction list
- `misreadings.json` — machine-readable misreading corrections
- `humans.txt` — human-oriented author/site summary

## Updating content

1. Edit the static files in the repository root or canonical subdirectories.
2. For diary content changes, update `content/diary/` and `assets/diary/`, then run `python tools/build_diary.py` before committing.
3. Keep dates, versions, links, and role labels aligned with the public mirrors and the already published site layer; do not invent biographical, semantic, or release metadata.
4. Keep the site dry: glossary, reading path, identity, corpus map, distinctions, entry, works, releases, and evidence only where they add a real navigation or verification function.
5. Commit changes on `main`.
6. Push to `origin`.

## Secondary domain

`advancedglobalintelligence.eu` is not connected as a second GitHub Pages custom domain.

Use the redirect plan in `REDIRECT_PLAN_ADVANCEDGLOBALINTELLIGENCE_EU.md` and configure a manual `301` redirect in OVH to:

`https://ivankotov.eu/advanced-global-intelligence/`
