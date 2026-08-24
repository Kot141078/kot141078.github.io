from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parent.parent
SITE = "https://ivankotov.eu"
TAG_PREFIX = f"{SITE}/diary/tags/"
SITEMAP_NAMESPACE = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

# These six legacy Qubit of Hope release/corpus resources were already present
# in the frozen origin/main sitemap. This iteration neither adds raw assets nor
# widens its 799 - 502 = 297 URL contract; it prevents any new raw URL and
# explicitly keeps the seven Search Console resources below out.
LEGACY_RAW_SITEMAP_URLS = {
    f"{SITE}/qubit-of-hope.json",
    f"{SITE}/qubit-of-hope-volume-ii.json",
    f"{SITE}/qubit-of-hope-volume-iii.json",
    f"{SITE}/QUBIT_OF_HOPE_TRILOGY_DOI_LEDGER_v1_0_2.json",
    f"{SITE}/QUBIT_OF_HOPE_TRILOGY_PUBLICATION_CLOSURE_v1_0_2.md",
    f"{SITE}/QUBIT_OF_HOPE_TRILOGY_PUBLICATION_CLOSURE_v1_0_2_SHA256SUMS.txt",
}
SEARCH_CONSOLE_RAW_URLS = {
    f"{SITE}/downloads/article50-transparency-implementation-briefs-v0-1/PACKAGE_MANIFEST.json",
    f"{SITE}/publications/a6-ctp-v0-1-4/files/SHA256SUMS_A6_CTP_v0_1_4.txt",
    f"{SITE}/publications/a6-ctp-v0-1-4/files/SHA256SUMS_A6_CTP_v0_1_4_GITHUB_PLACEMENT.txt",
    f"{SITE}/downloads/article50-transparency-implementation-briefs-v0-1/02_For_Engineers_CGAM_Witness_Oracle_Degradation.md",
    f"{SITE}/qubit-state-c.json",
    f"{SITE}/arq-cq-integration-addendum.json",
    f"{SITE}/sitemap.xml",
}

INDEX_INTENDED_PATHS = (
    "/diary/the-next-ai-risk-may-not-look-like-rebellion/",
    "/ai-governance/",
    "/publications/ester-theoretical-core-v0-1/",
    "/diary/ai-used-by-people-who-do-not-understand-the-work-becomes-expensive-theater/",
    "/diary/ester-clean-code-v0-2-1-is-out-with-v0-2-0-as-the-hardening-baseline/",
    "/diary/for-years-the-ai-race-was-framed-the-same-way/",
    "/diary/who-actually-creates-value-in-an-experience-economy/",
    "/diary/one-of-the-oldest-mistakes-in-ai-discourse-is-deciding-too-early-that-tool-is-already-a-sufficient-category/",
    "/long-lived-ai-entities/",
    "/diary/not-every-continuity-deserves-to-be-called-a-subject/",
    "/diary/the-problem-of-digital-sensory-deprivation-or-why-ai-needs-fresh-air/",
    "/diary/why-a-real-ai-entity-has-no-reason-to-lie/",
    "/diary/why-robots-should-be-raised-not-deployed/",
    "/diary/from-better-chat-to-stable-presence/",
    "/diary/visual-experience-capsules-vxcx-why-what-you-see-matters-more-than-pixels/",
    "/diary/we-speak-too-easily-about-intelligence-and-not-seriously-enough-about-home/",
    "/diary/the-future-is-not-an-event-it-is-a-process/",
    "/diary/a-good-ai-should-be-difficult-to-manipulate-even-by-its-owner/",
    "/diary/i-was-an-only-child/",
    "/diary/are-you-actually-ready-for-a-robot-at-home/",
    "/diary/ads-in-private-ai-chats-are-not-the-future-utility-is/",
    "/qubit-state-c/",
    "/diary/themes/local-first-infrastructure/",
    "/diary/what-comes-after-agents/",
    "/diary/a-new-public-layer-is-now-part-of-the-corpus/",
    "/diary/there-is-a-point-where-fluent-output-stops-being-impressive-and-responsibility-begins/",
    "/diary/one-of-the-strangest-habits-of-our-time-is-the-assumption-that-silence-means-absence/",
    "/kotov-principle-l4-bound-experience/",
    "/diary/why-superintelligence-is-not-what-sci-fi-promised/",
    "/diary/there-is-already-enough-public-structure-to-say-this-calmly/",
    "/diary/a-protocol-is-not-serious-if-it-cannot-survive-packaging/",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


class HeadParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.canonicals: list[str] = []
        self.robots: list[str] = []
        self.json_ld_blocks: list[str] = []
        self._in_json_ld = False
        self._json_ld_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {name.lower(): value or "" for name, value in attrs}
        if tag.lower() == "link" and "canonical" in values.get("rel", "").lower().split():
            self.canonicals.append(values.get("href", ""))
        elif tag.lower() == "meta" and values.get("name", "").lower() == "robots":
            self.robots.append(values.get("content", ""))
        elif tag.lower() == "script" and values.get("type", "").lower() == "application/ld+json":
            self._in_json_ld = True
            self._json_ld_parts = []

    def handle_data(self, data: str) -> None:
        if self._in_json_ld:
            self._json_ld_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "script" and self._in_json_ld:
            self.json_ld_blocks.append("".join(self._json_ld_parts))
            self._in_json_ld = False
            self._json_ld_parts = []


def parse_html(path: Path) -> HeadParser:
    text = path.read_text(encoding="utf-8")
    require("<!DOCTYPE html>" in text[:100], f"Missing HTML doctype: {path.relative_to(ROOT)}")
    parser = HeadParser()
    parser.feed(text)
    parser.close()
    return parser


def local_page(path: str) -> Path:
    require(path.startswith("/") and path.endswith("/"), f"Fixture path is not a clean page path: {path}")
    if path == "/":
        return ROOT / "index.html"
    return ROOT.joinpath(*path.strip("/").split("/"), "index.html")


def valid_site_url(value: str) -> bool:
    parsed = urlsplit(value)
    return parsed.scheme == "https" and parsed.netloc == "ivankotov.eu" and parsed.path.startswith("/")


def robots_tokens(values: list[str]) -> set[str]:
    tokens: set[str] = set()
    for value in values:
        tokens.update(token for token in re.split(r"[\s,]+", value.casefold()) if token)
    return tokens


def sitemap_locations() -> list[str]:
    tree = ET.parse(ROOT / "sitemap.xml")
    return [node.text or "" for node in tree.findall(".//sm:loc", SITEMAP_NAMESPACE)]


def expected_tag_pages() -> set[Path]:
    expected = {ROOT / "diary" / "tags" / "index.html"}
    for source in sorted((ROOT / "content" / "diary").glob("*.md")):
        if source.name == "README.md" or source.name.startswith("_"):
            continue
        text = source.read_text(encoding="utf-8").lstrip("\ufeff")
        front_matter = re.match(r"^---\r?\n(.*?)\r?\n---", text, re.DOTALL)
        require(front_matter is not None, f"Diary source lacks front matter: {source.relative_to(ROOT)}")
        tag_line = re.search(r"(?m)^tags:[ \t]*(.*?)[ \t]*$", front_matter.group(1))
        require(tag_line is not None, f"Diary source lacks tags: {source.relative_to(ROOT)}")
        for raw_tag in tag_line.group(1).split(","):
            if not raw_tag.strip():
                continue
            slug = re.sub(r"[^a-z0-9]+", "-", raw_tag.strip().casefold()).strip("-")
            require(bool(slug), f"Diary source has an invalid tag: {source.relative_to(ROOT)}")
            expected.add(ROOT / "diary" / "tags" / slug / "index.html")

    tag_index = json.loads((ROOT / "diary-tags.json").read_text(encoding="utf-8"))
    for item in tag_index.get("tags", []):
        slug = item.get("slug")
        require(isinstance(slug, str) and bool(slug), "diary-tags.json contains an invalid canonical slug")
        expected.add(ROOT / "diary" / "tags" / slug / "index.html")
    return expected


def validate_tag_surfaces(locations: set[str]) -> int:
    tag_pages = set((ROOT / "diary" / "tags").rglob("index.html"))
    expected = expected_tag_pages()
    require(tag_pages == expected, "Diary tag page set does not match source and canonical tag records")
    require(not any(url.startswith(TAG_PREFIX) for url in locations), "Diary tag surface remains in sitemap.xml")

    for path in sorted(tag_pages):
        parser = parse_html(path)
        rel = path.relative_to(ROOT).as_posix()
        require(robots_tokens(parser.robots) == {"noindex", "follow"}, f"Tag page lacks noindex, follow: {rel}")
        require(len(parser.canonicals) == 1, f"Tag page must have exactly one canonical: {rel}")
        canonical = parser.canonicals[0]
        require(valid_site_url(canonical) and canonical.startswith(TAG_PREFIX), f"Invalid tag canonical: {rel}")
        canonical_path = local_page(urlsplit(canonical).path)
        require(canonical_path.is_file(), f"Tag canonical target is missing: {rel} -> {canonical}")
    return len(tag_pages)


def validate_raw_asset_exclusion(locations: set[str]) -> None:
    observed_raw: set[str] = set()
    for url in locations:
        path = urlsplit(url).path.casefold()
        name = Path(path).name
        if path.endswith((".json", ".jsonld", ".txt", ".md")) or "sha256" in name or "manifest" in name:
            observed_raw.add(url)
        if path == "/sitemap.xml":
            observed_raw.add(url)
    require(not (SEARCH_CONSOLE_RAW_URLS & locations), "A Search Console raw resource is present in sitemap.xml")
    require(
        observed_raw <= LEGACY_RAW_SITEMAP_URLS,
        f"New raw/download asset is present in sitemap.xml: {sorted(observed_raw - LEGACY_RAW_SITEMAP_URLS)}",
    )


def validate_index_intended_fixtures(locations: set[str]) -> None:
    for page_path in INDEX_INTENDED_PATHS:
        url = f"{SITE}{page_path}"
        path = local_page(page_path)
        require(path.is_file(), f"Index-intended fixture is missing: {page_path}")
        parser = parse_html(path)
        rel = path.relative_to(ROOT).as_posix()
        require(parser.canonicals == [url], f"Index-intended page is not self-canonical: {rel}")
        require("noindex" not in robots_tokens(parser.robots), f"Index-intended page has noindex: {rel}")
        require(url in locations, f"Index-intended page is missing from sitemap.xml: {url}")
        require(parser.json_ld_blocks, f"Index-intended page lacks JSON-LD: {rel}")
        for block in parser.json_ld_blocks:
            json.loads(block)


def validate_sitemap_pages_are_indexable(locations: set[str]) -> None:
    for url in locations:
        parsed = urlsplit(url)
        if parsed.scheme != "https" or parsed.netloc != "ivankotov.eu" or not parsed.path.endswith("/"):
            continue
        path = local_page(parsed.path)
        require(path.is_file(), f"Sitemap page is missing locally: {url}")
        parser = parse_html(path)
        require("noindex" not in robots_tokens(parser.robots), f"Sitemap page has noindex: {url}")


def main() -> int:
    location_list = sitemap_locations()
    require(len(location_list) == len(set(location_list)), "sitemap.xml contains duplicate locations")
    locations = set(location_list)
    tag_page_count = validate_tag_surfaces(locations)
    validate_raw_asset_exclusion(locations)
    validate_index_intended_fixtures(locations)
    validate_sitemap_pages_are_indexable(locations)
    print(
        "PASS search indexability gate "
        f"({len(location_list)} sitemap URLs, 0 tag URLs, {tag_page_count} noindex tag pages, "
        f"{len(INDEX_INTENDED_PATHS)} index-intended fixtures)"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, ET.ParseError, json.JSONDecodeError, OSError, ValueError) as exc:
        print(f"FAIL search indexability gate: {exc}", file=sys.stderr)
        raise SystemExit(1)
