# Diary Import Protocol

## Purpose

This protocol defines how future diary batches must be imported into the static site without inventing posts, dates, tags, images, or meaning.

## Required batch input from the user

For each diary entry, provide:

- `date`
- `title`
- `text`
- `primary image path`
- `tags`

Optional per entry:

- `extra image paths`
- `linkedin_url`
- explicit `summary` if the user wants to override a shorter summary line
- explicit `image_alt` if the user provides a preferred image description

If any of these are missing, Codex must ask only for the missing factual fields or leave the optional fields empty. Codex must not invent them.

## Import steps for Codex

1. Verify the target batch materials exist locally and are readable.
2. Create or update one Markdown source file per entry in `content/diary/`.
3. Copy or place the related images under `assets/diary/<slug>/`.
4. Keep the source meaning intact while adapting only the formatting needed for the site.
5. Run `python tools/build_diary.py`.
6. Verify that:
   - `diary/index.html` updates correctly
   - `diary-index.json` updates correctly
   - `diary-latest.json` updates correctly
   - the latest-post slot on `index.html` changes correctly
   - a generated page exists at `diary/<slug>/index.html`
7. Review the rendered result and report any omissions, truncations, or image issues explicitly.

## Source file format

Use one file per entry with front matter and a Markdown body:

```md
---
title: Real Title
date: 2026-04-18
slug: real-title
summary: Short factual summary
tags: diary, protocol
primary_image: assets/diary/real-title/cover.jpg
image_alt: Plain description of the image
linkedin_url:
extra_images: assets/diary/real-title/image-02.jpg
---

Real entry body here.
```

Required front matter:

- `title`
- `date`
- `slug`
- `summary`

Optional front matter:

- `tags`
- `primary_image`
- `image_alt`
- `linkedin_url`
- `extra_images`

## Naming convention

- One Markdown source file per entry.
- Filename should follow the slug, for example: `content/diary/real-title.md`.
- Use lowercase ASCII slugs only.
- Use hyphens between words.

## Slug convention

- Lowercase only.
- `a-z`, `0-9`, and hyphens only.
- No spaces.
- No underscores.
- No transliteration guesswork unless the user already gave or approved the slug basis.

## Image placement convention

- Place diary images under `assets/diary/<slug>/`.
- Keep one folder per entry slug.
- Prefer:
  - `cover.ext`
  - `image-02.ext`
  - `image-03.ext`
- Use the original image if possible.
- If a source image needs omission or compression, state that explicitly in the import report.

## What Codex must not do

- Do not invent titles.
- Do not rewrite the meaning into slogans.
- Do not fabricate dates.
- Do not invent tags.
- Do not silently crop or remove images.
- Do not silently merge two posts into one.
- Do not silently split one post into several entries.
- Do not publish placeholder text as if it were a real diary entry.

## Latest post slot on home

- The home page contains a generated diary slot between `<!-- diary-slot:start -->` and `<!-- diary-slot:end -->`.
- `tools/build_diary.py` is responsible for updating that block.
- If at least one real diary entry exists:
  - show the latest entry card
  - include the primary image only if confirmed
  - link both to the latest entry and to `/diary/`
- If no real diary entry exists:
  - show the empty-state placeholder
  - do not show a fake title or fake image

## Archive ordering

- Sort entries in reverse chronological order.
- Newest date first.
- If dates match, keep a stable deterministic order by slug.

## Preserving original meaning

- Keep the original argument, chronology, and emphasis.
- Only normalize formatting where needed for readability and safe HTML rendering.
- Preserve links when they exist in the source material.
- If the user’s text contains ambiguity, ask for clarification instead of normalizing it silently.

## Output surfaces affected by an import

- `content/diary/*.md`
- `assets/diary/<slug>/...`
- `diary/index.html`
- `diary/<slug>/index.html`
- `diary-index.json`
- `diary-latest.json`
- home diary slot inside `index.html`

## Build command

```powershell
python tools/build_diary.py
```
