from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

VERSION_DOI = "10.5281/zenodo.22402601"
VERSION_DOI_URL = f"https://doi.org/{VERSION_DOI}"
CONCEPT_DOI = "10.5281/zenodo.22402600"
CONCEPT_DOI_URL = f"https://doi.org/{CONCEPT_DOI}"
ZENODO_RECORD = "https://zenodo.org/records/22402601"
ACCEPTANCE_COMMIT = "d170b0e8cd09a590a1826cf907125bd5cdc4dc1d"
ACCEPTANCE_URL = (
    "https://github.com/Kot141078/advanced-global-intelligence/commit/"
    + ACCEPTANCE_COMMIT
)
PACKAGE_SHA256 = "ca1e741f7d4f2dbf76a4a66fed7a5d83cf37e599e0fc4552bbca5aaa59b4ffde"

PAGE = ROOT / "publications" / "scientific-corrections-v1-0" / "index.html"
PUBLICATIONS_INDEX = ROOT / "publications" / "index.html"
WORKS_INDEX = ROOT / "works-index.json"
LLM_FILES = [ROOT / "llms.txt", ROOT / "llms-full.txt"]
PARENT_PAGES = [
    ROOT / "publications" / "motivational-formation-c-v0-1" / "index.html",
    ROOT / "publications" / "ccalc-full-stack-v0-1" / "index.html",
    ROOT / "publications" / "origin-neutral-recognition-provisional-care-v0-1" / "index.html",
]
RECEIPT = ROOT / "evidence" / "scientific-corrections-20260905" / "DOI_BACKFILL_RECEIPT.json"


def replace_once(path: Path, old: str, new: str, *, already: str | None = None) -> bool:
    text = path.read_text(encoding="utf-8")
    if already and already in text:
        return False
    count = text.count(old)
    if count != 1:
        raise RuntimeError(
            f"{path.relative_to(ROOT)} expected exactly one old fragment; found {count}"
        )
    path.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")
    return True


def update_correction_page() -> None:
    text = PAGE.read_text(encoding="utf-8")

    citation_doi = f'<meta name="citation_doi" content="{VERSION_DOI}">'
    if citation_doi not in text:
        anchor = '<meta name="citation_publication_date" content="2026-09-05">'
        if text.count(anchor) != 1:
            raise RuntimeError("citation publication-date anchor drift")
        text = text.replace(
            anchor,
            anchor
            + "\n"
            + citation_doi
            + '\n<meta name="citation_publisher" content="Zenodo">',
            1,
        )

    old_json = (
        '"datePublished": "2026-09-05", "version": "1.0", '
        '"inLanguage": ["en", "ru"]'
    )
    new_json = (
        '"datePublished": "2026-09-05", "version": "1.0", '
        f'"identifier": "{VERSION_DOI_URL}", '
        f'"sameAs": ["{VERSION_DOI_URL}", "{ZENODO_RECORD}"], '
        '"publisher": {"@type": "Organization", "name": "Zenodo"}, '
        '"inLanguage": ["en", "ru"]'
    )
    if new_json not in text:
        if text.count(old_json) != 1:
            raise RuntimeError("schema.org identity anchor drift")
        text = text.replace(old_json, new_json, 1)

    old_json_description = (
        '"description": "Author-issued scientific correction supplement with four '
        'corrected reading editions, source-bound patches and focused first-party '
        'regression tests. No DOI for this supplement is assigned yet."'
    )
    new_json_description = (
        '"description": "Author-issued scientific correction supplement with four '
        'corrected reading editions, source-bound patches and focused first-party '
        f'regression tests. Version DOI: {VERSION_DOI}; all-versions DOI: {CONCEPT_DOI}."'
    )
    if new_json_description not in text:
        if text.count(old_json_description) != 1:
            raise RuntimeError("schema.org description anchor drift")
        text = text.replace(old_json_description, new_json_description, 1)

    old_status = (
        "<p><strong>The earlier DOI files and release identifiers remain unchanged.</strong> "
        "This is not a complete new version of either parent compound package. "
        "A Zenodo DOI for this correction supplement has not yet been assigned.</p>"
    )
    new_status = (
        "<p><strong>The earlier DOI files and release identifiers remain unchanged.</strong> "
        "This is not a complete new version of either parent compound package. "
        f'This correction supplement is published on Zenodo as version DOI '
        f'<a href="{VERSION_DOI_URL}">{VERSION_DOI}</a>; '
        f'all-versions DOI <a href="{CONCEPT_DOI_URL}">{CONCEPT_DOI}</a>.</p>'
    )
    if new_status not in text:
        if text.count(old_status) != 1:
            raise RuntimeError("visible DOI status anchor drift")
        text = text.replace(old_status, new_status, 1)

    citation_line = (
        f'<p><strong>Citation:</strong> Ivan Kotov, <em>Scientific Corrigenda and '
        f'Regression Hardening for ARQ M2, MOT-c and C-Calculus</em>, version 1.0. '
        f'<a href="{VERSION_DOI_URL}">DOI {VERSION_DOI}</a> · '
        f'<a href="{ZENODO_RECORD}">Zenodo record</a>.</p>'
    )
    author_line = (
        '<p><strong>Author:</strong> Ivan Kotov · '
        '<a href="https://orcid.org/0009-0009-6002-9845">'
        "ORCID 0009-0009-6002-9845</a>. New explanatory text: CC BY 4.0; "
        "new maintenance code: MIT; reproduced sources retain their original attribution "
        "and licenses.</p>"
    )
    if citation_line not in text:
        if text.count(author_line) != 1:
            raise RuntimeError("author citation anchor drift")
        text = text.replace(author_line, author_line + "\n" + citation_line, 1)

    old_repo_links = (
        '<p><a href="https://github.com/Kot141078/advanced-global-intelligence/tree/'
        '78bce9419de6006a21fdfd8fcf1aee35c383205c/hardening/scientific_corrigenda_v1_0">'
        "Commit-pinned public repository package</a> · "
        '<a href="https://github.com/Kot141078/sovereign-entity-recursion/blob/'
        '5132db5c3119fe070182e9e975600304e60f7f4c/protocol/arq/corrections/20260905/README.md">'
        "SER-owned ARQ correction notice</a></p>"
    )
    new_repo_links = (
        '<p><a href="https://github.com/Kot141078/advanced-global-intelligence/tree/'
        '78bce9419de6006a21fdfd8fcf1aee35c383205c/hardening/scientific_corrigenda_v1_0">'
        "Commit-pinned public repository package</a> · "
        f'<a href="{ACCEPTANCE_URL}">GPG-verified acceptance commit</a> · '
        '<a href="https://github.com/Kot141078/sovereign-entity-recursion/blob/'
        '5132db5c3119fe070182e9e975600304e60f7f4c/protocol/arq/corrections/20260905/README.md">'
        "SER-owned ARQ correction notice</a></p>"
    )
    if new_repo_links not in text:
        if text.count(old_repo_links) != 1:
            raise RuntimeError("repository link anchor drift")
        text = text.replace(old_repo_links, new_repo_links, 1)

    old_ru = "Новый DOI дополнения пока не назначен."
    new_ru = (
        f'DOI дополнения: <a href="{VERSION_DOI_URL}">{VERSION_DOI}</a>; '
        f'общий DOI всех версий: <a href="{CONCEPT_DOI_URL}">{CONCEPT_DOI}</a>.'
    )
    if new_ru not in text:
        if text.count(old_ru) != 1:
            raise RuntimeError("Russian DOI status anchor drift")
        text = text.replace(old_ru, new_ru, 1)

    PAGE.write_text(text, encoding="utf-8", newline="\n")


def update_publications_index() -> None:
    old = (
        '<!-- SCIENTIFIC-CORRECTION-20260905 -->\n'
        '<section class="section" aria-label="Scientific correction"><div class="prose">'
        '<h2>Scientific correction · 5 September 2026</h2>'
        '<p>A source-bound corrigendum and regression-hardening supplement is available '
        'for ARQ M2, MOT-c and C-Calculus.</p>'
        '<p><a href="/publications/scientific-corrections-v1-0/">'
        'Read the corrigendum and full corrected editions</a>. '
        'Historical DOI files and citation metadata remain unchanged.</p></div></section>'
    )
    new = (
        '<!-- SCIENTIFIC-CORRECTION-20260905 -->\n'
        '<section class="section" aria-label="Scientific correction"><div class="prose">'
        '<h2>Scientific correction · 5 September 2026</h2>'
        '<p>A source-bound corrigendum and regression-hardening supplement is available '
        'for ARQ M2, MOT-c and C-Calculus.</p>'
        '<p><a href="/publications/scientific-corrections-v1-0/">'
        'Read the corrigendum and full corrected editions</a> · '
        f'<a href="{VERSION_DOI_URL}">DOI {VERSION_DOI}</a> · '
        f'<a href="{ZENODO_RECORD}">Zenodo</a>. '
        'Historical parent DOI files and citation metadata remain unchanged.</p>'
        '</div></section>'
    )
    replace_once(PUBLICATIONS_INDEX, old, new, already=f"DOI {VERSION_DOI}")


def update_parent_notices() -> None:
    old_tail = (
        '<a href="/publications/scientific-corrections-v1-0/">'
        "Read the corrigendum and full corrected editions</a>. "
        "Historical DOI files and citation metadata remain unchanged.</p>"
    )
    new_tail = (
        '<a href="/publications/scientific-corrections-v1-0/">'
        "Read the corrigendum and full corrected editions</a>. "
        "Historical DOI files and citation metadata remain unchanged. "
        f'Correction DOI: <a href="{VERSION_DOI_URL}">{VERSION_DOI}</a>.</p>'
    )
    for path in PARENT_PAGES:
        replace_once(path, old_tail, new_tail, already=f"Correction DOI: <a href=\"{VERSION_DOI_URL}\"")


def update_works_index() -> None:
    data = json.loads(WORKS_INDEX.read_text(encoding="utf-8"))
    works = data.get("works")
    if not isinstance(works, list):
        raise RuntimeError("works-index.json has no works array")
    matches = [item for item in works if item.get("id") == "scientific-corrections-v1-0"]
    if len(matches) != 1:
        raise RuntimeError(f"expected one corrigenda work record, found {len(matches)}")
    work = matches[0]

    work["doi"] = VERSION_DOI
    work["doi_url"] = VERSION_DOI_URL
    work["version_doi"] = VERSION_DOI
    work["concept_doi"] = CONCEPT_DOI
    work["concept_doi_url"] = CONCEPT_DOI_URL
    work["zenodo_record"] = ZENODO_RECORD
    work["doi_role"] = "version"
    work["resource_type"] = "Technical note"
    work["status"] = "published_scientific_corrigendum_with_zenodo_doi"
    work["acceptance_commit"] = ACCEPTANCE_COMMIT
    work["acceptance_commit_url"] = ACCEPTANCE_URL

    claims = work.get("non_claims")
    if not isinstance(claims, list):
        raise RuntimeError("corrigenda work record has no non_claims list")
    claims = [item for item in claims if item != "no new DOI assigned yet"]
    replacement = "the correction DOI does not replace or rewrite parent DOI payloads"
    if replacement not in claims:
        claims.insert(1, replacement)
    work["non_claims"] = claims

    WORKS_INDEX.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def update_llm_guides() -> None:
    old = (
        "- https://ivankotov.eu/publications/scientific-corrections-v1-0/\n"
        "Source-bound ARQ M2, MOT-c and C-Calculus corrigendum, corrected reading editions "
        "and regression checks. Historical DOI payloads retained; the correction supplement "
        "has no DOI assigned yet."
    )
    new = (
        "- Human page: https://ivankotov.eu/publications/scientific-corrections-v1-0/\n"
        f"- Version DOI: {VERSION_DOI_URL}\n"
        f"- All-versions DOI: {CONCEPT_DOI_URL}\n"
        f"- Zenodo: {ZENODO_RECORD}\n"
        "- Source-bound ARQ M2, MOT-c and C-Calculus corrigendum, corrected reading editions "
        "and regression checks. Historical parent DOI payloads remain unchanged."
    )
    for path in LLM_FILES:
        replace_once(path, old, new, already=f"- Version DOI: {VERSION_DOI_URL}")


def write_receipt() -> None:
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema": "scientific-corrigenda-doi-backfill-v1",
        "status": "DOI_BACKFILL_APPLIED_AWAITING_CI_AND_LIVE_VERIFICATION",
        "date": "2026-09-05",
        "version_doi": VERSION_DOI,
        "concept_doi": CONCEPT_DOI,
        "zenodo_record": ZENODO_RECORD,
        "package_sha256_unchanged": PACKAGE_SHA256,
        "acceptance_commit": ACCEPTANCE_COMMIT,
        "changed_classes": [
            "canonical publication page metadata and citation surface",
            "publications index",
            "parent correction notices",
            "legacy works index",
            "LLM discovery guides",
        ],
        "generated_machine_outputs": [
            "scientific-corpus-index.json",
            "scientific-corpus.jsonld",
        ],
        "boundary": (
            "No scientific package bytes, parent DOI payloads, corrected PDFs/Markdown, "
            "source snapshots, regression fixtures, or archive hashes are changed by this backfill."
        ),
    }
    RECEIPT.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def main() -> int:
    update_correction_page()
    update_publications_index()
    update_parent_notices()
    update_works_index()
    update_llm_guides()
    write_receipt()

    page = PAGE.read_text(encoding="utf-8")
    works = json.loads(WORKS_INDEX.read_text(encoding="utf-8"))["works"]
    work = next(item for item in works if item["id"] == "scientific-corrections-v1-0")
    required = [
        citation for citation in (VERSION_DOI, CONCEPT_DOI, ZENODO_RECORD)
        if citation not in page
    ]
    if required:
        raise RuntimeError(f"publication page missing DOI bindings: {required}")
    if work.get("version_doi") != VERSION_DOI or work.get("concept_doi") != CONCEPT_DOI:
        raise RuntimeError("works-index DOI binding failed")
    print(
        "PASS DOI backfill source surfaces: "
        f"version DOI {VERSION_DOI}, concept DOI {CONCEPT_DOI}; package bytes unchanged"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
