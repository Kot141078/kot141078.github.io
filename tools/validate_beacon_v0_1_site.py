from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parent.parent
BUILDER_REL = "tools/build_beacon_v0_1_site_surfaces.py"
BUILDER = ROOT / BUILDER_REL
PUBLICATION_ROOT = ROOT / "publications" / "beacon-profile-v0-1"
FILES_ROOT = PUBLICATION_ROOT / "files"
TOKEN = "__BEACON_AGI_" + "PUBLICATION_COMMIT__"
MOCK_COMMIT = "1" * 40
COMMIT_RE = re.compile(r"[0-9a-f]{40}\Z")
DOI = "10.5281/zenodo.18933553"
DOI_URL = f"https://doi.org/{DOI}"
GUESS_DOI = "10.5281/zenodo." + "18933552"
PAGE_URL = "https://ivankotov.eu/publications/beacon-profile-v0-1/"
ZENODO_URL = "https://zenodo.org/records/18933553"
TITLE = "Beacon Profile v0.1 — Inter-Entity Recognition for Sovereign Digital Entities"
STATUS = (
    "Published DOI-linked informative synthesis profile containing normative-style local requirements. "
    "It is not a standards-track specification, not a certification regime, and not a completed "
    "cryptographic conformance package."
)
IMPLEMENTATION_STATUS = "Structural reference classifier and persistence sidecar."
IMPLEMENTATION_COMMIT = "54cd0c8754587f5e9daf82b16eb84c66a7ac94ef"
IMPLEMENTATION_MODULE_PATH = "modules/beacon_profile/profile.py"
IMPLEMENTATION_TEST_PATH = "tests/test_beacon_profile.py"
IMPLEMENTATION_MODULE_URL = (
    "https://github.com/Kot141078/ester-clean-code/blob/"
    f"{IMPLEMENTATION_COMMIT}/{IMPLEMENTATION_MODULE_PATH}"
)
IMPLEMENTATION_TEST_URL = (
    "https://github.com/Kot141078/ester-clean-code/blob/"
    f"{IMPLEMENTATION_COMMIT}/{IMPLEMENTATION_TEST_PATH}"
)

HISTORICAL_HASHES = {
    "protocols/beacon/Beacon_Profile_v0.1_EN.md":
        "4e5061fc655ce384dcbf75843ff158a10c5e1f39e3c2bdf60e2a85ffed494de1",
    "protocols/beacon/Beacon_Profile_v0.1_EN.pdf":
        "d646934ea8657785741af57e422d9e044a0de407f2f9d5a6089f083a37b6eeb0",
    "protocols/beacon/README.md":
        "9bf3b577e38519b7d25eb7051667e7c7db89b302c2f7ef5a80179593ed99dd26",
}
PUBLICATION_HASHES = {
    "README.md": "ad17fbfda021a1c26558602de57038e7b5510954557cdd45f66dc352d4972a14",
    "PUBLICATION_RECORD.json": "9cc6fc93f6704ac0fef23d8ab4c6eb18f2f2a5652979e92fba4102cc86bc6289",
    "CITATION.cff": "66fa7ab787eef421aa77b2ad94e0e4d7d490a72f488b073a34c0e2ccd7833ebf",
}
SITE_COPY_HASHES = {
    "historical/hashes/SHA256SUMS_beacon_v0.1_2026-03-10.txt":
        "2cbbff8a1948866f05e00faf675b2a818b62b3af21b9ad27ca74935f07a2a3bd",
    **{f"historical/{name}": digest for name, digest in HISTORICAL_HASHES.items()},
    **{f"publication/{name}": digest for name, digest in PUBLICATION_HASHES.items()},
    "publication/SHA256SUMS_PUBLICATION_BRIDGE.txt":
        "06bcdd34be22c9663da866f6ff9b3c57a5ea1d48a95fbea4ad85228870ac59f4",
}

DENIED_IMPLEMENTATION_CAPABILITIES = (
    "payload-hash recomputation",
    "cryptographic signature verification",
    "Ed25519 verification",
    "key resolution",
    "key rotation proof",
    "key revocation proof",
    "witness-reference resolution",
    "challenge execution",
    "independent interoperability",
    "production deployment conformance",
)
SITE_DENIAL_ALTERNATIVES = (
    ("payload-hash recomputation", "recomputation of payload hashes"),
    ("cryptographic signature verification",),
    ("Ed25519 verification",),
    ("key resolution",),
    ("key rotation proof", "key rotation or revocation proof"),
    ("key revocation proof", "key rotation or revocation proof"),
    ("witness-reference resolution",),
    ("challenge execution",),
    ("independent interoperability",),
    ("production deployment conformance",),
)


class ValidationError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate the DOI-safe Beacon Profile v0.1 website publication package."
    )
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument(
        "--prepared",
        action="store_true",
        help="Validate the unfixed source package with exactly one AGI commit placeholder.",
    )
    modes.add_argument(
        "--allow-mock-commit",
        action="store_true",
        help="Validate the reserved offline mock commit; external AGI-link existence remains pending.",
    )
    return parser.parse_args()


def read_text(relative: str) -> str:
    path = ROOT / relative
    require(path.is_file(), f"missing required file: {relative}")
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise ValidationError(f"cannot read UTF-8 file {relative}: {exc}") from exc


def read_json(relative: str) -> Any:
    try:
        return json.loads(read_text(relative))
    except json.JSONDecodeError as exc:
        raise ValidationError(f"invalid JSON in {relative}: {exc}") from exc


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_manifest(path: Path) -> dict[str, str]:
    require(path.is_file(), f"missing checksum manifest: {path.relative_to(ROOT).as_posix()}")
    entries: dict[str, str] = {}
    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw_line:
            continue
        match = re.fullmatch(r"([0-9a-f]{64})  ([^\r\n]+)", raw_line)
        require(match is not None, f"malformed checksum line {line_number} in {path.name}")
        digest, relative = match.groups()
        require("\\" not in relative, f"non-canonical path in {path.name}: {relative}")
        pure = Path(relative)
        require(not pure.is_absolute() and ".." not in pure.parts, f"unsafe path in {path.name}: {relative}")
        require(relative not in entries, f"duplicate path in {path.name}: {relative}")
        entries[relative] = digest
    require(bool(entries), f"empty checksum manifest: {path.name}")
    return entries


def verify_manifest(path: Path, base: Path, expected: dict[str, str]) -> None:
    entries = parse_manifest(path)
    require(entries == expected, f"unexpected entries or digests in {path.relative_to(ROOT).as_posix()}")
    for relative, expected_digest in entries.items():
        target = base / Path(relative)
        require(target.is_file(), f"manifest target missing: {target.relative_to(ROOT).as_posix()}")
        actual = sha256(target)
        require(
            actual == expected_digest,
            f"SHA-256 mismatch for {target.relative_to(ROOT).as_posix()}: {actual}",
        )


def validate_copied_artifacts() -> None:
    historical_manifest = FILES_ROOT / "historical" / "hashes" / "SHA256SUMS_beacon_v0.1_2026-03-10.txt"
    verify_manifest(historical_manifest, FILES_ROOT / "historical", HISTORICAL_HASHES)

    bridge_manifest = FILES_ROOT / "publication" / "SHA256SUMS_PUBLICATION_BRIDGE.txt"
    verify_manifest(bridge_manifest, FILES_ROOT / "publication", PUBLICATION_HASHES)

    site_manifest = FILES_ROOT / "SHA256SUMS_BEACON_SITE_COPIES.txt"
    verify_manifest(site_manifest, FILES_ROOT, SITE_COPY_HASHES)

    attributes = read_text("publications/beacon-profile-v0-1/files/.gitattributes")
    require("historical/** -text" in attributes, "historical copy bytes are not protected with -text")
    require("publication/** -text" in attributes, "publication copy bytes are not protected with -text")


def validate_publication_record() -> dict[str, Any]:
    relative = "publications/beacon-profile-v0-1/files/publication/PUBLICATION_RECORD.json"
    record = read_json(relative)
    require(isinstance(record, dict), f"{relative} must contain a JSON object")
    expected = {
        "published_doi": DOI,
        "doi_url": DOI_URL,
        "doi_role": "unresolved",
        "version_doi": None,
        "concept_doi": None,
        "zenodo_record_url": ZENODO_URL,
        "zenodo_metadata_verified": False,
        "zenodo_file_inventory_verified": False,
        "zenodo_byte_identity_verified": False,
    }
    for key, value in expected.items():
        require(record.get(key) == value, f"publication record {key} must be {value!r}")

    implementation = record.get("implementation_bridge")
    require(isinstance(implementation, dict), "publication record lacks implementation_bridge")
    require(implementation.get("commit") == IMPLEMENTATION_COMMIT, "implementation commit mismatch")
    require(implementation.get("module") == IMPLEMENTATION_MODULE_PATH, "implementation module mismatch")
    require(implementation.get("tests") == IMPLEMENTATION_TEST_PATH, "implementation test path mismatch")
    denied = implementation.get("does_not_demonstrate")
    require(isinstance(denied, list), "implementation does_not_demonstrate must be a list")
    for capability in DENIED_IMPLEMENTATION_CAPABILITIES:
        require(capability in denied, f"publication record does not deny {capability}")
    return record


def validate_cff_route() -> None:
    relative = "publications/beacon-profile-v0-1/files/publication/CITATION.cff"
    text = read_text(relative)
    lines = text.splitlines()
    top_level = [line for line in lines if line and not line.startswith((" ", "#"))]
    require("cff-version: 1.2.0" in top_level, "CFF version must be 1.2.0")
    require("type: dataset" in top_level, "CFF top-level type must be dataset")
    require(not any(line.startswith("doi:") for line in top_level), "CFF top-level DOI is forbidden")
    require(not any(line.startswith("date-released:") for line in top_level), "CFF date-released is forbidden")
    require(not any(line.startswith("license:") for line in top_level), "CFF license is unverified and forbidden")
    require("preferred-citation:" in top_level, "CFF lacks preferred-citation")

    start = lines.index("preferred-citation:") + 1
    preferred = []
    for line in lines[start:]:
        if line and not line.startswith(" "):
            break
        preferred.append(line)
    require("  type: report" in preferred, "preferred-citation type must be report")
    require(f'  doi: "{DOI}"' in preferred, "preferred-citation DOI mismatch")
    require(f'  title: "{TITLE}"' in preferred, "preferred-citation title mismatch")
    require(not any("concept-doi" in line.lower() for line in lines), "CFF must not invent a concept DOI")


def iter_files_without_git() -> Iterable[Path]:
    for path in sorted(ROOT.rglob("*")):
        if path.is_file() and ".git" not in path.parts and "__pycache__" not in path.parts:
            yield path


def byte_occurrences(needle: bytes) -> list[str]:
    locations: list[str] = []
    for path in iter_files_without_git():
        payload = path.read_bytes()
        occurrences = payload.count(needle)
        if occurrences:
            locations.extend([path.relative_to(ROOT).as_posix()] * occurrences)
    return locations


def validate_builder(prepared: bool, allow_mock: bool) -> str:
    source = read_text(BUILDER_REL)
    compile(source, str(BUILDER), "exec")
    token_locations = byte_occurrences(TOKEN.encode("ascii"))
    if prepared:
        require(
            token_locations == [BUILDER_REL],
            f"prepared package must contain exactly one token in {BUILDER_REL}; found {token_locations}",
        )
        commit = TOKEN
    else:
        require(not token_locations, f"finalized package still contains token at {token_locations}")
        match = re.search(r'^AGI_COMMIT\s*=\s*["\']([0-9a-f]{40})["\']\s*$', source, re.MULTILINE)
        require(match is not None, "builder lacks a finalized lowercase 40-hex AGI_COMMIT")
        commit = match.group(1)
        require(commit != "0" * 40, "all-zero AGI commit is forbidden")
        if allow_mock:
            require(commit == MOCK_COMMIT, "--allow-mock-commit requires the reserved 40-times-'1' commit")
        else:
            require(commit != MOCK_COMMIT, "reserved mock commit is forbidden in final validation")

    required_source_fragments = (
        DOI,
        "doi_role",
        "unresolved",
        "version_doi",
        "concept_doi",
        "Published DOI-linked informative synthesis profile containing normative-style local requirements.",
        "It is not a standards-track specification, not a certification regime, and not a completed ",
        "cryptographic conformance package.",
        IMPLEMENTATION_COMMIT,
        IMPLEMENTATION_MODULE_PATH,
        IMPLEMENTATION_TEST_PATH,
        IMPLEMENTATION_STATUS,
        "payload-hash recomputation",
        "cryptographic signature",
        "Ed25519 verification",
        "key resolution",
        "witness-reference resolution",
    )
    for fragment in required_source_fragments:
        require(fragment in source, f"builder lacks required bounded source fragment: {fragment}")
    require(GUESS_DOI not in source, "builder contains the forbidden guessed concept DOI")
    return commit


def all_key_values(value: Any, key: str) -> list[Any]:
    found: list[Any] = []
    if isinstance(value, dict):
        for current_key, current_value in value.items():
            if current_key == key:
                found.append(current_value)
            found.extend(all_key_values(current_value, key))
    elif isinstance(value, list):
        for item in value:
            found.extend(all_key_values(item, key))
    return found


def all_strings(value: Any) -> list[str]:
    found: list[str] = []
    if isinstance(value, str):
        found.append(value)
    elif isinstance(value, dict):
        for key, item in value.items():
            found.append(key)
            found.extend(all_strings(item))
    elif isinstance(value, list):
        for item in value:
            found.extend(all_strings(item))
    return found


def find_record(value: Any, record_id: str) -> dict[str, Any] | None:
    if isinstance(value, dict):
        if value.get("id") == record_id:
            return value
        for child in value.values():
            found = find_record(child, record_id)
            if found is not None:
                return found
    elif isinstance(value, list):
        for child in value:
            found = find_record(child, record_id)
            if found is not None:
                return found
    return None


def require_doi_boundary(record: dict[str, Any], label: str) -> None:
    published = record.get("published_doi")
    if published is None and isinstance(record.get("identifiers"), dict):
        published = record["identifiers"].get("published_doi")
    require(published in {DOI, DOI_URL}, f"{label} published DOI mismatch: {published!r}")

    role = record.get("doi_role")
    if role is None and isinstance(record.get("identifiers"), dict):
        role = record["identifiers"].get("doi_role")
    require(role == "unresolved", f"{label} DOI role must be unresolved")

    for key in ("version_doi", "concept_doi"):
        present = key in record
        value = record.get(key)
        if isinstance(record.get("identifiers"), dict) and key in record["identifiers"]:
            present = True
            value = record["identifiers"].get(key)
        require(present and value is None, f"{label} {key} must be explicit null")


def validate_dedicated_machine(commit: str) -> None:
    relative = "publications/beacon-profile-v0-1/files/machine/index.json"
    machine = read_json(relative)
    require(isinstance(machine, dict), "dedicated machine index must be a JSON object")
    require_doi_boundary(machine, "dedicated machine index")
    serialized = json.dumps(machine, ensure_ascii=False, sort_keys=True)
    for fragment in (
        TITLE,
        DOI,
        STATUS,
        IMPLEMENTATION_STATUS,
        IMPLEMENTATION_COMMIT,
        IMPLEMENTATION_MODULE_PATH,
        IMPLEMENTATION_TEST_PATH,
        commit,
    ):
        require(fragment in serialized, f"dedicated machine index lacks {fragment}")

    denied_lists = all_key_values(machine, "does_not_demonstrate")
    require(denied_lists, "dedicated machine index lacks does_not_demonstrate")
    denied_strings = "\n".join(all_strings(denied_lists))
    for alternatives in SITE_DENIAL_ALTERNATIVES:
        require(
            any(capability in denied_strings for capability in alternatives),
            f"dedicated machine index does not deny {' / '.join(alternatives)}",
        )

    require(
        all(value is False for value in all_key_values(machine, "zenodo_byte_identity_verified"))
        and bool(all_key_values(machine, "zenodo_byte_identity_verified")),
        "dedicated machine index must explicitly keep Zenodo byte identity unverified",
    )
    require(not all_key_values(machine, "datePublished"), "dedicated machine index invents datePublished")
    require(not all_key_values(machine, "license"), "dedicated machine index invents a license")


def validate_schema_org(commit: str) -> None:
    relative = "publications/beacon-profile-v0-1/files/schema.org.jsonld"
    linked = read_json(relative)
    require(isinstance(linked, dict), "dedicated Schema.org document must be a JSON object")
    serialized = json.dumps(linked, ensure_ascii=False, sort_keys=True)
    for fragment in (TITLE, DOI, "unresolved", STATUS, IMPLEMENTATION_STATUS):
        require(fragment in serialized, f"dedicated Schema.org JSON-LD lacks {fragment}")
    require(not all_key_values(linked, "datePublished"), "Schema.org JSON-LD invents datePublished")
    require(not all_key_values(linked, "license"), "Schema.org JSON-LD invents a license")


def validate_page(commit: str) -> None:
    relative = "publications/beacon-profile-v0-1/index.html"
    page = read_text(relative)
    immutable_root = (
        "https://github.com/Kot141078/advanced-global-intelligence/tree/"
        f"{commit}/protocols/beacon"
    )
    required = (
        TITLE,
        DOI,
        DOI_URL,
        ZENODO_URL,
        "DOI role",
        "unresolved",
        STATUS,
        IMPLEMENTATION_STATUS,
        IMPLEMENTATION_MODULE_URL,
        IMPLEMENTATION_TEST_URL,
        immutable_root,
        "files/historical/protocols/beacon/Beacon_Profile_v0.1_EN.md",
        "files/historical/protocols/beacon/Beacon_Profile_v0.1_EN.pdf",
        "files/historical/hashes/SHA256SUMS_beacon_v0.1_2026-03-10.txt",
        "files/publication/PUBLICATION_RECORD.json",
        "files/publication/CITATION.cff",
        "files/publication/SHA256SUMS_PUBLICATION_BRIDGE.txt",
        "files/machine/index.json",
        "files/schema.org.jsonld",
        "Beacon",
        "VXCX",
        "L4 Witness",
        "authority",
    )
    for fragment in required:
        require(fragment in page, f"publication page lacks {fragment}")
    for alternatives in SITE_DENIAL_ALTERNATIVES:
        require(
            any(capability in page for capability in alternatives),
            f"publication page does not deny {' / '.join(alternatives)}",
        )
    require("datePublished" not in page, "publication page invents datePublished")
    require(GUESS_DOI not in page, "publication page contains guessed concept DOI")


def validate_routing(commit: str) -> None:
    works = read_json("works-index.json")
    work = find_record(works, "beacon-profile-v0-1")
    require(work is not None, "works-index.json lacks Beacon record")
    require_doi_boundary(work, "works-index Beacon record")
    require("date" not in work, "works-index Beacon record must not map document date to datePublished")
    require("license" not in work, "works-index Beacon record invents a license")
    require(work.get("status") == STATUS, "works-index Beacon status ceiling mismatch")
    require(work.get("commit") == commit, "works-index Beacon AGI commit mismatch")

    library = read_json("library-index.json")
    library_record = find_record(library, "beacon-profile-v0-1")
    require(library_record is not None, "library-index.json lacks Beacon record")
    require_doi_boundary(library_record, "library-index Beacon record")
    require(library_record.get("status") == STATUS, "library-index Beacon status ceiling mismatch")
    require(commit in json.dumps(library_record, ensure_ascii=False), "library-index Beacon commit missing")

    canonical = read_json("canonical-map.json")
    canonical_record = find_record(canonical, "beacon-profile-v0-1")
    require(canonical_record is not None, "canonical-map.json lacks Beacon node")
    require_doi_boundary(canonical_record, "canonical-map Beacon node")
    require(canonical_record.get("status") == STATUS, "canonical-map Beacon status ceiling mismatch")
    require(canonical.get("beacon_profile_v0_1_url") == PAGE_URL, "canonical-map Beacon route mismatch")

    downloads = read_json("downloads-index.json")
    download_text = json.dumps(downloads, ensure_ascii=False)
    for fragment in (PAGE_URL, DOI, "PUBLICATION_RECORD.json", "Beacon_Profile_v0.1_EN.md", "Beacon_Profile_v0.1_EN.pdf"):
        require(fragment in download_text, f"downloads-index.json lacks {fragment}")

    scientific = read_json("scientific-corpus-index.json")
    scientific_record = find_record(scientific, "beacon-profile-v0-1")
    require(scientific_record is not None, "scientific-corpus-index.json lacks Beacon record")
    require_doi_boundary(scientific_record, "scientific corpus Beacon record")
    require("datePublished" not in scientific_record, "scientific corpus invents Beacon datePublished")
    require("license" not in scientific_record, "scientific corpus invents a Beacon license")

    machine_index = read_json("machine-index.json")
    works_list = scientific.get("works")
    require(isinstance(works_list, list), "scientific-corpus-index.json works must be a list")
    work_count = scientific.get("work_count")
    require(work_count == len(works_list), "scientific corpus work_count does not match works length")
    counts = machine_index.get("counts")
    require(isinstance(counts, dict), "machine-index.json lacks counts")
    require(
        counts.get("normalized_works") == work_count,
        "machine-index normalized_works count does not bind to the scientific corpus",
    )
    entries_text = json.dumps(machine_index.get("entries"), ensure_ascii=False)
    require(
        "https://ivankotov.eu/scientific-corpus-index.json" in entries_text,
        "machine-index.json does not route to the scientific corpus index",
    )

    scientific_ld = read_text("scientific-corpus.jsonld")
    require(PAGE_URL in scientific_ld and DOI in scientific_ld, "scientific-corpus.jsonld lacks Beacon route or DOI")
    require("datePublished" not in json.dumps(scientific_record), "Beacon scientific record has datePublished")

    for relative in ("publications/index.html", "library/index.html", "downloads/index.html"):
        text = read_text(relative)
        require(PAGE_URL in text or "./beacon-profile-v0-1/" in text or "../publications/beacon-profile-v0-1/" in text, f"{relative} lacks Beacon route")
        require(DOI in text, f"{relative} lacks published DOI")
        require(STATUS in text, f"{relative} lacks exact status ceiling")

    for relative in ("llms.txt", "llms-full.txt"):
        text = read_text(relative)
        for fragment in (PAGE_URL, DOI, "PUBLICATION_RECORD.json", "SHA256SUMS_beacon_v0.1_2026-03-10.txt", IMPLEMENTATION_COMMIT):
            require(fragment in text, f"{relative} lacks {fragment}")
        require(IMPLEMENTATION_STATUS in text, f"{relative} lacks implementation claim ceiling")

    sitemap = read_text("sitemap.xml")
    require(sitemap.count(f"<loc>{PAGE_URL}</loc>") == 1, "sitemap must contain exactly one Beacon page route")


def validate_diary() -> None:
    source_rel = "content/diary/2026-03-15-beacon-profile-v0-1-why-ai-entities-need-recognition-not-just-identity.md"
    output_rel = "diary/beacon-profile-v0-1-why-ai-entities-need-recognition-not-just-identity/index.html"
    for relative in (source_rel, output_rel):
        text = read_text(relative)
        for fragment in (
            "https://lnkd.in/ekW6tsax",
            PAGE_URL,
            DOI,
            "Beacon_Profile_v0.1_EN.md",
            "Beacon_Profile_v0.1_EN.pdf",
            "SHA256SUMS_beacon_v0.1_2026-03-10.txt",
            "PUBLICATION_RECORD.json",
        ):
            require(fragment in text, f"{relative} lacks {fragment}")


def validate_forbidden_scope(prepared: bool) -> None:
    paths = [BUILDER]
    if PUBLICATION_ROOT.is_dir():
        paths.extend(path for path in PUBLICATION_ROOT.rglob("*") if path.is_file())
    if not prepared:
        paths.extend(
            ROOT / relative
            for relative in (
                "works-index.json",
                "library-index.json",
                "downloads-index.json",
                "canonical-map.json",
                "scientific-corpus-index.json",
                "scientific-corpus.jsonld",
                "machine-index.json",
                "llms.txt",
                "llms-full.txt",
                "content/diary/2026-03-15-beacon-profile-v0-1-why-ai-entities-need-recognition-not-just-identity.md",
            )
        )
    seen: set[Path] = set()
    role_pattern = re.compile(
        rf"(?i)(?:version|concept)[ _-]*doi(?:[\"']?\s*[:=]|\s+is|\s+as)\s*[\"']*(?:https://doi\.org/)?{re.escape(DOI)}"
    )
    for path in paths:
        if path in seen or not path.is_file():
            continue
        seen.add(path)
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        relative = path.relative_to(ROOT).as_posix()
        require(GUESS_DOI not in text, f"forbidden guessed DOI in {relative}")
        require("Beacon Profile v0.2" not in text, f"forbidden Beacon v0.2 material in {relative}")
        require(role_pattern.search(text) is None, f"published DOI falsely assigned a version/concept role in {relative}")


def validate_final_surfaces(commit: str) -> None:
    require(COMMIT_RE.fullmatch(commit) is not None, "invalid finalized AGI commit")
    validate_page(commit)
    validate_dedicated_machine(commit)
    validate_schema_org(commit)
    validate_routing(commit)
    validate_diary()


def main() -> int:
    args = parse_args()
    validate_copied_artifacts()
    validate_publication_record()
    validate_cff_route()
    commit = validate_builder(args.prepared, args.allow_mock_commit)
    validate_forbidden_scope(args.prepared)

    if args.prepared:
        for relative in (
            "publications/beacon-profile-v0-1/index.html",
            "publications/beacon-profile-v0-1/files/machine/index.json",
            "publications/beacon-profile-v0-1/files/schema.org.jsonld",
        ):
            require(not (ROOT / relative).exists(), f"prepared package contains stale generated surface: {relative}")
        require(not byte_occurrences(MOCK_COMMIT.encode("ascii")), "prepared package contains reserved mock commit")
        print("PASS Beacon v0.1 site validator PREPARED", flush=True)
        return 0

    validate_final_surfaces(commit)
    if args.allow_mock_commit:
        print("PASS Beacon v0.1 site validator MOCK_EXTERNAL_LINK_PENDING", flush=True)
    else:
        print("PASS Beacon v0.1 site validator PASS", flush=True)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValidationError, OSError, UnicodeError) as exc:
        print(f"FAIL Beacon v0.1 site validator: {exc}", file=sys.stderr)
        raise SystemExit(1)
