# Diary Import Protocol

## Purpose

This protocol defines the exact working method for future diary batch imports into the static site. The goal is to transform real source materials into `content/diary/*.md`, `assets/diary/<slug>/...`, and generated public surfaces without inventing posts, dates, tags, images, summaries, or meaning.

## Exact batch package format

Accepted input batch:

```text
batch-root/
  YYYY-MM-DD__slug-basis/
    body.md or body.txt
    images/
      <image files>
  YYYY-MM-DD__slug-basis-2/
    body.md or body.txt
    images/
      <image files>
```

Required per entry folder:

- folder name format: `YYYY-MM-DD__slug-basis`
- one source text file: `body.md` or `body.txt`
- a factual title basis in the body heading, user note, or accompanying message

Optional per entry folder:

- `images/cover.<ext>`
- `images/image-02.<ext>`, `images/image-03.<ext>`, and so on
- explicit user note for tags
- explicit LinkedIn URL
- explicit summary override
- explicit image alt text

If a batch arrives in another shape, Codex must normalize it into this folder structure before import and report that normalization explicitly. The final normalized repo output must still be one Markdown file per entry in `content/diary/`.

## Repo output format

Each imported entry must end as exactly one Markdown file:

```md
---
title: Real Title
date: 2026-04-18
slug: real-title
summary: Short factual summary
tags: architecture, diary
primary_image: assets/diary/real-title/cover.jpg
image_alt: Plain factual image description
linkedin_url: https://www.linkedin.com/...
extra_images: assets/diary/real-title/image-02.jpg, assets/diary/real-title/image-03.jpg
---

Real entry body here.
```

Required explicit front matter keys:

- `title`
- `date`
- `slug`
- `summary`
- `tags`
- `primary_image`
- `image_alt`
- `linkedin_url`

Optional front matter keys:

- `extra_images`

Required content after front matter:

- non-empty body

## File naming rules

- Final source file path must be `content/diary/<slug>.md`.
- The filename must match the final slug exactly.
- One source file equals one public diary post.
- Do not merge multiple source entries into one file.
- Do not split one source entry into several files unless the user explicitly says the source package contains separate posts.

## Image naming rules

- All imported images must live under `assets/diary/<slug>/`.
- Preferred naming:
  - `cover.<ext>`
  - `image-02.<ext>`
  - `image-03.<ext>`
- Keep original extension when possible.
- Do not silently rename images into unrelated names.
- Do not place diary images outside `assets/diary/<slug>/` unless the user explicitly requires an external asset path.

## Slug rules

- Slug must be lowercase ASCII.
- Allowed characters: `a-z`, `0-9`, `-`.
- No spaces, underscores, or trailing hyphens.
- Slug must be stable and deterministic.
- Slug must not be guessed from non-Latin text without an explicit user-approved basis.
- If the title exists and already converts cleanly into an ASCII slug, use that normalized form.
- If the slug basis is ambiguous, stop and ask the user instead of publishing a guessed slug.

## Date normalization rules

- Final date must be ISO format: `YYYY-MM-DD`.
- Preserve the factual date from the source batch when present.
- If the source uses another exact format, normalize it into ISO only after confirming the day/month meaning is unambiguous.
- If the date is ambiguous, missing, or contradictory across materials, stop and ask the user.
- Never invent a date to make the builder pass.

## Title extraction fallback rules

- Use the explicit user-provided title first.
- If no explicit title was provided, use the strongest factual source in this order:
  1. entry folder name
  2. file name
  3. first clear heading in `body.md`
- If no reliable title can be extracted, stop and ask the user.
- Do not write marketing copy or paraphrased slogans as a substitute title.

## Summary extraction rules

- Use explicit user-provided summary if supplied.
- Otherwise derive a short factual summary from the opening lines of the real body text.
- Keep the summary compact, neutral, and literal.
- Do not invent claims not present in the source material.
- Do not use placeholder text such as `Summary pending`.

## Tag normalization rules

- Tags must come from the user or from explicit source labels already present in the batch.
- Store tag labels in front matter as a comma-separated list.
- Builder normalization converts each tag label into a lowercase ASCII tag slug for URL generation.
- If a tag label cannot be normalized into a usable ASCII slug, stop and ask for a corrected factual tag.
- Do not invent tags for SEO or navigation cosmetics.

## LinkedIn trace handling

- `linkedin_url` is optional.
- If the source post was published on LinkedIn and the URL is known, preserve it exactly.
- If the URL is unknown, keep `linkedin_url:` present but empty.
- Do not fabricate or search for a likely LinkedIn URL unless the user explicitly asks for that research.

## One image vs gallery

- Use one image only when the entry has a single confirmed public image or one clear hero image.
- Use `primary_image` for the hero image.
- Use `extra_images` only for additional confirmed images that belong to the same entry.
- If there are no confirmed images, leave `primary_image` and `image_alt` empty and do not invent placeholders.
- If `primary_image` is set, `image_alt` must also be set.

## Missing images, broken paths, ambiguous dates

- If a referenced image is missing, stop before build and report the missing path.
- If image order is unclear, keep only the confirmed hero image until the user clarifies the gallery order.
- If the body exists but the date is ambiguous, do not import the entry yet.
- If the body exists but the slug/title basis is ambiguous, do not import the entry yet.
- If a path is broken after copying, fix the factual path or stop; do not silently drop the image from a real post.

## What Codex must never do

- Never invent a diary entry.
- Never invent a date.
- Never invent a title.
- Never invent a slug.
- Never invent tags.
- Never invent a summary that changes the meaning.
- Never invent or fabricate image files.
- Never publish placeholder body text as if it were a real entry.
- Never rewrite the argument into a different voice or narrative.
- Never silently discard source links.

## Latest-post slot selection

- The home diary slot is derived from generated state, not handwritten HTML.
- The selected latest post is the newest valid entry after date sort.
- Sort order is newest date first.
- If dates are equal, use slug as the deterministic tie-breaker.
- If there are no valid entries, home must show the empty placeholder only.

## Archive ordering

- Archive ordering is reverse chronological.
- Group entries by year on `/diary/archive/`.
- Inside each year, entries remain sorted by newest date first.
- If two entries share the same date, order by slug.

## Tag pages generation

- `/diary/tags/` lists only tags that actually exist on imported entries.
- Per-tag pages are generated from normalized tag slugs.
- A tag page contains only entries explicitly carrying that tag.
- No empty per-tag page should be generated unless at least one real entry uses that tag.

## Import execution steps

1. Verify the repo working tree is clean before starting a new import pass.
2. Verify the batch source materials exist and are readable.
3. Normalize title, date, slug, summary, tags, image paths, and LinkedIn trace according to this protocol.
4. Create or update `content/diary/<slug>.md`.
5. Copy images into `assets/diary/<slug>/`.
6. Run `python tools/build_diary.py`.
7. Verify generated outputs:
   - `diary/index.html`
   - `diary/archive/index.html`
   - `diary/tags/index.html`
   - `diary/<slug>/index.html`
   - `diary-index.json`
   - `diary-tags.json`
   - `diary-feed.xml`
   - home latest-post slot in `index.html`
8. Review rendered output and report any unresolved omissions or blocked entries explicitly.

## Build command

```powershell
python tools/build_diary.py
```
