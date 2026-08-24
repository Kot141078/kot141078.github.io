from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parent.parent
TAP_ROOT = ROOT / "temporal-ai-presence"

CANONICAL_URL = "https://ivankotov.eu/temporal-ai-presence/"
INDEX_URL = f"{CANONICAL_URL}index.json"
SCHEMAORG_URL = f"{CANONICAL_URL}schemaorg.jsonld"
DEFINITION = "Temporal AI Presence = sustained bounded AI participation across time."
VERSION_DOI = "10.5281/zenodo.22070960"
CONCEPT_DOI = "10.5281/zenodo.22070959"
VERSION_DOI_URL = f"https://doi.org/{VERSION_DOI}"
CONCEPT_DOI_URL = f"https://doi.org/{CONCEPT_DOI}"
PROFILE_TAG = "temporal-ai-presence-v1.0"
BRIDGE_TAG = "temporal-ai-presence-implementation-bridge-v1.0"
PROFILE_TAG_URL = (
    "https://github.com/Kot141078/advanced-global-intelligence/tree/"
    f"{PROFILE_TAG}"
)
BRIDGE_TAG_URL = (
    "https://github.com/Kot141078/advanced-global-intelligence/tree/"
    f"{BRIDGE_TAG}"
)
BRIDGE_RELEASE_URL = (
    "https://github.com/Kot141078/advanced-global-intelligence/releases/tag/"
    f"{BRIDGE_TAG}"
)
T03_STATUS = "PUBLIC_PARTIAL_WITH_DEPLOYMENT_EXTERNAL_BOUNDARY"
T03_BOUNDARY = (
    "Deployment activation, external orchestrator state, production pause/revoke "
    "enforcement, and deployment-level witness activation are not fully verified."
)
EXPECTED_MATRIX = {
    "TAP-T01": "PUBLIC_VERIFIED",
    "TAP-T02": "PUBLIC_VERIFIED",
    "TAP-T03": T03_STATUS,
    "TAP-T04": "PUBLIC_VERIFIED",
    "TAP-T05": "PUBLIC_VERIFIED",
    "TAP-T06": "PUBLIC_VERIFIED",
    "TAP-T07": "PUBLIC_VERIFIED",
    "TAP-T08": "PUBLIC_VERIFIED",
    "TAP-T09": "PUBLIC_VERIFIED",
    "TAP-T10": "PUBLIC_VERIFIED",
}


class TapSurfaceError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise TapSurfaceError(message)


def require_no_overclaim(raw: str, context: str) -> None:
    patterns = {
        "TAP-C claimed": r"\bTAP[-_]C\s*=\s*CLAIMED\b|\"TAP[_-]C\"\s*:\s*\"CLAIMED\"",
        "M4 full pass": r"\bM4_FULL_PASS\s*=\s*true\b|\"M4_FULL_PASS\"\s*:\s*true",
        "TAP-T03 fully verified": r"\"TAP-T03\"\s*:\s*\"PUBLIC_VERIFIED\"|\bTAP-T03\s*[:=]\s*PUBLIC_VERIFIED\b|<tr[^>]*>(?:(?!</tr>).)*TAP-T03(?:(?!</tr>).)*PUBLIC_VERIFIED(?:(?!</tr>).)*</tr>",
    }
    for label, pattern in patterns.items():
        require(re.search(pattern, raw, re.IGNORECASE | re.DOTALL) is None, f"{context}: contradictory {label} claim")


def normalize_text(parts: list[str] | str) -> str:
    value = "".join(parts) if isinstance(parts, list) else parts
    return " ".join(value.split())


class TapHtmlParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.canonical_links: list[str] = []
        self.alternate_links: dict[str, list[str]] = {}
        self.absolute_urls: list[str] = []
        self.text_parts: list[str] = []
        self.rows: list[list[str]] = []
        self.jsonld_blocks: list[str] = []
        self._row: list[str] | None = None
        self._cell: list[str] | None = None
        self._jsonld: list[str] | None = None
        self._suppressed_text_depth = 0

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        attributes = {name: value or "" for name, value in attrs}
        for name in ("href", "src", "content"):
            value = attributes.get(name, "")
            if value.startswith(("https://", "http://")):
                self.absolute_urls.append(value)

        if tag == "link":
            rel = set(attributes.get("rel", "").lower().split())
            href = attributes.get("href", "")
            if "canonical" in rel:
                self.canonical_links.append(href)
            if "alternate" in rel:
                media_type = attributes.get("type", "")
                self.alternate_links.setdefault(media_type, []).append(href)

        if tag in {"style", "script"}:
            self._suppressed_text_depth += 1
        if tag == "script" and attributes.get("type", "").lower() == "application/ld+json":
            self._jsonld = []
        if tag == "tr":
            self._row = []
        elif tag in {"td", "th"} and self._row is not None:
            self._cell = []

    def handle_endtag(self, tag: str) -> None:
        if tag in {"td", "th"} and self._row is not None and self._cell is not None:
            self._row.append(normalize_text(self._cell))
            self._cell = None
        elif tag == "tr" and self._row is not None:
            self.rows.append(self._row)
            self._row = None
            self._cell = None

        if tag == "script" and self._jsonld is not None:
            self.jsonld_blocks.append("".join(self._jsonld))
            self._jsonld = None
        if tag in {"style", "script"} and self._suppressed_text_depth:
            self._suppressed_text_depth -= 1

    def handle_data(self, data: str) -> None:
        if self._jsonld is not None:
            self._jsonld.append(data)
        if self._cell is not None:
            self._cell.append(data)
        if self._suppressed_text_depth == 0:
            self.text_parts.append(data)


def load_json(path: Path) -> Any:
    value = json.loads(path.read_text(encoding="utf-8"))
    require(isinstance(value, dict), f"{path.name}: top level must be an object")
    return value


def iter_strings(value: Any):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for item in value.values():
            yield from iter_strings(item)
    elif isinstance(value, list):
        for item in value:
            yield from iter_strings(item)


def validate_canonical_host(values: list[str], context: str) -> None:
    checked = 0
    for value in values:
        parsed = urlsplit(value)
        hostname = (parsed.hostname or "").lower()
        if hostname == "ivankotov.eu" or hostname.endswith(".ivankotov.eu"):
            checked += 1
            require(parsed.scheme == "https", f"{context}: site URL is not HTTPS: {value}")
            require(hostname == "ivankotov.eu", f"{context}: non-canonical host: {value}")
            require(parsed.port is None, f"{context}: canonical URL contains a port: {value}")
            require(parsed.username is None, f"{context}: canonical URL contains userinfo: {value}")
    require(checked > 0, f"{context}: no canonical-host URL found")


def jsonld_nodes(document: dict[str, Any]) -> list[dict[str, Any]]:
    graph = document.get("@graph")
    if isinstance(graph, list):
        return [node for node in graph if isinstance(node, dict)]
    return [document]


def node_of_type(nodes: list[dict[str, Any]], node_type: str) -> dict[str, Any]:
    matches = [node for node in nodes if node.get("@type") == node_type]
    require(len(matches) == 1, f"schemaorg.jsonld: expected one {node_type}, found {len(matches)}")
    return matches[0]


def property_values(node: dict[str, Any]) -> dict[str, Any]:
    values = node.get("additionalProperty")
    require(isinstance(values, list), "schemaorg.jsonld: additionalProperty must be a list")
    result: dict[str, Any] = {}
    for value in values:
        require(isinstance(value, dict), "schemaorg.jsonld: malformed PropertyValue")
        name = value.get("name")
        require(isinstance(name, str), "schemaorg.jsonld: PropertyValue name missing")
        require(name not in result, f"schemaorg.jsonld: duplicate PropertyValue {name}")
        result[name] = value.get("value")
    return result


def validate_html(path: Path) -> dict[str, Any]:
    raw = path.read_text(encoding="utf-8")
    require_no_overclaim(raw, "index.html")
    parser = TapHtmlParser()
    parser.feed(raw)
    parser.close()
    text = normalize_text(parser.text_parts)

    require(parser.canonical_links == [CANONICAL_URL], "index.html: canonical link mismatch")
    require(parser.alternate_links.get("application/json") == [INDEX_URL], "index.html: JSON alternate mismatch")
    require(
        parser.alternate_links.get("application/ld+json") == [SCHEMAORG_URL],
        "index.html: JSON-LD alternate mismatch",
    )
    validate_canonical_host(parser.absolute_urls, "index.html")
    require(DEFINITION in text, "index.html: exact TAP definition missing")
    for value, label in (
        (VERSION_DOI, "Version DOI"),
        (CONCEPT_DOI, "Concept DOI"),
        (PROFILE_TAG, "profile tag"),
        (BRIDGE_TAG, "bridge tag"),
    ):
        require(value in raw, f"index.html: exact {label} missing")

    matrix: dict[str, str] = {}
    for row in parser.rows:
        if len(row) >= 3 and re.fullmatch(r"TAP-T\d{2}", row[0]):
            require(row[0] not in matrix, f"index.html: duplicate matrix row {row[0]}")
            matrix[row[0]] = row[2]
    require(matrix == EXPECTED_MATRIX, "index.html: T01-T10 matrix mismatch")
    require(T03_BOUNDARY in text, "index.html: exact T03 deployment boundary missing")
    require("M4_FULL_PASS=false" in text, "index.html: M4_FULL_PASS=false missing")
    require("TAP-C=NOT CLAIMED" in text, "index.html: TAP-C=NOT CLAIMED missing")

    require(parser.jsonld_blocks, "index.html: embedded JSON-LD missing")
    embedded_documents = [json.loads(block) for block in parser.jsonld_blocks]
    embedded_strings = list(iter_strings(embedded_documents))
    validate_canonical_host(embedded_strings, "index.html embedded JSON-LD")
    embedded_nodes = [node for document in embedded_documents for node in jsonld_nodes(document)]
    embedded_pages = [node for node in embedded_nodes if node.get("@type") == "WebPage"]
    require(embedded_pages, "index.html: embedded WebPage JSON-LD missing")
    require(
        any(node.get("url") == CANONICAL_URL for node in embedded_pages),
        "index.html: embedded WebPage canonical URL mismatch",
    )
    embedded_serialized = json.dumps(embedded_documents, ensure_ascii=False, sort_keys=True)
    for value, label in (
        (DEFINITION, "definition"),
        (VERSION_DOI_URL, "Version DOI"),
        (BRIDGE_TAG, "bridge tag"),
    ):
        require(value in embedded_serialized, f"index.html: embedded JSON-LD {label} mismatch")
    return {"matrix": matrix}


def validate_index_json(path: Path) -> dict[str, Any]:
    document = load_json(path)
    require_no_overclaim(json.dumps(document, ensure_ascii=False), "index.json")
    validate_canonical_host(list(iter_strings(document)), "index.json")
    require(document.get("canonical_url") == CANONICAL_URL, "index.json: canonical URL mismatch")
    require(document.get("definition") == DEFINITION, "index.json: definition mismatch")
    require(document.get("version_doi") == VERSION_DOI, "index.json: Version DOI mismatch")
    require(document.get("concept_doi") == CONCEPT_DOI, "index.json: Concept DOI mismatch")

    profile = document.get("profile")
    bridge = document.get("implementation_bridge")
    require(isinstance(profile, dict), "index.json: profile object missing")
    require(isinstance(bridge, dict), "index.json: implementation_bridge object missing")
    require(profile.get("tag") == PROFILE_TAG, "index.json: profile tag mismatch")
    require(profile.get("tag_url") == PROFILE_TAG_URL, "index.json: profile tag URL mismatch")
    require(bridge.get("tag") == BRIDGE_TAG, "index.json: bridge tag mismatch")
    require(bridge.get("tag_url") == BRIDGE_TAG_URL, "index.json: bridge tag URL mismatch")
    require(bridge.get("release_url") == BRIDGE_RELEASE_URL, "index.json: bridge release URL mismatch")

    tests = document.get("tests")
    require(isinstance(tests, list), "index.json: tests must be a list")
    matrix: dict[str, str] = {}
    test_rows: dict[str, dict[str, Any]] = {}
    for row in tests:
        require(isinstance(row, dict), "index.json: malformed test row")
        test_id = row.get("id")
        status = row.get("status")
        require(isinstance(test_id, str), "index.json: test id missing")
        require(isinstance(status, str), f"index.json: status missing for {test_id}")
        require(test_id not in matrix, f"index.json: duplicate test id {test_id}")
        matrix[test_id] = status
        test_rows[test_id] = row
    require(matrix == EXPECTED_MATRIX, "index.json: T01-T10 tests mismatch")
    require(document.get("effective_public_matrix") == EXPECTED_MATRIX, "index.json: effective matrix mismatch")
    require(test_rows["TAP-T03"].get("boundary") == T03_BOUNDARY, "index.json: T03 boundary mismatch")

    ceiling = document.get("claim_ceiling")
    require(isinstance(ceiling, dict), "index.json: claim_ceiling object missing")
    require(ceiling.get("M4_FULL_PASS") is False, "index.json: M4_FULL_PASS must be false")
    require(ceiling.get("TAP_C") == "NOT_CLAIMED", "index.json: TAP_C must be NOT_CLAIMED")
    require(ceiling.get("T03") == T03_STATUS, "index.json: T03 claim ceiling mismatch")
    for test_id in ("TAP-T02", "TAP-T06", "TAP-T07", "TAP-T08"):
        require(matrix[test_id] == "PUBLIC_VERIFIED", f"index.json: {test_id} is not PUBLIC_VERIFIED")
    return document


def validate_schemaorg(path: Path) -> dict[str, Any]:
    document = load_json(path)
    require_no_overclaim(json.dumps(document, ensure_ascii=False), "schemaorg.jsonld")
    strings = list(iter_strings(document))
    validate_canonical_host(strings, "schemaorg.jsonld")
    nodes = jsonld_nodes(document)
    webpage = node_of_type(nodes, "WebPage")
    term = node_of_type(nodes, "DefinedTerm")
    article = node_of_type(nodes, "ScholarlyArticle")
    source = node_of_type(nodes, "SoftwareSourceCode")

    require(webpage.get("url") == CANONICAL_URL, "schemaorg.jsonld: WebPage canonical URL mismatch")
    require(webpage.get("description") == DEFINITION, "schemaorg.jsonld: WebPage definition mismatch")
    require(term.get("url") == CANONICAL_URL, "schemaorg.jsonld: DefinedTerm canonical URL mismatch")
    require(term.get("description") == DEFINITION, "schemaorg.jsonld: DefinedTerm definition mismatch")
    require(article.get("@id") == VERSION_DOI_URL, "schemaorg.jsonld: primary Version DOI mismatch")
    require(article.get("url") == VERSION_DOI_URL, "schemaorg.jsonld: article URL mismatch")

    serialized = json.dumps(document, ensure_ascii=False, sort_keys=True)
    for value, label in (
        (VERSION_DOI, "Version DOI"),
        (CONCEPT_DOI, "Concept DOI"),
        (PROFILE_TAG, "profile tag"),
        (BRIDGE_TAG, "bridge tag"),
    ):
        require(value in serialized, f"schemaorg.jsonld: exact {label} missing")
    require(source.get("@id") == BRIDGE_RELEASE_URL, "schemaorg.jsonld: bridge release identity mismatch")

    article_identifiers = article.get("identifier")
    require(isinstance(article_identifiers, list), "schemaorg.jsonld: article identifiers missing")
    identifier_values = {
        item.get("propertyID"): item.get("value")
        for item in article_identifiers
        if isinstance(item, dict)
    }
    require(identifier_values.get("DOI") == VERSION_DOI, "schemaorg.jsonld: DOI identifier mismatch")
    require(identifier_values.get("Concept DOI") == CONCEPT_DOI, "schemaorg.jsonld: Concept DOI identifier mismatch")

    source_identifiers = source.get("identifier")
    require(isinstance(source_identifiers, list), "schemaorg.jsonld: source identifiers missing")
    source_identifier_values = {
        item.get("propertyID"): item.get("value")
        for item in source_identifiers
        if isinstance(item, dict)
    }
    require(source_identifier_values.get("Git tag") == BRIDGE_TAG, "schemaorg.jsonld: bridge Git tag mismatch")

    claims = property_values(term)
    require(claims.get("M4_FULL_PASS") is False, "schemaorg.jsonld: M4_FULL_PASS must be false")
    require(claims.get("TAP-C") == "NOT_CLAIMED", "schemaorg.jsonld: TAP-C must be NOT_CLAIMED")
    require(claims.get("TAP-T03") == T03_STATUS, "schemaorg.jsonld: T03 boundary mismatch")
    return document


def main() -> int:
    html_result = validate_html(TAP_ROOT / "index.html")
    index_document = validate_index_json(TAP_ROOT / "index.json")
    schema_document = validate_schemaorg(TAP_ROOT / "schemaorg.jsonld")

    require(html_result["matrix"] == index_document["effective_public_matrix"], "HTML/JSON matrix disagreement")
    for value, label in (
        (DEFINITION, "definition"),
        (VERSION_DOI, "Version DOI"),
        (CONCEPT_DOI, "Concept DOI"),
        (PROFILE_TAG, "profile tag"),
        (BRIDGE_TAG, "bridge tag"),
    ):
        require(value in json.dumps(schema_document, ensure_ascii=False), f"cross-surface {label} mismatch")

    print("TAP_R4_CLAIM_CONSISTENCY_PASS")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, UnicodeError, json.JSONDecodeError, TapSurfaceError) as exc:
        print(f"TAP_R4_CLAIM_CONSISTENCY_FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
