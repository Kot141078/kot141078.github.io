# POST_DEPLOY_CHECK

## Poll

- Ready attempt: `1`
- Expected live latest slug: `a-lot-of-ai-discussion-still-assumes-the-main-demand-will-come-from-offices`

## URL Status

- URL checks performed: `41`
- URL checks returning `200`: `41`
- Entry pages returning `200`:
  - `/diary/agents-are-not-the-subject/`
  - `/diary/a-good-ai-should-be-difficult-to-manipulate-even-by-its-owner/`
  - `/diary/arq-is-now-published-on-zenodo/`
  - `/diary/most-people-look-at-ai-systems-from-the-outside/`
  - `/diary/a-lot-of-ai-discussion-still-assumes-the-main-demand-will-come-from-offices/`
- New tag pages returning `200`:
  - `/diary/tags/ai-ethics/`
  - `/diary/tags/trusts/`
  - `/diary/tags/home-ai/`
  - `/diary/tags/digital-continuity/`
- Assets returning `200`:
  - `/assets/diary/agents-are-not-the-subject/cover.jpg`
  - `/assets/diary/a-good-ai-should-be-difficult-to-manipulate-even-by-its-owner/cover.jpg`
  - `/assets/diary/most-people-look-at-ai-systems-from-the-outside/cover.jpg`
  - `/assets/diary/a-lot-of-ai-discussion-still-assumes-the-main-demand-will-come-from-offices/cover.jpg`

## Live State

- `diary-index.json` count: `78`
- `diary-latest.json` slug: `a-lot-of-ai-discussion-still-assumes-the-main-demand-will-come-from-offices`
- Live top 7:
  - `2026-03-27 a-lot-of-ai-discussion-still-assumes-the-main-demand-will-come-from-offices`
  - `2026-03-26 most-people-look-at-ai-systems-from-the-outside`
  - `2026-03-25 arq-is-now-published-on-zenodo`
  - `2026-03-25 a-good-ai-should-be-difficult-to-manipulate-even-by-its-owner`
  - `2026-03-24 agents-are-not-the-subject`
  - `2026-03-23 this-is-not-a-studio-render`
  - `2026-03-23 sometimes-i-think-the-current-agi-race-looks-less-like-science-and-more-like-cervantes`
- Live same-date `2026-03-25` order:
  - `arq-is-now-published-on-zenodo`
  - `a-good-ai-should-be-difficult-to-manipulate-even-by-its-owner`
- Live latest preview count on `/diary/`: `5`
- Live latest preview slugs:
  - `a-lot-of-ai-discussion-still-assumes-the-main-demand-will-come-from-offices`
  - `most-people-look-at-ai-systems-from-the-outside`
  - `arq-is-now-published-on-zenodo`
  - `a-good-ai-should-be-difficult-to-manipulate-even-by-its-owner`
  - `agents-are-not-the-subject`

## Live Validation

- Home latest-post meta line is date-only: `PASS`
- Diary card meta lines are date-only: `PASS`
- Repaired V28 latest preview count is live at `5`: `PASS`
- `/diary/` includes all five imported posts: `PASS`
- `/diary/archive/` includes all five imported posts: `PASS`
- `/diary/tags/` lists `ai-ethics`, `trusts`, `home-ai`, `digital-continuity`: `PASS`
- `POST 0076` remained image-less on live page: `PASS`
- `POST 0076` remained tag-less on live page: `PASS`
- `POST 0076` DOI and GitHub reading-context link survived: `PASS`
- `POST 0075` literal `Trusts` tag survived: `PASS`
- `POST 0074` DOI and `c = a + b` survived: `PASS`
- `POST 0077` `Presence.` and `c = a + b` survived: `PASS`
- `POST 0078` household question block survived: `PASS`
- New live tag counts:
  - `AI Ethics = 1`
  - `Trusts = 1`
  - `Home AI = 1`
  - `Digital Continuity = 1`
- Previously imported entry `this-is-not-a-studio-render` still exists: `PASS`
- No fake placeholder image introduced anywhere checked: `PASS`
