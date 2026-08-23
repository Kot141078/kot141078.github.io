from __future__ import annotations

import hashlib
import html.parser
import json
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

from build_machine_layer import OUTPUTS, ROOT, SCHEMAS, SITE, build_outputs


DOI_RE = re.compile(r"^https://doi\.org/10\.\d{4,9}/\S+$", re.IGNORECASE)
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
ARTIFACT_ID_RE = re.compile(r"^A\d{3}$")
COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")
LOCAL_HOST = "ivankotov.eu"
MOT_C_PUBLICATION_ID = "motivational-formation-c-v0-1"
MOT_C_REPOSITORY = "https://github.com/Kot141078/advanced-global-intelligence"
MOT_C_RELEASE_TAG = "mot-c-v0.1"
MOT_C_SOURCE_COMMIT = "35fa9007f61836aed686c0f62404e1ae47301939"
MOT_C_REPOSITORY_PATH = f"publications/{MOT_C_PUBLICATION_ID}"
MOT_C_TAG_SOURCE = f"{MOT_C_REPOSITORY}/tree/{MOT_C_RELEASE_TAG}/{MOT_C_REPOSITORY_PATH}"
MOT_C_LIVING_SOURCE = f"{MOT_C_REPOSITORY}/tree/main/{MOT_C_REPOSITORY_PATH}"
MOT_C_COMMIT_SOURCE = f"{MOT_C_REPOSITORY}/tree/{MOT_C_SOURCE_COMMIT}/{MOT_C_REPOSITORY_PATH}"
MOT_C_RELEASE_URL = f"{MOT_C_REPOSITORY}/releases/tag/{MOT_C_RELEASE_TAG}"
MOT_C_VERSION_DOI = "https://doi.org/10.5281/zenodo.22060517"


class CheckError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CheckError(message)


def read_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        raise CheckError(f"Cannot read JSON {path.relative_to(ROOT)}: {exc}") from exc


def sha256_file(path: Path) -> str:
    # Match build_machine_layer.py: source hashes are normalized-text hashes,
    # not platform checkout newline hashes.
    return hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def local_path_for_url(url: str) -> Path | None:
    parsed = urlsplit(url)
    if parsed.scheme not in {"http", "https"} or parsed.netloc.lower() != LOCAL_HOST:
        return None
    relative = unquote(parsed.path).lstrip("/")
    if not relative:
        return ROOT / "index.html"
    candidate = ROOT / relative
    if parsed.path.endswith("/"):
        return candidate / "index.html"
    return candidate


class PageParser(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.doctype = False
        self.lang: str | None = None
        self.title_parts: list[str] = []
        self.in_title = False
        self.h1_count = 0
        self.canonicals: list[str] = []
        self.robots: list[str] = []
        self.references: list[str] = []
        self.images_without_alt = 0
        self.jsonld: list[str] = []
        self.in_jsonld = False
        self.jsonld_parts: list[str] = []

    def handle_decl(self, decl: str) -> None:
        if decl.lower().startswith("doctype"):
            self.doctype = True

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key.lower(): "" if value is None else value for key, value in attrs}
        tag = tag.lower()
        if tag == "html" and self.lang is None:
            self.lang = values.get("lang")
        elif tag == "title":
            self.in_title = True
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "link":
            rel = values.get("rel", "").lower().split()
            href = values.get("href", "")
            if "canonical" in rel and href:
                self.canonicals.append(href)
            if href:
                self.references.append(href)
        elif tag == "meta" and values.get("name", "").lower() == "robots":
            self.robots.append(values.get("content", "").lower())
        elif tag == "a" and values.get("href"):
            self.references.append(values["href"])
        elif tag in {"img", "script", "source"} and values.get("src"):
            self.references.append(values["src"])
            if tag == "img" and "alt" not in values:
                self.images_without_alt += 1
        elif tag == "img" and "alt" not in values:
            self.images_without_alt += 1
        if tag == "script" and values.get("type", "").lower() == "application/ld+json":
            self.in_jsonld = True
            self.jsonld_parts = []

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "title":
            self.in_title = False
        elif tag == "script" and self.in_jsonld:
            self.in_jsonld = False
            self.jsonld.append("".join(self.jsonld_parts).strip())
            self.jsonld_parts = []

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)
        if self.in_jsonld:
            self.jsonld_parts.append(data)

    @property
    def title(self) -> str:
        return " ".join("".join(self.title_parts).split())


def check_generated_outputs() -> None:
    expected = build_outputs()
    for path, text in expected.items():
        require(path.exists(), f"Missing generated file: {path.relative_to(ROOT)}")
        require(path.read_text(encoding="utf-8") == text, f"Stale generated file: {path.relative_to(ROOT)}")


def check_schema_documents() -> None:
    for route in SCHEMAS.values():
        path = ROOT / route.lstrip("/")
        schema = read_json(path)
        require(schema.get("$schema") == "https://json-schema.org/draft/2020-12/schema", f"Wrong schema dialect: {path.relative_to(ROOT)}")
        require(schema.get("$id") == SITE + route, f"Schema id mismatch: {path.relative_to(ROOT)}")


def check_works() -> None:
    payload = read_json(OUTPUTS["works"])
    source = read_json(ROOT / "works-index.json")
    works = payload["works"]
    require(payload["work_count"] == len(works) == len(source["works"]), "Normalized work counts disagree")
    require(payload["source"]["record_count"] == len(source["works"]), "Work source record_count mismatch")
    require(payload["source"]["sha256"] == sha256_file(ROOT / "works-index.json"), "Work source SHA-256 mismatch")
    ids = [work["id"] for work in works]
    graph_ids = [work["@id"] for work in works]
    require(len(ids) == len(set(ids)), "Duplicate normalized work id")
    require(len(graph_ids) == len(set(graph_ids)), "Duplicate normalized work @id")
    completeness_fields = {"version", "date", "version_doi", "languages", "license", "repository", "claim_boundary"}
    for work in works:
        require(work["primary_url"].startswith("https://"), f"Non-HTTPS primary URL in {work['id']}")
        for key in ("version_doi", "concept_doi"):
            doi = work["identifiers"][key]
            require(doi is None or bool(DOI_RE.fullmatch(doi)), f"Malformed {key} in {work['id']}: {doi!r}")
        for key in ("sha256", "archive_sha256"):
            value = work["integrity"][key]
            require(value is None or bool(SHA256_RE.fullmatch(value)), f"Malformed {key} in {work['id']}")
        known = set(work["metadata_completeness"]["known"])
        unknown = set(work["metadata_completeness"]["unknown"])
        require(not (known & unknown), f"Overlapping metadata completeness fields in {work['id']}")
        require(known | unknown == completeness_fields, f"Incomplete metadata completeness declaration in {work['id']}")

    jsonld = read_json(OUTPUTS["works_jsonld"])
    items = jsonld["itemListElement"]
    require(jsonld["numberOfItems"] == len(items) == len(works), "Scientific corpus JSON-LD count mismatch")
    require([item["item"]["@id"] for item in items] == graph_ids, "Scientific corpus JSON-LD order or ids mismatch")


def check_terms() -> None:
    payload = read_json(OUTPUTS["terms"])
    terms = payload["terms"]
    require(payload["term_count"] == len(terms), "Term count mismatch")
    require(payload["distinction_count"] == len(payload["distinctions"]), "Distinction count mismatch")
    ids = [term["term_id"] for term in terms]
    local_ids = [term["local_id"] for term in terms]
    require(len(ids) == len(set(ids)), "Duplicate term_id")
    require(len(local_ids) == len(set(local_ids)), "Duplicate local term id")
    required_core = {"a", "b", "c", "c-a-plus-b", "governed-plus", "l4-boundary"}
    require(required_core <= set(local_ids), f"Missing core terms: {sorted(required_core - set(local_ids))}")
    l4 = next(term for term in terms if term["local_id"] == "l4-boundary")
    require(l4["preferred_label"] == "L4 Boundary", "L4 Boundary must be the preferred machine label")
    require("L4" in l4["alternate_labels"], "L4 alias missing from L4 Boundary term")
    require("OSI transport layer" in l4["non_equivalents"], "L4 disambiguation boundary missing")
    plus = next(term for term in terms if term["local_id"] == "governed-plus")
    require("arithmetic addition" in plus["non_equivalents"], "Governed plus/arithmetic boundary missing")
    for name, path in {
        "canonical_map": ROOT / "canonical-map.json",
        "core_terms": ROOT / "content" / "machine" / "core-terms.json",
        "distinctions": ROOT / "distinctions.json",
    }.items():
        require(payload["source_hashes"][name] == sha256_file(path), f"Term source hash mismatch for {name}")
    jsonld = read_json(OUTPUTS["terms_jsonld"])
    require(len(jsonld["hasDefinedTerm"]) == len(terms), "Term JSON-LD count mismatch")


def check_bridges() -> None:
    payload = read_json(OUTPUTS["bridges"])
    bridges = payload["bridges"]
    require(payload["bridge_count"] == len(bridges), "Semantic bridge count mismatch")
    require(sum(item["visibility"] == "explicit" for item in bridges) >= 1, "At least one explicit semantic bridge is required")
    require(sum(item["visibility"] == "implicit" for item in bridges) >= 2, "At least two implicit semantic bridges are required")
    ids = [item["bridge_id"] for item in bridges]
    require(len(ids) == len(set(ids)), "Duplicate semantic bridge id")
    relation_uris = {item["relation_uri"] for item in payload["relation_definitions"]}
    for bridge in bridges:
        node_ids = {node["id"] for node in bridge["nodes"]}
        require(len(node_ids) == len(bridge["nodes"]), f"Duplicate node id in {bridge['bridge_id']}")
        for edge in bridge["edges"]:
            require(edge["source"] in node_ids and edge["target"] in node_ids, f"Dangling bridge edge in {bridge['bridge_id']}")
            require(edge["relation_uri"] in relation_uris, f"Undefined relation URI in {bridge['bridge_id']}")


def check_repositories() -> None:
    payload = read_json(OUTPUTS["repositories"])
    repositories = payload["repositories"]
    require(payload["repository_count"] == len(repositories) == 18, "Public repository inventory must contain 18 observed repositories")
    names = [item["name"] for item in repositories]
    require(len(names) == len(set(names)), "Duplicate public repository name")
    require("kot141078.github.io" in names, "Public site repository missing")
    require("ester-site" in names, "Archived legacy site repository missing")
    for item in repositories:
        require(bool(COMMIT_RE.fullmatch(item["observed_head_commit"])), f"Malformed observed commit for {item['name']}")
        require(item["repository_url"] == f"https://github.com/Kot141078/{item['name']}", f"Repository URL mismatch for {item['name']}")
        require(item["observed_commit_url"].endswith(item["observed_head_commit"]), f"Observed commit URL mismatch for {item['name']}")


def check_mot_c_source_pinning() -> None:
    def one(records: list[dict], predicate, label: str) -> dict:
        matches = [record for record in records if predicate(record)]
        require(len(matches) == 1, f"Expected exactly one MOT-c record in {label}, found {len(matches)}")
        return matches[0]

    def expect(record: dict, expected: dict[str, object], label: str) -> None:
        for field, value in expected.items():
            require(record.get(field) == value, f"MOT-c {label}.{field} is not pinned to the published source")

    work = one(
        read_json(ROOT / "works-index.json")["works"],
        lambda record: record.get("id") == MOT_C_PUBLICATION_ID,
        "works-index.json",
    )
    expect(
        work,
        {
            "github": MOT_C_TAG_SOURCE,
            "github_release_url": MOT_C_RELEASE_URL,
            "release_tag": MOT_C_RELEASE_TAG,
            "github_living_mirror": MOT_C_LIVING_SOURCE,
            "commit": MOT_C_SOURCE_COMMIT,
            "commit_url": MOT_C_COMMIT_SOURCE,
            "repository_path": MOT_C_REPOSITORY_PATH,
        },
        "works-index",
    )

    normalized_work = one(
        read_json(OUTPUTS["works"])["works"],
        lambda record: record.get("id") == MOT_C_PUBLICATION_ID,
        OUTPUTS["works"].name,
    )
    expect(
        normalized_work["source"],
        {
            "repository_url": MOT_C_REPOSITORY,
            "repository_detail_url": MOT_C_TAG_SOURCE,
            "repository_path": MOT_C_REPOSITORY_PATH,
            "release_url": MOT_C_RELEASE_URL,
            "release_tag": MOT_C_RELEASE_TAG,
            "commit": MOT_C_SOURCE_COMMIT,
        },
        "normalized-source",
    )

    library_item = one(
        read_json(ROOT / "library-index.json")["items"],
        lambda record: record.get("id") == MOT_C_PUBLICATION_ID,
        "library-index.json",
    )
    expect(
        library_item,
        {
            "repo_url": MOT_C_REPOSITORY,
            "release_url": MOT_C_RELEASE_URL,
            "source_url": MOT_C_TAG_SOURCE,
            "living_source_url": MOT_C_LIVING_SOURCE,
            "commit_url": MOT_C_COMMIT_SOURCE,
        },
        "library-index",
    )

    download_item = one(
        read_json(ROOT / "downloads-index.json")["items"],
        lambda record: record.get("publication_id") == MOT_C_PUBLICATION_ID
        and record.get("surface") == "GitHub corpus entry",
        "downloads-index.json",
    )
    expect(download_item, {"url": MOT_C_TAG_SOURCE, "commit_url": MOT_C_COMMIT_SOURCE}, "downloads-index")

    publication_machine = read_json(ROOT / MOT_C_REPOSITORY_PATH / "files" / "machine" / "index.json")
    expect(
        publication_machine,
        {
            "publication_id": MOT_C_PUBLICATION_ID,
            "github_corpus_entry": MOT_C_TAG_SOURCE,
            "github_living_mirror": MOT_C_LIVING_SOURCE,
            "github_release": MOT_C_RELEASE_URL,
            "source_tag": MOT_C_RELEASE_TAG,
            "source_commit": MOT_C_SOURCE_COMMIT,
            "source_commit_url": MOT_C_COMMIT_SOURCE,
        },
        "publication-machine-index",
    )

    linked_data = read_json(ROOT / MOT_C_REPOSITORY_PATH / "files" / "schema.org.jsonld")
    same_as = linked_data.get("sameAs")
    require(isinstance(same_as, list), "MOT-c Schema.org sameAs must be an array")
    require(
        {MOT_C_TAG_SOURCE, MOT_C_COMMIT_SOURCE, MOT_C_RELEASE_URL} <= set(same_as),
        "MOT-c Schema.org sameAs lacks stable tag, commit, or release provenance",
    )
    expect(
        linked_data,
        {"codeRepository": MOT_C_REPOSITORY, "isBasedOn": MOT_C_VERSION_DOI},
        "schema.org",
    )

    for relative in ("README.md", "llms.txt", "llms-full.txt", f"{MOT_C_REPOSITORY_PATH}/index.html"):
        require(
            MOT_C_TAG_SOURCE in (ROOT / relative).read_text(encoding="utf-8"),
            f"MOT-c stable tag source is missing from {relative}",
        )

    for relative in ("index.html", "publications/index.html", "library/index.html", "downloads/index.html"):
        text = (ROOT / relative).read_text(encoding="utf-8")
        require(MOT_C_TAG_SOURCE in text, f"MOT-c listing provenance lacks stable tag in {relative}")
        require(MOT_C_COMMIT_SOURCE in text, f"MOT-c listing provenance lacks stable commit in {relative}")


def protocol_payload(path: Path) -> dict:
    payload = read_json(path)
    return payload["data"] if "data" in payload and payload.get("kind") == "protocol_map" else payload


def check_protocol_map() -> None:
    source = protocol_payload(ROOT / "content" / "corpus" / "protocol-map.json")
    endpoint = protocol_payload(ROOT / "corpus-protocol-map.json")
    require(source == endpoint, "Protocol source and public endpoint payload differ")
    protocols = source["protocols"]
    require(source["record_count"] == len(protocols) == 17, "Protocol map must contain 17 records")
    all_ids = []
    for index, protocol in enumerate(protocols, start=1):
        require(protocol["protocol_map_id"] == f"PM-{index:03d}", "Protocol ids are malformed or out of order")
        related = protocol["related_artifact_ids"]
        source_ids = [item["artifact_id"] for item in protocol["source_refs"]]
        require(related == source_ids, f"Artifact relation mismatch in {protocol['protocol_map_id']}")
        require(all(isinstance(value, str) and ARTIFACT_ID_RE.fullmatch(value) for value in related), f"Malformed artifact id in {protocol['protocol_map_id']}")
        require(all(SHA256_RE.fullmatch(item["sha256"]) for item in protocol["source_refs"]), f"Malformed source hash in {protocol['protocol_map_id']}")
        all_ids.extend(related)
    require(Counter(all_ids) == Counter(f"A{index:03d}" for index in range(1, 61)), "Protocol map must cover A001 through A060 exactly once")


def check_machine_index() -> None:
    payload = read_json(OUTPUTS["machine_index"])
    expected_counts = {
        "normalized_works": read_json(OUTPUTS["works"])["work_count"],
        "terms": read_json(OUTPUTS["terms"])["term_count"],
        "distinctions": read_json(OUTPUTS["terms"])["distinction_count"],
        "semantic_bridges": read_json(OUTPUTS["bridges"])["bridge_count"],
        "public_repositories": read_json(OUTPUTS["repositories"])["repository_count"],
    }
    require(payload["counts"] == expected_counts, "Machine index counts disagree with child indexes")
    roles = [entry["role"] for entry in payload["entries"]]
    require(len(roles) == len(set(roles)), "Duplicate machine-index role")
    for entry in payload["entries"]:
        path = local_path_for_url(entry["url"])
        if path is not None:
            require(path.exists(), f"Machine-index target is missing: {entry['url']}")
        if entry["schema"]:
            schema_path = local_path_for_url(entry["schema"])
            require(schema_path is not None and schema_path.exists(), f"Machine-index schema is missing: {entry['schema']}")


def check_json_files() -> None:
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file() or path.suffix.lower() not in {".json", ".jsonld"}:
            continue
        read_json(path)


def page_url(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    if rel == "index.html":
        return SITE + "/"
    if rel.endswith("/index.html"):
        return SITE + "/" + rel[: -len("index.html")]
    return SITE + "/" + rel


def check_html_pages() -> None:
    ignored = {ROOT / "404.html", ROOT / "google1a6f459df5d54192.html"}
    checked = 0
    for path in sorted(ROOT.rglob("*.html")):
        if ".git" in path.parts or path in ignored or "artifacts" in path.parts:
            continue
        parser = PageParser()
        parser.feed(path.read_text(encoding="utf-8"))
        parser.close()
        rel = path.relative_to(ROOT)
        require(parser.doctype, f"Missing doctype in {rel}")
        require(bool(parser.lang), f"Missing html lang in {rel}")
        require(bool(parser.title), f"Missing title in {rel}")
        require(parser.h1_count == 1, f"Expected exactly one h1 in {rel}, found {parser.h1_count}")
        require(len(parser.canonicals) == 1, f"Expected exactly one canonical URL in {rel}")
        if parser.canonicals[0] != page_url(path):
            canonical_target = local_path_for_url(parser.canonicals[0])
            require(
                rel.parts[:1] == ("diary",) and canonical_target is not None and canonical_target.exists(),
                f"Canonical URL mismatch in {rel}: {parser.canonicals[0]!r}",
            )
            require(any("noindex" in value.split(",") for value in parser.robots), f"Canonical alias lacks noindex in {rel}")
        require(parser.images_without_alt == 0, f"Image without alt attribute in {rel}")
        for block_index, block in enumerate(parser.jsonld, start=1):
            try:
                json.loads(block)
            except json.JSONDecodeError as exc:
                raise CheckError(f"Invalid JSON-LD block {block_index} in {rel}: {exc}") from exc
        checked += 1
    require(checked >= 200, f"Unexpectedly low public HTML page count: {checked}")


def check_internal_html_links() -> None:
    ignored = {ROOT / "404.html", ROOT / "google1a6f459df5d54192.html"}
    missing: list[str] = []
    for path in sorted(ROOT.rglob("*.html")):
        if ".git" in path.parts or path in ignored or "artifacts" in path.parts:
            continue
        parser = PageParser()
        parser.feed(path.read_text(encoding="utf-8"))
        parser.close()
        base_url = page_url(path)
        for reference in parser.references:
            if not reference or reference.startswith(("#", "mailto:", "tel:", "data:", "javascript:")):
                continue
            absolute = urljoin(base_url, reference)
            target = local_path_for_url(absolute)
            if target is None:
                continue
            if not target.exists():
                missing.append(f"{path.relative_to(ROOT)} -> {reference} ({target.relative_to(ROOT)})")
    require(not missing, "Missing internal HTML targets:\n" + "\n".join(missing[:30]))


def check_discovery_files() -> None:
    robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
    require("User-agent: *" in robots and "Allow: /" in robots, "robots.txt does not allow public discovery")
    require(f"Sitemap: {SITE}/sitemap.xml" in robots, "robots.txt does not name the primary sitemap")

    llms = (ROOT / "llms.txt").read_text(encoding="utf-8")
    meaningful_lines = [line for line in llms.splitlines() if line.strip()]
    require(meaningful_lines and meaningful_lines[0].startswith("# "), "llms.txt must start with an H1 title")
    require(len(meaningful_lines) > 1 and meaningful_lines[1].startswith("> "), "llms.txt must place a summary blockquote after its title")
    require(len(re.findall(r"\[[^\]]+\]\(https://[^)]+\)", llms)) >= 10, "llms.txt must expose routes as Markdown links")
    for url in (
        f"{SITE}/machine-index.json",
        f"{SITE}/scientific-corpus-index.json",
        f"{SITE}/term-registry.json",
        f"{SITE}/semantic-bridges.json",
        f"{SITE}/public-repositories.json",
    ):
        require(url in llms, f"llms.txt does not expose {url}")

    index = (ROOT / "index.html").read_text(encoding="utf-8")
    require('rel="alternate" type="application/json" href="https://ivankotov.eu/machine-index.json"' in index, "Home page lacks machine-index alternate link")
    require('rel="alternate" type="application/ld+json" href="https://ivankotov.eu/scientific-corpus.jsonld"' in index, "Home page lacks corpus JSON-LD alternate link")

    tree = ET.parse(ROOT / "sitemap.xml")
    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locations = [element.text for element in tree.findall(".//sm:loc", namespace) if element.text]
    require(len(locations) == len(set(locations)), "sitemap.xml contains duplicate locations")
    for location in locations:
        target = local_path_for_url(location)
        require(target is not None and target.exists(), f"Sitemap target missing: {location}")
        if target.suffix.lower() == ".html":
            parser = PageParser()
            parser.feed(target.read_text(encoding="utf-8"))
            parser.close()
            require(parser.canonicals == [location], f"Sitemap lists a non-canonical HTML URL: {location}")


def check_diary_canonical_aliases() -> None:
    payload = read_json(ROOT / "diary-index.json")
    items = payload.get("items")
    require(isinstance(items, list), "diary-index.json must contain an items array")
    required_keys = {"slug", "page", "canonical_page", "identifier", "is_canonical"}
    aliases = []
    identifier_counts: Counter[str] = Counter()
    for item in items:
        require(isinstance(item, dict) and required_keys <= set(item), "Diary item lacks canonical identity fields")
        identifier_counts[item["identifier"]] += 1
        if not item["is_canonical"]:
            aliases.append(item)
    require(
        [(item["slug"], item["canonical_page"]) for item in aliases]
        == [(
            "there-is-a-difference-between-digital-immortality-and-what-i-would-call-post-anchor-continuity-0116",
            f"{SITE}/diary/there-is-a-difference-between-digital-immortality-and-what-i-would-call-post-anchor-continuity/",
        )],
        "Unexpected diary canonical-alias set",
    )
    duplicate_identifiers = {identifier: count for identifier, count in identifier_counts.items() if count > 1}
    require(len(duplicate_identifiers) == 1 and set(duplicate_identifiers.values()) == {2}, "Unexpected duplicate diary identifiers")

    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    sitemap = ET.parse(ROOT / "sitemap.xml")
    sitemap_dates: dict[str, str | None] = {}
    for url_node in sitemap.findall(".//sm:url", namespace):
        location = url_node.findtext("sm:loc", default="", namespaces=namespace)
        lastmod = url_node.findtext("sm:lastmod", default=None, namespaces=namespace)
        if location:
            sitemap_dates[location] = lastmod
    for item in items:
        if item["is_canonical"]:
            require(sitemap_dates.get(item["canonical_page"]) == item["date"], f"Diary sitemap lastmod mismatch: {item['slug']}")
        else:
            require(item["page"] not in sitemap_dates, f"Diary alias is present in sitemap: {item['slug']}")


def main() -> int:
    checks = [
        check_generated_outputs,
        check_schema_documents,
        check_works,
        check_terms,
        check_bridges,
        check_repositories,
        check_mot_c_source_pinning,
        check_protocol_map,
        check_machine_index,
        check_json_files,
        check_html_pages,
        check_internal_html_links,
        check_discovery_files,
        check_diary_canonical_aliases,
    ]
    try:
        for check in checks:
            check()
            print(f"PASS {check.__name__}")
        print(f"PASS machine readability gate ({len(checks)} checks)")
        return 0
    except (CheckError, KeyError, TypeError, ValueError) as exc:
        print(f"FAIL {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
