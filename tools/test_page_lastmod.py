"""Exercise lastmod against disposable Git histories and an exact XML fixture."""

from __future__ import annotations

import os
import subprocess
import tempfile
import unittest
from pathlib import Path

from update_page_lastmod import PAGE_SOURCES, update_page_lastmod


INITIAL = b"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://ivankotov.eu/</loc><lastmod>2000-01-01</lastmod></url>
  <!-- Leave this entry and the whitespace intact. -->
  <url>
    <loc>https://ivankotov.eu/diary/example/</loc>
    <lastmod>2025-10-03</lastmod><changefreq>monthly</changefreq>
  </url>
  <url><loc>https://ivankotov.eu/world-intelligence/</loc><lastmod>2000-01-02</lastmod></url>
  <url><loc>https://ivankotov.eu/publications/</loc><lastmod>2000-01-03</lastmod></url>
</urlset>
""".replace(b"\n", b"\r\n")

INITIAL_DATE = "2026-11-14T17:55:31+01:00"
WI_DATE = "2026-11-23T00:14:57+01:00"
PUBLICATIONS_DATE = "2026-11-25T09:02:11+01:00"
EXPECTED = (
    INITIAL.replace(b"2000-01-01", INITIAL_DATE.encode("ascii"))
    .replace(b"2000-01-02", WI_DATE.encode("ascii"))
    .replace(b"2000-01-03", PUBLICATIONS_DATE.encode("ascii"))
)


class PageLastmodTest(unittest.TestCase):
    def setUp(self) -> None:
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.root = Path(folder.name) / "repo"
        self.root.mkdir()
        self.git("init", "--quiet")
        self.git("config", "user.name", "Sitemap test")
        self.git("config", "user.email", "test@example.invalid")
        self.git("config", "core.autocrlf", "false")
        self.git("config", "commit.gpgsign", "false")
        for source in PAGE_SOURCES.values():
            path = self.root / source
            path.parent.mkdir(exist_ok=True)
            path.write_bytes(b"initial\n")
        self.sitemap = self.root / "sitemap.xml"
        self.sitemap.write_bytes(INITIAL)
        self.commit(INITIAL_DATE)
        (self.root / "world-intelligence/index.html").write_bytes(b"audio links\n")
        self.commit(WI_DATE)
        self.publications = self.root / "publications/index.html"
        self.publications.write_bytes(b"updated labels\n")
        self.commit(PUBLICATIONS_DATE)

    def git(self, *args: str, date: str | None = None) -> None:
        env = os.environ.copy()
        if date is not None:
            env.update(GIT_AUTHOR_DATE=INITIAL_DATE, GIT_COMMITTER_DATE=date)
        subprocess.run(["git", *args], cwd=self.root, env=env, check=True, capture_output=True)

    def commit(self, date: str) -> None:
        self.git("add", "--all")
        self.git("commit", "--quiet", "-m", "Fixture", date=date)

    def test_committer_dates_and_unrelated_commit_preserve_other_xml(self) -> None:
        update_page_lastmod(self.root)
        self.assertEqual(self.sitemap.read_bytes(), EXPECTED)
        self.git("add", "sitemap.xml")
        self.git("commit", "--quiet", "-m", "Sitemap only", date="2026-11-26T12:00:00+01:00")
        (self.root / "unrelated.txt").write_bytes(b"unrelated\n")
        self.commit("2026-11-27T12:00:00+01:00")
        update_page_lastmod(self.root)
        self.assertEqual(self.sitemap.read_bytes(), EXPECTED)

    def test_ignores_mtime_and_is_idempotent(self) -> None:
        for source in PAGE_SOURCES.values():
            os.utime(self.root / source, (1_600_000_000, 1_600_000_000))
        update_page_lastmod(self.root)
        self.assertEqual(self.sitemap.read_bytes(), EXPECTED)
        sitemap_stat = self.sitemap.stat()
        update_page_lastmod(self.root)
        self.assertEqual(self.sitemap.read_bytes(), EXPECTED)
        self.assertEqual(self.sitemap.stat().st_mtime_ns, sitemap_stat.st_mtime_ns)

    def test_rejects_unstaged_source(self) -> None:
        self.publications.write_bytes(b"uncommitted\n")
        self.assert_rejected("Page sources must be committed")

    def test_rejects_staged_source_even_if_worktree_matches_head(self) -> None:
        self.publications.write_bytes(b"staged\n")
        self.git("add", "publications/index.html")
        self.publications.write_bytes(b"updated labels\n")
        self.assert_rejected("Page sources must be committed")

    def test_rejects_missing_committed_source(self) -> None:
        self.publications.unlink()
        self.commit(PUBLICATIONS_DATE)
        self.assert_rejected(r"cat-file.*publications/index.html.*failed")

    def test_rejects_shallow_history(self) -> None:
        shallow = self.root.parent / "shallow"
        self.git("clone", "--quiet", "--depth=1", self.root.as_uri(), str(shallow))
        with self.assertRaisesRegex(RuntimeError, "Full Git history is required"):
            update_page_lastmod(shallow)
        self.assertEqual((shallow / "sitemap.xml").read_bytes(), INITIAL)

    def test_rejects_missing_history(self) -> None:
        empty = self.root.parent / "empty"
        empty.mkdir()
        self.git("init", "--quiet", str(empty))
        sitemap = empty / "sitemap.xml"
        sitemap.write_bytes(INITIAL)
        with self.assertRaisesRegex(RuntimeError, "rev-parse --verify HEAD"):
            update_page_lastmod(empty)
        self.assertEqual(sitemap.read_bytes(), INITIAL)

    def test_rejects_incomplete_sitemap_without_writing_any_dates(self) -> None:
        data = INITIAL.replace(b"<lastmod>2000-01-03</lastmod>", b"")
        self.sitemap.write_bytes(data)
        with self.assertRaisesRegex(RuntimeError, "one lastmod.*publications"):
            update_page_lastmod(self.root)
        self.assertEqual(self.sitemap.read_bytes(), data)

    def assert_rejected(self, reason: str) -> None:
        with self.assertRaisesRegex(RuntimeError, reason):
            update_page_lastmod(self.root)
        self.assertEqual(self.sitemap.read_bytes(), INITIAL)


if __name__ == "__main__":
    unittest.main(verbosity=2)
