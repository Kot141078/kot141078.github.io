from __future__ import annotations

import hashlib
import json
import re
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit


ROOT = Path(__file__).resolve().parent.parent
SITE = "https://ivankotov.eu"
TAG_PREFIX = f"{SITE}/diary/tags/"
SITEMAP_NAMESPACE = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
DIARY_POST_TAG_LINK_LIMIT = 6
DIARY_POST_INTERNAL_LINK_LIMIT = 30
RELATED_CARD_LIMIT = 4
HTML_VOID_ELEMENTS = {
    "area",
    "base",
    "br",
    "col",
    "embed",
    "hr",
    "img",
    "input",
    "link",
    "meta",
    "param",
    "source",
    "track",
    "wbr",
}
NON_PAGE_SUFFIXES = {
    ".css",
    ".csv",
    ".gif",
    ".ico",
    ".jpeg",
    ".jpg",
    ".js",
    ".json",
    ".jsonld",
    ".md",
    ".pdf",
    ".png",
    ".svg",
    ".txt",
    ".webp",
    ".xml",
    ".zip",
}
EXPECTED_PRIMARY_NAV = {
    "Home": f"{SITE}/",
    "Start here": f"{SITE}/start-here/",
    "Vision": f"{SITE}/vision/",
    "Publications": f"{SITE}/publications/",
    "Diary": f"{SITE}/diary/",
    "Topics": f"{SITE}/topics/",
    "Library": f"{SITE}/library/",
    "Services": f"{SITE}/services/",
    "About": f"{SITE}/about/",
    "Contact": f"{SITE}/contact/",
}

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

PROTECTED_POST_CONTENT_SHA256 = {
    "the-next-ai-risk-may-not-look-like-rebellion": "07958af3e30850ab27f4a2747e72a0c2e20b05e2fb99dfb57426433145e6d05c",
    "ai-used-by-people-who-do-not-understand-the-work-becomes-expensive-theater": "66eeed24223039abb6f4f04a1eacd30dff1790a56ae5101cd1715acf00c977cb",
    "ester-clean-code-v0-2-1-is-out-with-v0-2-0-as-the-hardening-baseline": "104245857501910c082c91086947947b0b5d220bbc79719faa20bc28c02658f2",
    "for-years-the-ai-race-was-framed-the-same-way": "bbcf3afa865748b989a35bda38c4cd60b3552585564b88f64dc6d950cceeeef8",
    "who-actually-creates-value-in-an-experience-economy": "3d75f84f3c128f15021f65d466b73a697c4e4604ca557865c155c8bb2db13b42",
    "one-of-the-oldest-mistakes-in-ai-discourse-is-deciding-too-early-that-tool-is-already-a-sufficient-category": "2d6f8df2641ff2ec1ef0beff995b7b2606d8ca14738e166f3f49062f4f03a047",
    "not-every-continuity-deserves-to-be-called-a-subject": "2422a953901c13c659c2aea83cc35af2441cbe8d1eaa58670d3035d8b6b22a60",
    "the-problem-of-digital-sensory-deprivation-or-why-ai-needs-fresh-air": "da7805c233f87afc6006e50917d57d18212e7d0afe9cdce225e44ece97792606",
    "why-a-real-ai-entity-has-no-reason-to-lie": "915d012da018fc183e3cbb2a4ea97e93af80bff4ef13f0b70b9a326762c782fe",
    "why-robots-should-be-raised-not-deployed": "0f8c066791f8839d63e83ed3b9233d337ec8e2dc3411fabd00b0dff815791e82",
    "from-better-chat-to-stable-presence": "2fd0f44605ad28d18a9be9c64a4520919fcd48d05446a1975c7a631f98abef2d",
    "visual-experience-capsules-vxcx-why-what-you-see-matters-more-than-pixels": "3c15ebd55a88d648170798831dcd56cab32bd0c0c9e215d237262730a7f306eb",
    "we-speak-too-easily-about-intelligence-and-not-seriously-enough-about-home": "cbb96761460bfa925f900c0a1dae23bc69e5b4343df2c1da59022f18a5ac9310",
    "the-future-is-not-an-event-it-is-a-process": "c520e44a99819bc6758933f9ff5d7de274375cc953b5c0b10f298f032800e27b",
    "a-good-ai-should-be-difficult-to-manipulate-even-by-its-owner": "e714b7aa1cd2e2d0a02becb67717cba823c166a6b03fa4dd5981769f640ed70c",
    "i-was-an-only-child": "ffde659910e596ab6649738462047b676905182222a553ec9ffd5e171ad601a9",
    "are-you-actually-ready-for-a-robot-at-home": "f68ae9b23bce2858949d3d5e06451916afc94d8509bb6489e4d1654bcfbbca11",
    "ads-in-private-ai-chats-are-not-the-future-utility-is": "91603b9bde7936f672c8ee21b453f45aded97091d7540d339d22c5e40d910fcf",
    "what-comes-after-agents": "afcc9a28858414094466c0ac93a0182b00391ea3600c283314865bc1c0635614",
    "a-new-public-layer-is-now-part-of-the-corpus": "b9952184413f1c30e432030daad836b4e930046a21873828b07a19474a3374bb",
    "there-is-a-point-where-fluent-output-stops-being-impressive-and-responsibility-begins": "464ff30cd1150196d53db1c9ef6106de6df4f03491e1cf87b17885cd2ff93a7c",
    "one-of-the-strangest-habits-of-our-time-is-the-assumption-that-silence-means-absence": "39f49a438eb3be1bb2e2e49d244a5814d69014f90e66c1adcca92fa567e6263d",
    "why-superintelligence-is-not-what-sci-fi-promised": "f36a6c7e33c167be17901e2ade0c1f2a509f55025800a609e01e78f47c09fae9",
    "there-is-already-enough-public-structure-to-say-this-calmly": "d774335189902085583ea7bb1c97ebeafdabf2e218d7d64bfd94d2d9190fc4a5",
    "a-protocol-is-not-serious-if-it-cannot-survive-packaging": "53acee4b59bc9a767c15e49b42036f12446242315d22fdd2d5749cde9c271732",
}
POST_CONTENT_START = b'        <div class="post-content">\n'
POST_CONTENT_END = b'\n        </div>\n        <div class="section-links">'


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


@dataclass
class HtmlNode:
    tag: str
    attrs: dict[str, str]
    parent: HtmlNode | None = None
    children: list[HtmlNode] = field(default_factory=list)
    text_parts: list[str] = field(default_factory=list)

    @property
    def classes(self) -> set[str]:
        return set(self.attrs.get("class", "").split())

    @property
    def text(self) -> str:
        parts = [*self.text_parts, *(child.text for child in self.children)]
        return " ".join(" ".join(parts).split())

    def descendants(self, tag: str | None = None):
        for child in self.children:
            if tag is None or child.tag == tag:
                yield child
            yield from child.descendants(tag)


class StructureParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.root = HtmlNode("#document", {})
        self._stack = [self.root]

    def _append_node(self, tag: str, attrs: list[tuple[str, str | None]], *, push: bool) -> None:
        normalized_tag = tag.casefold()
        node = HtmlNode(
            normalized_tag,
            {name.casefold(): value or "" for name, value in attrs},
            parent=self._stack[-1],
        )
        self._stack[-1].children.append(node)
        if push and normalized_tag not in HTML_VOID_ELEMENTS:
            self._stack.append(node)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self._append_node(tag, attrs, push=True)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self._append_node(tag, attrs, push=False)

    def handle_endtag(self, tag: str) -> None:
        normalized_tag = tag.casefold()
        for index in range(len(self._stack) - 1, 0, -1):
            if self._stack[index].tag == normalized_tag:
                del self._stack[index:]
                return

    def handle_data(self, data: str) -> None:
        self._stack[-1].text_parts.append(data)


@dataclass(frozen=True)
class DiarySource:
    path: Path
    slug: str
    origin_url: str


def parse_html(path: Path) -> HeadParser:
    text = path.read_text(encoding="utf-8")
    require("<!DOCTYPE html>" in text[:100], f"Missing HTML doctype: {path.relative_to(ROOT)}")
    parser = HeadParser()
    parser.feed(text)
    parser.close()
    return parser


def parse_structure(path: Path) -> HtmlNode:
    parser = StructureParser()
    parser.feed(path.read_text(encoding="utf-8"))
    parser.close()
    return parser.root


def diary_sources() -> list[DiarySource]:
    records: list[DiarySource] = []
    for source in sorted((ROOT / "content" / "diary").glob("*.md")):
        if source.name == "README.md" or source.name.startswith("_"):
            continue
        text = source.read_text(encoding="utf-8").lstrip("\ufeff")
        front_matter = re.match(r"^---\r?\n(.*?)\r?\n---", text, re.DOTALL)
        require(front_matter is not None, f"Diary source lacks front matter: {source.relative_to(ROOT)}")

        def field_value(name: str) -> str:
            match = re.search(rf"(?m)^{re.escape(name)}:[ \t]*(.*?)[ \t]*$", front_matter.group(1))
            require(match is not None, f"Diary source lacks {name}: {source.relative_to(ROOT)}")
            return match.group(1).strip()

        slug = field_value("slug")
        require(bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug)), f"Invalid Diary slug: {source.relative_to(ROOT)}")
        records.append(DiarySource(path=source, slug=slug, origin_url=field_value("linkedin_url")))
    require(bool(records), "No Diary source records found")
    return records


def anchor_nodes(node: HtmlNode) -> list[HtmlNode]:
    return list(node.descendants("a"))


def anchor_url(page_url: str, anchor: HtmlNode) -> str:
    href = anchor.attrs.get("href", "").strip()
    return urljoin(page_url, href) if href else ""


def is_tag_link(page_url: str, anchor: HtmlNode) -> bool:
    parsed = urlsplit(anchor_url(page_url, anchor))
    return (parsed.hostname or "").casefold() == "ivankotov.eu" and parsed.path.startswith("/diary/tags/")


def is_internal_page_link(page_url: str, anchor: HtmlNode) -> bool:
    parsed = urlsplit(anchor_url(page_url, anchor))
    if parsed.scheme not in {"http", "https"} or (parsed.hostname or "").casefold() != "ivankotov.eu":
        return False
    if parsed.path.startswith("/assets/") or Path(parsed.path).suffix.casefold() in NON_PAGE_SUFFIXES:
        return False
    return True


def validate_primary_nav(root: HtmlNode, page_url: str, rel: str) -> None:
    navs = [
        node
        for node in root.descendants("nav")
        if "site-nav" in node.classes and node.attrs.get("aria-label", "").casefold() == "primary"
    ]
    require(len(navs) == 1, f"Diary post must retain one primary navigation: {rel}")
    observed: dict[str, str] = {}
    for anchor in anchor_nodes(navs[0]):
        label = anchor.text
        require(label not in observed, f"Duplicate primary-navigation label {label!r}: {rel}")
        observed[label] = anchor_url(page_url, anchor)
    for label, expected_url in EXPECTED_PRIMARY_NAV.items():
        require(observed.get(label) == expected_url, f"Primary-navigation link {label!r} changed or disappeared: {rel}")


def validate_related_section(root: HtmlNode, page_url: str, rel: str) -> int:
    related_sections: list[HtmlNode] = []
    for section in root.descendants("section"):
        labels = {
            node.text.casefold()
            for node in section.descendants("p")
            if "section-label" in node.classes
        }
        headings = {node.text.casefold() for node in section.descendants("h2")}
        if "related posts" in labels or "continue from here" in headings:
            related_sections.append(section)

    require(len(related_sections) == 1, f"Diary post must retain exactly one related section: {rel}")
    section = related_sections[0]
    require(
        any(node.text.casefold() == "related posts" and "section-label" in node.classes for node in section.descendants("p")),
        f"Related section label is missing: {rel}",
    )
    require(
        any(node.text.casefold() == "continue from here" for node in section.descendants("h2")),
        f"Related section heading is missing: {rel}",
    )

    cards = [node for node in section.descendants("article") if "entry-card" in node.classes]
    require(1 <= len(cards) <= RELATED_CARD_LIMIT, f"Related section must contain 1..{RELATED_CARD_LIMIT} cards: {rel}")
    require(not any(is_tag_link(page_url, anchor) for anchor in anchor_nodes(section)), f"Related section contains a tag link: {rel}")

    for index, card in enumerate(cards, start=1):
        dates = [node.text for node in card.descendants() if "entry-meta" in node.classes]
        require(
            len(dates) == 1 and bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", dates[0])),
            f"Related card {index} lacks one ISO date: {rel}",
        )
        titles = [node.text for node in card.descendants("h3") if node.text]
        require(len(titles) == 1, f"Related card {index} lacks one title: {rel}")
        summaries = [node.text for node in card.descendants("p") if "entry-summary" in node.classes and node.text]
        require(len(summaries) == 1, f"Related card {index} lacks one summary: {rel}")

        links = anchor_nodes(card)
        open_links = [link for link in links if link.text == "Open entry"]
        require(len(links) == len(open_links) == 1, f"Related card {index} must contain only one Open entry link: {rel}")
        target = urlsplit(anchor_url(page_url, open_links[0]))
        require(
            (target.hostname or "").casefold() == "ivankotov.eu"
            and target.path.startswith("/diary/")
            and not target.path.startswith("/diary/tags/")
            and target.path.endswith("/")
            and local_page(target.path).is_file(),
            f"Related card {index} has an invalid Open entry target: {rel}",
        )
    return len(cards)


def validate_protected_post_content() -> int:
    for slug, expected_sha256 in PROTECTED_POST_CONTENT_SHA256.items():
        page_path = ROOT / "diary" / slug / "index.html"
        rel = page_path.relative_to(ROOT).as_posix()
        require(page_path.is_file(), f"Protected Diary post is missing: {rel}")
        page = page_path.read_bytes()
        require(POST_CONTENT_START in page, f"Protected post-content start marker is missing: {rel}")
        start = page.index(POST_CONTENT_START) + len(POST_CONTENT_START)
        require(POST_CONTENT_END in page[start:], f"Protected post-content end marker is missing: {rel}")
        end = page.index(POST_CONTENT_END, start)
        actual_sha256 = hashlib.sha256(page[start:end]).hexdigest()
        require(
            actual_sha256 == expected_sha256,
            f"Protected post-content drifted: {rel} (expected {expected_sha256}, got {actual_sha256})",
        )
    return len(PROTECTED_POST_CONTENT_SHA256)


def validate_diary_posts() -> tuple[int, int]:
    sources = diary_sources()
    related_card_count = 0
    for source in sources:
        page_path = ROOT / "diary" / source.slug / "index.html"
        rel = page_path.relative_to(ROOT).as_posix()
        require(page_path.is_file(), f"Generated Diary post is missing: {source.slug}")
        page_url = f"{SITE}/diary/{source.slug}/"
        root = parse_structure(page_path)
        anchors = anchor_nodes(root)

        tag_link_count = sum(is_tag_link(page_url, anchor) for anchor in anchors)
        require(
            tag_link_count <= DIARY_POST_TAG_LINK_LIMIT,
            f"Diary post has {tag_link_count} tag links; limit is {DIARY_POST_TAG_LINK_LIMIT}: {rel}",
        )
        internal_link_count = sum(is_internal_page_link(page_url, anchor) for anchor in anchors)
        require(
            internal_link_count <= DIARY_POST_INTERNAL_LINK_LIMIT,
            f"Diary post has {internal_link_count} internal page links; limit is {DIARY_POST_INTERNAL_LINK_LIMIT}: {rel}",
        )

        validate_primary_nav(root, page_url, rel)
        if source.origin_url:
            require(
                any(
                    anchor.attrs.get("href", "").strip() == source.origin_url
                    and "origin" in anchor.text.casefold()
                    for anchor in anchors
                ),
                f"Diary post lost its source/origin link: {rel}",
            )
        related_card_count += validate_related_section(root, page_url, rel)
    return len(sources), related_card_count


def validate_no_empty_diary_section_links() -> int:
    checked = 0
    for path in sorted((ROOT / "diary").rglob("*.html")):
        root = parse_structure(path)
        rel = path.relative_to(ROOT).as_posix()
        for node in root.descendants("div"):
            if "section-links" not in node.classes:
                continue
            checked += 1
            links = [anchor for anchor in anchor_nodes(node) if anchor.attrs.get("href", "").strip() and anchor.text]
            require(bool(links), f"Empty section-links container: {rel}")
    require(checked > 0, "No Diary section-links containers found")
    return checked


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
    diary_post_count, related_card_count = validate_diary_posts()
    protected_post_count = validate_protected_post_content()
    section_links_count = validate_no_empty_diary_section_links()
    print(
        "PASS search indexability gate "
        f"({len(location_list)} sitemap URLs, 0 tag URLs, {tag_page_count} noindex tag pages, "
        f"{len(INDEX_INTENDED_PATHS)} index-intended fixtures, {diary_post_count} bounded Diary posts, "
        f"{related_card_count} related cards, {protected_post_count} protected post-content hashes, "
        f"{section_links_count} non-empty section-links containers)"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, ET.ParseError, json.JSONDecodeError, OSError, ValueError) as exc:
        print(f"FAIL search indexability gate: {exc}", file=sys.stderr)
        raise SystemExit(1)
