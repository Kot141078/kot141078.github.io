# Diary Import Checklist

1. Confirm the site repo working tree is clean before starting the import pass.
2. Confirm each entry has a real body source, factual title basis, unambiguous date, and stable slug basis.
3. Normalize every entry into `content/diary/<slug>.md` with explicit front matter keys.
4. Place all confirmed images under `assets/diary/<slug>/` with `cover` plus ordered gallery names when needed.
5. Keep `linkedin_url` exact if known, otherwise keep it explicitly empty.
6. Run `python tools/build_diary.py`.
7. Check `/diary/`, `/diary/archive/`, `/diary/tags/`, per-post pages, `diary-index.json`, `diary-tags.json`, `diary-feed.xml`, and the home latest-post slot.
8. Verify no fake posts, fake dates, fake tags, fake summaries, or broken image paths were published.
9. Commit only after the generated surfaces and machine-readable files match the imported batch.
