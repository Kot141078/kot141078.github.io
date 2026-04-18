# Diary Content

Use this directory for real diary entries only.

- Keep each published entry in one Markdown file.
- Do not invent or pre-seed public posts.
- Keep `_template.md` as the starting structure for future imports.
- After adding or changing entries, run `python tools/build_diary.py`.
- The builder treats this directory as the single source of truth for diary entries.

The builder skips:

- files starting with `_`
- `README.md`

Chosen source format:

- one Markdown file per entry
- front matter between `---` lines
- Markdown body after the closing `---`

Required front matter keys:

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

Body rules:

- The body is required after the closing front matter delimiter.
- Preserve the original meaning.
- Do not silently compress the argument into slogans.

Validation rules:

- `date` must use ISO format: `YYYY-MM-DD`.
- `slug` must use lowercase ASCII plus hyphens.
- `tags` must stay explicit; keep the field even when empty.
- `primary_image`, `image_alt`, and `linkedin_url` must stay explicit even when empty.

Example filename:

- `content/diary/real-entry-slug.md`
