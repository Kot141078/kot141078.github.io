"""Update the sitemap dates for the three pages maintained directly as HTML."""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path
from xml.etree import ElementTree


PAGE_SOURCES = {
    "https://ivankotov.eu/": "index.html",
    "https://ivankotov.eu/world-intelligence/": "world-intelligence/index.html",
    "https://ivankotov.eu/publications/": "publications/index.html",
}
SITEMAP_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"


def git(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=root, capture_output=True, text=True, encoding="utf-8"
    )
    if result.returncode:
        raise RuntimeError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout.strip()


def page_dates(root: Path) -> dict[str, str]:
    if git(root, "rev-parse", "--is-shallow-repository") != "false":
        raise RuntimeError("Full Git history is required; fetch with --unshallow first.")

    commit = git(root, "rev-parse", "--verify", "HEAD^{commit}")
    dirty = git(root, "status", "--porcelain=v1", "--untracked-files=all", "--", *PAGE_SOURCES.values())
    if dirty:
        raise RuntimeError(f"Page sources must be committed before computing lastmod:\n{dirty}")

    dates = {}
    for url, source in PAGE_SOURCES.items():
        if git(root, "cat-file", "-t", f"{commit}:{source}") != "blob":
            raise RuntimeError(f"Expected a committed page source at {commit}:{source}")
        date = git(root, "log", "-1", "--format=%cI", commit, "--", source)
        if not date or datetime.fromisoformat(date).utcoffset() is None:
            raise RuntimeError(f"No timezone-aware Git committer timestamp for {source} at {commit}")
        dates[url] = date

    if git(root, "rev-parse", "--verify", "HEAD^{commit}") != commit:
        raise RuntimeError("HEAD changed while reading page history; run again on a fixed commit.")
    return dates


def sitemap_dates(data: bytes) -> dict[str, str | None]:
    root = ElementTree.fromstring(data)
    if root.tag != f"{SITEMAP_NS}urlset":
        raise RuntimeError("Expected a sitemap urlset in the sitemap namespace.")

    dates = {}
    for entry in root.findall(f"{SITEMAP_NS}url"):
        url = entry.findtext(f"{SITEMAP_NS}loc")
        if url not in PAGE_SOURCES:
            continue
        lastmods = entry.findall(f"{SITEMAP_NS}lastmod")
        if url in dates or len(lastmods) != 1:
            raise RuntimeError(f"Expected one sitemap entry with one lastmod for {url}")
        dates[url] = lastmods[0].text
    return dates


def update_page_lastmod(root: Path) -> None:
    dates = page_dates(root)
    sitemap = root / "sitemap.xml"
    original = sitemap.read_bytes()
    missing = dates.keys() - sitemap_dates(original).keys()
    if missing:
        raise RuntimeError(f"Missing sitemap entries: {', '.join(sorted(missing))}")

    updated = original
    for url, date in dates.items():
        # The repository uses adjacent, unprefixed loc and lastmod elements.
        # Replace only the value so the rest of the XML stays byte-for-byte intact.
        pattern = (
            rb"(<loc>" + re.escape(url.encode("ascii")) + rb"</loc>\s*<lastmod>)[^<]*(</lastmod>)"
        )
        updated, count = re.subn(
            pattern, lambda match: match[1] + date.encode("ascii") + match[2], updated
        )
        if count != 1:
            raise RuntimeError(f"Expected one editable sitemap lastmod for {url}, found {count}")

    if sitemap_dates(updated) != dates:
        raise RuntimeError("Updated sitemap dates do not match the page source history.")
    if updated == original:
        return

    with tempfile.NamedTemporaryFile(dir=root, delete=False) as temporary:
        target = Path(temporary.name)
    try:
        target.write_bytes(updated)
        shutil.copymode(sitemap, target)
        os.replace(target, sitemap)
    finally:
        target.unlink(missing_ok=True)


if __name__ == "__main__":
    try:
        update_page_lastmod(Path.cwd())
    except (OSError, RuntimeError, ValueError, ElementTree.ParseError) as exc:
        print(f"FAIL sitemap page lastmod: {exc}", file=sys.stderr)
        raise SystemExit(1)
