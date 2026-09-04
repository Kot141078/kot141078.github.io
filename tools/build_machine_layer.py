from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parent.parent
SITE = "https://ivankotov.eu"
OWNER = "Kot141078"
LAST_VERIFIED = "2026-09-04"

WORKS_SOURCE = ROOT / "works-index.json"
CANONICAL_SOURCE = ROOT / "canonical-map.json"
DISTINCTIONS_SOURCE = ROOT / "distinctions.json"
REPOSITORIES_SOURCE = ROOT / "content" / "machine" / "public-repositories.json"
CORE_TERMS_SOURCE = ROOT / "content" / "machine" / "core-terms.json"
BRIDGES_SOURCE = ROOT / "content" / "machine" / "semantic-bridges.json"

OUTPUTS = {
    "machine_index": ROOT / "machine-index.json",
    "works": ROOT / "scientific-corpus-index.json",
    "works_jsonld": ROOT / "scientific-corpus.jsonld",
    "terms": ROOT / "term-registry.json",
    "terms_jsonld": ROOT / "term-registry.jsonld",
    "bridges": ROOT / "semantic-bridges.json",
    "repositories": ROOT / "public-repositories.json",
}

SCHEMAS = {
    "machine_index": "/schemas/machine-index-v1.schema.json",
    "works": "/schemas/scientific-corpus-index-v1.schema.json",
    "terms": "/schemas/term-registry-v1.schema.json",
    "bridges": "/schemas/semantic-bridges-v1.schema.json",
    "repositories": "/schemas/public-repositories-v1.schema.json",
}

DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$", re.IGNORECASE)
SHA256_RE = re.compile(r"^[0-9a-fA-F]{64}$")
BCP47_RE = re.compile(r"^[A-Za-z]{2,3}(?:-[A-Za-z0-9]{2,8})*$")


class BuildError(RuntimeError):
    pass


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise BuildError(f"Missing required source: {path.relative_to(ROOT)}") from exc
    except json.JSONDecodeError as exc:
        raise BuildError(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}") from exc


def json_text(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=False) + "\n"


def sha256_file(path: Path) -> str:
    # Source JSON hashes are machine-contract identifiers, so keep them stable
    # across Windows CRLF checkouts and Linux CI LF checkouts.
    return hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def clean_string(value: Any) -> str | None:
    if not isinstance(value, str):
        return None
    value = value.strip()
    return value or None


def first_string(record: dict[str, Any], fields: list[str]) -> str | None:
    for field in fields:
        value = clean_string(record.get(field))
        if value:
            return value
    return None


def normalize_doi(value: Any) -> str | None:
    value = clean_string(value)
    if not value:
        return None
    value = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", value, flags=re.IGNORECASE)
    value = re.sub(r"^doi:\s*", "", value, flags=re.IGNORECASE)
    value = value.strip().rstrip(".,")
    if not DOI_RE.fullmatch(value):
        return None
    return f"https://doi.org/{value}"


def normalize_sha256(value: Any) -> str | None:
    value = clean_string(value)
    if value and SHA256_RE.fullmatch(value):
        return value.lower()
    return None


def github_repository(record: dict[str, Any]) -> tuple[str | None, str | None]:
    candidates = [
        "repository_url",
        "github",
        "github_url",
        "github_package",
        "repository_package",
        "secondary_url",
        "repository",
        "repo",
    ]
    for field in candidates:
        value = clean_string(record.get(field))
        if not value:
            continue
        if value.startswith("https://github.com/"):
            parts = [part for part in urlsplit(value).path.split("/") if part]
            if len(parts) >= 2:
                return f"https://github.com/{parts[0]}/{parts[1]}", value
        if re.fullmatch(r"[A-Za-z0-9_.-]+", value):
            return f"https://github.com/{OWNER}/{value}", f"https://github.com/{OWNER}/{value}"
        if re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", value):
            return f"https://github.com/{value}", f"https://github.com/{value}"
    return None, None


def schema_org_type(source_type: str) -> str:
    lowered = source_type.lower()
    if "book" in lowered:
        return "Book"
    if "software" in lowered:
        return "SoftwareSourceCode"
    if "paper" in lowered:
        return "ScholarlyArticle"
    return "CreativeWork"


def language_values(record: dict[str, Any]) -> tuple[list[str], list[str]]:
    raw = record.get("languages", record.get("language", record.get("inLanguage")))
    if isinstance(raw, str):
        values = [raw]
    elif isinstance(raw, list):
        values = [str(item).strip() for item in raw if str(item).strip()]
    else:
        values = []
    codes = [value for value in values if BCP47_RE.fullmatch(value)]
    labels = [value for value in values if value not in codes]
    return codes, labels


def non_claims(record: dict[str, Any]) -> tuple[list[str], str | None]:
    for field in ("non_claims", "not"):
        value = record.get(field)
        if isinstance(value, list):
            return [str(item).strip() for item in value if str(item).strip()], field
    return [], None


def normalize_work(record: dict[str, Any], index: int) -> dict[str, Any]:
    record_id = clean_string(record.get("id"))
    title = clean_string(record.get("title"))
    source_type = clean_string(record.get("type"))
    role = clean_string(record.get("role"))
    primary_url = clean_string(record.get("primary_url"))
    if not all((record_id, title, source_type, role, primary_url)):
        raise BuildError(f"works-index.json record {index} is missing id, title, type, role, or primary_url")
    if not primary_url.startswith("https://"):
        raise BuildError(f"Work {record_id} has a non-HTTPS primary_url")

    version_doi = normalize_doi(first_string(record, ["version_doi", "doi_url", "doi", "doi_identifier", "doi_value"]))
    concept_doi = normalize_doi(first_string(record, ["concept_doi_url", "concept_doi", "full_technical_corpus_concept_doi_url", "full_technical_corpus_concept_doi"]))
    published_doi = normalize_doi(first_string(record, ["published_doi_url", "published_doi"]))
    doi_role = clean_string(record.get("doi_role"))
    if doi_role and doi_role not in {"version", "concept", "unresolved"}:
        raise BuildError(f"Work {record_id} has an unsupported DOI role: {doi_role}")
    if doi_role == "unresolved":
        if not published_doi:
            raise BuildError(f"Work {record_id} has unresolved DOI role without a published DOI")
        if version_doi or concept_doi:
            raise BuildError(f"Work {record_id} assigns a version or concept DOI while DOI role is unresolved")
    elif not published_doi and version_doi:
        published_doi = version_doi
        doi_role = doi_role or "version"
    repository_url, repository_detail_url = github_repository(record)
    language_codes, language_labels = language_values(record)
    boundaries, boundary_source_field = non_claims(record)

    release_url = first_string(record, ["github_release_url", "release_url", "github_release", "release", "first_release_url"])
    if release_url and not release_url.startswith("https://"):
        release_url = None
    commit = first_string(record, ["commit", "source_commit", "reader_machine_commit", "release_source_commit"])
    if commit and not re.fullmatch(r"[0-9a-fA-F]{7,40}", commit):
        commit = None

    integrity = {
        "sha256": normalize_sha256(first_string(record, ["sha256", "master_pdf_sha256"])),
        "archive_sha256": normalize_sha256(first_string(record, ["archive_sha256", "zip_sha256", "master_pdf_sha256"])),
        "manifest_url": first_string(record, ["manifest_url", "sha_manifest", "artifact_checksums_url"]),
        "checksums_url": first_string(record, ["sha256sums_url", "sha256_url", "github_placement_checksums_url"]),
    }
    licenses = {
        "overall": clean_string(record.get("license")),
        "software": clean_string(record.get("license_code")),
        "documentation": clean_string(record.get("license_docs")),
        "machine_metadata": clean_string(record.get("license_machine")),
        "rights": clean_string(record.get("rights")),
    }
    known = []
    unknown = []
    completeness_fields = {
        "version": clean_string(record.get("version")),
        "date": first_string(record, ["date", "publication_date", "first_publication_date", "package_date"]),
        "version_doi": version_doi,
        "languages": language_codes or language_labels,
        "license": any(licenses.values()),
        "repository": repository_url,
        "claim_boundary": boundaries,
    }
    for field, value in completeness_fields.items():
        (known if value else unknown).append(field)

    return {
        "id": record_id,
        "@id": f"{SITE}/id/work/{record_id}",
        "schema_org_type": schema_org_type(source_type),
        "source_type": source_type,
        "title": title,
        "alternative_title": clean_string(record.get("alternative_title")),
        "role": role,
        "summary": clean_string(record.get("summary")),
        "primary_url": primary_url,
        "version": clean_string(record.get("version")),
        "date": first_string(record, ["date", "publication_date", "first_publication_date", "package_date"]),
        "status": clean_string(record.get("status")),
        "languages": language_codes,
        "source_language_labels": language_labels,
        "identifiers": {
            "published_doi": published_doi,
            "doi_role": doi_role,
            "version_doi": version_doi,
            "concept_doi": concept_doi,
            "other": [clean_string(record.get("identifier"))] if clean_string(record.get("identifier")) else [],
        },
        "source": {
            "repository_url": repository_url,
            "repository_detail_url": repository_detail_url,
            "repository_path": first_string(record, ["repository_path", "root_path"]),
            "release_url": release_url,
            "release_tag": first_string(record, ["release_tag", "tag"]),
            "commit": commit.lower() if commit else None,
        },
        "licenses": licenses,
        "integrity": integrity,
        "claim_boundary": {
            "non_claims": boundaries,
            "source_field": boundary_source_field,
            "rule": "Publication, DOI, repository presence, checksum, or internal review does not by itself establish implementation, reproduction, validation, safety, entity status, consciousness, personhood, or deployment authorization.",
        },
        "metadata_completeness": {"known": known, "unknown": unknown},
        "legacy_source_pointer": f"/works-index.json#/works/{index}",
    }


def build_works() -> tuple[dict[str, Any], dict[str, Any]]:
    source = read_json(WORKS_SOURCE)
    works = source.get("works")
    if not isinstance(works, list):
        raise BuildError("works-index.json must contain a works array")
    normalized = [normalize_work(record, index) for index, record in enumerate(works)]
    ids = [record["id"] for record in normalized]
    if len(ids) != len(set(ids)):
        raise BuildError("works-index.json contains duplicate work ids")

    payload = {
        "$schema": SITE + SCHEMAS["works"],
        "schema_version": "scientific-corpus-index.v1",
        "document_id": "ivankotov-public-authored-corpus-index-v1",
        "url": f"{SITE}/scientific-corpus-index.json",
        "last_verified": LAST_VERIFIED,
        "author": {
            "name": "Ivan Kotov",
            "orcid": "https://orcid.org/0009-0009-6002-9845",
            "profile": f"{SITE}/about/",
        },
        "scope": "Normalized discovery layer for public research, software, protocol, book, and authorial-statement records listed in works-index.json.",
        "authority_rule": "This index is a routing projection. DOI records, signed releases, tagged repository states, and explicitly named canonical source files retain their stated authority.",
        "claim_boundary": "Listing, normalization, or JSON-LD typing does not elevate scientific, technical, legal, empirical, continuity, entity, consciousness, personhood, safety, certification, or deployment claims.",
        "source": {
            "url": f"{SITE}/works-index.json",
            "sha256": sha256_file(WORKS_SOURCE),
            "record_count": len(works),
        },
        "work_count": len(normalized),
        "works": normalized,
    }

    item_list = []
    for position, record in enumerate(normalized, start=1):
        item: dict[str, Any] = {
            "@type": record["schema_org_type"],
            "@id": record["@id"],
            "name": record["title"],
            "url": record["primary_url"],
            "creator": {"@id": f"{SITE}/about/#person"},
        }
        if record["version"]:
            item["version"] = record["version"]
        if record["date"]:
            item["datePublished"] = record["date"]
        if record["summary"]:
            item["description"] = record["summary"]
        if record["languages"]:
            item["inLanguage"] = record["languages"]
        identifiers: list[str] = []
        for value in (
            record["identifiers"]["published_doi"],
            record["identifiers"]["version_doi"],
            record["identifiers"]["concept_doi"],
            *record["identifiers"]["other"],
        ):
            if isinstance(value, str) and value and value not in identifiers:
                identifiers.append(value)
        if identifiers:
            item["identifier"] = identifiers
        item_list.append({"@type": "ListItem", "position": position, "item": item})
    jsonld = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "@id": f"{SITE}/scientific-corpus.jsonld",
        "url": f"{SITE}/scientific-corpus-index.json",
        "name": "Ivan Kotov public authored corpus — normalized machine index",
        "numberOfItems": len(item_list),
        "itemListOrder": "https://schema.org/ItemListOrderAscending",
        "itemListElement": item_list,
    }
    return payload, jsonld


def canonical_term_records() -> list[dict[str, Any]]:
    canonical = read_json(CANONICAL_SOURCE)
    nodes = canonical.get("nodes")
    if not isinstance(nodes, list):
        raise BuildError("canonical-map.json must contain a nodes array")
    work_summaries = {
        item.get("id"): item.get("summary")
        for item in read_json(WORKS_SOURCE).get("works", [])
        if isinstance(item, dict) and clean_string(item.get("id")) and clean_string(item.get("summary"))
    }
    records = []
    for node in nodes:
        local_id = clean_string(node.get("id"))
        title = clean_string(node.get("title"))
        source = clean_string(node.get("url"))
        definition = (
            clean_string(node.get("summary"))
            or clean_string(node.get("canonical_text"))
            or clean_string(work_summaries.get(local_id))
        )
        if not all((local_id, title, source, definition)):
            raise BuildError("canonical-map.json contains an incomplete node")
        if local_id == "l4":
            continue
        records.append(
            {
                "term_id": f"{SITE}/terms/{local_id}",
                "local_id": local_id,
                "preferred_label": title,
                "alternate_labels": [],
                "long_form": None,
                "definition": definition,
                "scope": "Public corpus routing definition.",
                "authoritative_source": source,
                "source_version": clean_string(node.get("version")),
                "status": "site-canonical-routing",
                "non_equivalents": [str(item) for item in node.get("not", []) if str(item).strip()],
                "related_terms": [],
                "language": "en",
            }
        )
    return records


def build_terms() -> tuple[dict[str, Any], dict[str, Any]]:
    source = read_json(CORE_TERMS_SOURCE)
    extra = source.get("terms")
    if not isinstance(extra, list):
        raise BuildError("core-terms.json must contain a terms array")
    terms = canonical_term_records()
    for item in extra:
        local_id = clean_string(item.get("local_id"))
        if not local_id:
            raise BuildError("core-terms.json contains a term without local_id")
        record = dict(item)
        record["term_id"] = f"{SITE}/terms/{local_id}"
        terms.append(record)
    terms.sort(key=lambda item: item["local_id"])
    ids = [item["term_id"] for item in terms]
    if len(ids) != len(set(ids)):
        raise BuildError("Term registry contains duplicate term_id values")

    distinctions = read_json(DISTINCTIONS_SOURCE).get("distinctions")
    if not isinstance(distinctions, list):
        raise BuildError("distinctions.json must contain a distinctions array")
    boundaries = []
    for index, item in enumerate(distinctions):
        term = clean_string(item.get("term"))
        not_value = clean_string(item.get("not"))
        why = clean_string(item.get("why"))
        primary_url = clean_string(item.get("primary_url"))
        if not all((term, not_value, why, primary_url)):
            raise BuildError(f"distinctions.json record {index} is incomplete")
        boundaries.append(
            {
                "boundary_id": clean_string(item.get("identifier")) or f"{SITE}/id/distinction/{index + 1:03d}",
                "term": term,
                "non_equivalent_to": not_value,
                "reason": why,
                "authoritative_source": primary_url,
            }
        )

    payload = {
        "$schema": SITE + SCHEMAS["terms"],
        "schema_version": "term-registry.v1",
        "document_id": "ivankotov-public-term-registry-v1",
        "url": f"{SITE}/term-registry.json",
        "last_verified": LAST_VERIFIED,
        "preferred_label_rule": "Use preferred_label in new machine-facing records. alternate_labels are discovery aliases, not strict equivalents outside the declared scope.",
        "claim_boundary": source["claim_boundary"],
        "source_hashes": {
            "canonical_map": sha256_file(CANONICAL_SOURCE),
            "core_terms": sha256_file(CORE_TERMS_SOURCE),
            "distinctions": sha256_file(DISTINCTIONS_SOURCE),
        },
        "term_count": len(terms),
        "terms": terms,
        "distinction_count": len(boundaries),
        "distinctions": boundaries,
    }
    jsonld = {
        "@context": "https://schema.org",
        "@type": "DefinedTermSet",
        "@id": f"{SITE}/term-registry.jsonld",
        "url": f"{SITE}/term-registry.json",
        "name": "Ivan Kotov public corpus term registry",
        "hasDefinedTerm": [
            {
                "@type": "DefinedTerm",
                "@id": term["term_id"],
                "termCode": term["local_id"],
                "name": term["preferred_label"],
                "alternateName": term["alternate_labels"],
                "description": term["definition"],
                "inDefinedTermSet": {"@id": f"{SITE}/term-registry.jsonld"},
                "url": term["authoritative_source"],
                "inLanguage": term["language"],
            }
            for term in terms
        ],
    }
    return payload, jsonld


RELATION_DEFINITIONS = {
    "requiresBoundary": "The source reading depends on the target boundary being applied.",
    "constrainsExecution": "The source boundary limits execution represented by the target.",
    "producesCandidateRecordFor": "The source may produce a record that remains only a candidate for the target evidence surface.",
    "suppliesCandidateEvidenceTo": "The source may supply candidate evidence to the target without automatic admission.",
    "doesNotEntail": "The source does not by itself establish the target.",
    "suppliesLongitudinalEvidenceTo": "The source may supply time-ordered evidence to the target control layer.",
    "constrainsClassificationIn": "The source limits classifications available in the target framework.",
    "mayPerformWithoutCollapsing": "One actor may perform target roles while the roles remain semantically and authoritatively distinct.",
    "hasPublicArchitectureToCodeEvidenceFor": "The source has a public, immutable, and reproducible architecture-to-code evidence route at the target.",
    "doesNotClose": "The source does not close the target boundary.",
}


def build_bridges() -> dict[str, Any]:
    source = read_json(BRIDGES_SOURCE)
    bridges = source.get("bridges")
    if not isinstance(bridges, list):
        raise BuildError("semantic-bridges.json source must contain a bridges array")
    relation_names = sorted({edge["relation"] for bridge in bridges for edge in bridge.get("edges", [])})
    unknown = [name for name in relation_names if name not in RELATION_DEFINITIONS]
    if unknown:
        raise BuildError(f"Undefined semantic bridge relations: {unknown!r}")
    normalized = []
    for bridge in bridges:
        record = json.loads(json.dumps(bridge))
        for edge in record["edges"]:
            edge["relation_uri"] = f"{SITE}/ns/relations/{edge['relation']}"
        normalized.append(record)
    return {
        "$schema": SITE + SCHEMAS["bridges"],
        "schema_version": "semantic-bridges.v1",
        "document_id": "ivankotov-public-semantic-bridges-v1",
        "url": f"{SITE}/semantic-bridges.json",
        "last_verified": LAST_VERIFIED,
        "status": source["status"],
        "claim_boundary": source["claim_boundary"],
        "source_sha256": sha256_file(BRIDGES_SOURCE),
        "relation_definitions": [
            {
                "relation": name,
                "relation_uri": f"{SITE}/ns/relations/{name}",
                "definition": RELATION_DEFINITIONS[name],
            }
            for name in relation_names
        ],
        "bridge_count": len(normalized),
        "bridges": normalized,
    }


def build_repositories() -> dict[str, Any]:
    source = read_json(REPOSITORIES_SOURCE)
    repositories = source.get("repositories")
    if not isinstance(repositories, list):
        raise BuildError("public-repositories.json source must contain a repositories array")
    normalized = []
    for record in repositories:
        item = json.loads(json.dumps(record))
        name = item["name"]
        commit = item["observed_head_commit"]
        item["repository_id"] = f"github:{OWNER}/{name}"
        item["repository_url"] = f"https://github.com/{OWNER}/{name}"
        item["observed_commit_url"] = f"https://github.com/{OWNER}/{name}/commit/{commit}"
        item["presence_scope"] = source["presence_scope"]
        normalized.append(item)
    normalized.sort(key=lambda item: item["name"])
    return {
        "$schema": SITE + SCHEMAS["repositories"],
        "schema_version": "public-repositories.v1",
        "document_id": "ivankotov-public-repositories-v1",
        "url": f"{SITE}/public-repositories.json",
        "last_verified": source["last_verified"],
        "owner": source["owner"],
        "scope": source["scope"],
        "claim_boundary": source["claim_boundary"],
        "source_sha256": sha256_file(REPOSITORIES_SOURCE),
        "repository_count": len(normalized),
        "repositories": normalized,
    }


def build_machine_index(works: dict[str, Any], terms: dict[str, Any], bridges: dict[str, Any], repositories: dict[str, Any]) -> dict[str, Any]:
    return {
        "$schema": SITE + SCHEMAS["machine_index"],
        "schema_version": "machine-index.v1",
        "document_id": "ivankotov-machine-entry-v1",
        "url": f"{SITE}/machine-index.json",
        "last_verified": LAST_VERIFIED,
        "human_entry": f"{SITE}/start-here/",
        "author": {"name": "Ivan Kotov", "orcid": "https://orcid.org/0009-0009-6002-9845"},
        "scope": "Discovery and normalization entry point for the public authored corpus and living-corpus projection.",
        "authority_rule": "This index is not the byte authority for DOI-bound, signed, tagged, or separately hashed artifacts. Follow each record's canonical source, release, DOI, manifest, and checksum declarations.",
        "claim_boundary": "Machine readability does not elevate publication into implementation, internal review into independent validation, archive into continuity, replay into resumption, a profile into an entity, or telemetry into subjective experience.",
        "counts": {
            "normalized_works": works["work_count"],
            "terms": terms["term_count"],
            "distinctions": terms["distinction_count"],
            "semantic_bridges": bridges["bridge_count"],
            "public_repositories": repositories["repository_count"],
        },
        "entries": [
            {"role": "normalized_work_index", "url": f"{SITE}/scientific-corpus-index.json", "media_type": "application/json", "schema": SITE + SCHEMAS["works"]},
            {"role": "linked_data_work_index", "url": f"{SITE}/scientific-corpus.jsonld", "media_type": "application/ld+json", "schema": None},
            {"role": "term_registry", "url": f"{SITE}/term-registry.json", "media_type": "application/json", "schema": SITE + SCHEMAS["terms"]},
            {"role": "linked_data_term_registry", "url": f"{SITE}/term-registry.jsonld", "media_type": "application/ld+json", "schema": None},
            {"role": "semantic_bridges", "url": f"{SITE}/semantic-bridges.json", "media_type": "application/json", "schema": SITE + SCHEMAS["bridges"]},
            {"role": "public_repository_inventory", "url": f"{SITE}/public-repositories.json", "media_type": "application/json", "schema": SITE + SCHEMAS["repositories"]},
            {"role": "living_corpus_index", "url": f"{SITE}/corpus-index.json", "media_type": "application/json", "schema": None},
            {"role": "living_corpus_protocol_map", "url": f"{SITE}/corpus-protocol-map.json", "media_type": "application/json", "schema": None},
            {"role": "legacy_work_index", "url": f"{SITE}/works-index.json", "media_type": "application/json", "schema": None},
            {"role": "machine_guide", "url": f"{SITE}/llms.txt", "media_type": "text/plain", "schema": None},
            {"role": "extended_machine_guide", "url": f"{SITE}/llms-full.txt", "media_type": "text/plain", "schema": None},
        ],
    }


def build_outputs() -> dict[Path, str]:
    works, works_jsonld = build_works()
    terms, terms_jsonld = build_terms()
    bridges = build_bridges()
    repositories = build_repositories()
    machine_index = build_machine_index(works, terms, bridges, repositories)
    return {
        OUTPUTS["machine_index"]: json_text(machine_index),
        OUTPUTS["works"]: json_text(works),
        OUTPUTS["works_jsonld"]: json_text(works_jsonld),
        OUTPUTS["terms"]: json_text(terms),
        OUTPUTS["terms_jsonld"]: json_text(terms_jsonld),
        OUTPUTS["bridges"]: json_text(bridges),
        OUTPUTS["repositories"]: json_text(repositories),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail if generated outputs differ from tracked files")
    args = parser.parse_args()
    try:
        outputs = build_outputs()
        changed = []
        for path, text in outputs.items():
            if args.check:
                existing = path.read_text(encoding="utf-8") if path.exists() else None
                if existing != text:
                    changed.append(str(path.relative_to(ROOT)))
            else:
                path.write_text(text, encoding="utf-8", newline="\n")
        if changed:
            print("Generated machine layer is stale:", file=sys.stderr)
            for path in changed:
                print(f"- {path}", file=sys.stderr)
            return 1
        print(f"Machine layer {'verified' if args.check else 'built'}: {len(outputs)} files")
        return 0
    except (BuildError, KeyError, TypeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
