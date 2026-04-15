# kot141078.github.io

Static user-site repository for `ivankotov.eu`.

## What this is

This repository serves a minimal public entry page for:

- `advanced-global-intelligence`
- `sovereign-entity-recursion`
- `ester-reality-bound`
- `ester-clean-code`

It also includes canonical, identity, authority/evidence, and distinctions layers through:

- `about`
- `corpus-map`
- `distinctions`
- `misreadings`
- `c = a + b`
- `L4`
- `SER`
- `Qubit of Hope — Volume I`
- `glossary`
- `reading-path`
- `publications`
- `releases`
- `evidence`
- `llms.txt`
- `canonical-map.json`
- `works-index.json`
- `about.json`
- `distinctions.json`
- `misreadings.json`
- `humans.txt`

Current site layer: `v0.6` distinctions/misreadings layer on top of identity/corpus-map layer `v0.5`, authority/evidence layer `v0.4`, and canonical layer `v0.3`.

It is a plain static site: HTML + CSS + JSON/JSON-LD only, no build step, no package manager, no framework.

## Primary domain

- Primary custom domain: `ivankotov.eu`
- GitHub Pages source: branch `main`, path `/`

## Canonical, identity, evidence, and distinctions pages

- `index.html`
- `about/index.html`
- `corpus-map/index.html`
- `distinctions/index.html`
- `misreadings/index.html`
- `advanced-global-intelligence/index.html`
- `c-a-plus-b/index.html`
- `l4/index.html`
- `ser/index.html`
- `qubit-of-hope/index.html`
- `glossary/index.html`
- `reading-path/index.html`
- `publications/index.html`
- `releases/index.html`
- `evidence/index.html`

## Machine-readable layer

- `llms.txt` — compact machine-facing site guide
- `canonical-map.json` — canonical term and node map
- `works-index.json` — machine-readable public works index
- `about.json` — machine-readable author identity and work entry points
- `distinctions.json` — machine-readable distinction list
- `misreadings.json` — machine-readable misreading corrections
- `humans.txt` — human-oriented author/site summary

## Updating content

1. Edit the static files in the repository root or canonical subdirectories.
2. Keep dates, versions, links, and role labels aligned with the public mirrors and the already published site layer; do not invent biographical, semantic, or release metadata.
3. Keep the site dry: glossary, reading path, identity, corpus map, distinctions, works, releases, and evidence only where they add a real navigation or verification function.
4. Commit changes on `main`.
5. Push to `origin`.

## Secondary domain

`advancedglobalintelligence.eu` is not connected as a second GitHub Pages custom domain.

Use the redirect plan in `REDIRECT_PLAN_ADVANCEDGLOBALINTELLIGENCE_EU.md` and configure a manual `301` redirect in OVH to:

`https://ivankotov.eu/advanced-global-intelligence/`
