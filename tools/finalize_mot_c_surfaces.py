from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUBLICATION_ID = "motivational-formation-c-v0-1"
PAGE_URL = "https://ivankotov.eu/publications/motivational-formation-c-v0-1/"
DOI = "https://doi.org/10.5281/zenodo.22060517"
CONCEPT_DOI = "https://doi.org/10.5281/zenodo.22060516"
REPO = "https://github.com/Kot141078/advanced-global-intelligence"
TAG = "mot-c-v0.1"
SOURCE_COMMIT = "35fa9007f61836aed686c0f62404e1ae47301939"
LIVE_SOURCE = f"{REPO}/tree/main/publications/{PUBLICATION_ID}"
TAG_SOURCE = f"{REPO}/tree/{TAG}/publications/{PUBLICATION_ID}"
COMMIT_SOURCE = f"{REPO}/tree/{SOURCE_COMMIT}/publications/{PUBLICATION_ID}"
RELEASE_URL = f"{REPO}/releases/tag/{TAG}"

TITLE = "Motivational Formation, Reflective Endorsement, and Motivational Custody in c-Class Digital Entities: Foundation Theory"
ABSTRACT = (
    "Foundation theory distinguishing reward, preference, task, mandate, goal, motive, obligation, "
    "and authority in continuity-bearing c-class digital entities. It defines motivational formation, "
    "reflective endorsement, motivational custody, cognitive time, resource dependence, model-replacement "
    "and fork/replay boundaries, while explicitly making no consciousness, personhood, free-will, "
    "universal-motive, or automatic-authority claim."
)


def read_json(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def write_json(path: str, value: dict) -> None:
    (ROOT / path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def replace_text(path: str, old: str, new: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    if old in text:
        target.write_text(text.replace(old, new), encoding="utf-8", newline="\n")


def upsert_block(path: str, begin: str, end: str, block: str, before: str = "</head>") -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    wrapped = f"{begin}\n{block.rstrip()}\n{end}"
    if begin in text and end in text:
        left, tail = text.split(begin, 1)
        _, right = tail.split(end, 1)
        text = left + wrapped + right
    else:
        if before not in text:
            raise RuntimeError(f"Insertion anchor {before!r} not found in {path}")
        text = text.replace(before, wrapped + "\n" + before, 1)
    target.write_text(text, encoding="utf-8", newline="\n")


def publication_node() -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "TechArticle",
        "@id": PAGE_URL + "#work",
        "url": PAGE_URL,
        "name": TITLE,
        "headline": "Motivational Formation, Reflective Endorsement, and Motivational Custody in c-Class Digital Entities",
        "abstract": ABSTRACT,
        "author": {
            "@type": "Person",
            "name": "Ivan Kotov",
            "identifier": "https://orcid.org/0009-0009-6002-9845",
            "sameAs": "https://orcid.org/0009-0009-6002-9845",
        },
        "datePublished": "2026-08-22",
        "version": "0.1",
        "inLanguage": ["en", "ru"],
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "identifier": [
            {"@type": "PropertyValue", "propertyID": "DOI", "value": "10.5281/zenodo.22060517", "url": DOI},
            {"@type": "PropertyValue", "propertyID": "Concept DOI", "value": "10.5281/zenodo.22060516", "url": CONCEPT_DOI},
        ],
        "sameAs": [DOI, CONCEPT_DOI, TAG_SOURCE, COMMIT_SOURCE, RELEASE_URL],
        "isPartOf": {
            "@type": "CreativeWorkSeries",
            "name": "Project Ester / Advanced Global Intelligence corpus",
            "url": "https://ivankotov.eu/advanced-global-intelligence/",
        },
    }


def update_indexes() -> None:
    works = read_json("works-index.json")
    record = next(item for item in works["works"] if item.get("id") == PUBLICATION_ID)
    record["github"] = TAG_SOURCE
    record["github_living_mirror"] = LIVE_SOURCE
    record["commit"] = SOURCE_COMMIT
    record["commit_url"] = COMMIT_SOURCE
    record["repository_path"] = f"publications/{PUBLICATION_ID}"
    write_json("works-index.json", works)

    library = read_json("library-index.json")
    item = next(item for item in library["items"] if item.get("id") == PUBLICATION_ID)
    item["source_url"] = TAG_SOURCE
    item["living_source_url"] = LIVE_SOURCE
    item["commit_url"] = COMMIT_SOURCE
    write_json("library-index.json", library)

    downloads = read_json("downloads-index.json")
    for item in downloads["items"]:
        if item.get("publication_id") == PUBLICATION_ID and item.get("surface") == "GitHub corpus entry":
            item["url"] = TAG_SOURCE
            item["commit_url"] = COMMIT_SOURCE
            item["note"] = "Tag-pinned readable corpus mirror; Zenodo remains the immutable publication authority."
    write_json("downloads-index.json", downloads)

    machine = read_json(f"publications/{PUBLICATION_ID}/files/machine/index.json")
    machine["github_corpus_entry"] = TAG_SOURCE
    machine["github_living_mirror"] = LIVE_SOURCE
    machine["github_release"] = RELEASE_URL
    machine["source_tag"] = TAG
    machine["source_commit"] = SOURCE_COMMIT
    machine["source_commit_url"] = COMMIT_SOURCE
    write_json(f"publications/{PUBLICATION_ID}/files/machine/index.json", machine)

    linked = read_json(f"publications/{PUBLICATION_ID}/files/schema.org.jsonld")
    linked["sameAs"] = [DOI, CONCEPT_DOI, TAG_SOURCE, COMMIT_SOURCE, RELEASE_URL]
    linked["codeRepository"] = REPO
    linked["isBasedOn"] = DOI
    write_json(f"publications/{PUBLICATION_ID}/files/schema.org.jsonld", linked)


def update_human_surfaces() -> None:
    paths = [
        f"publications/{PUBLICATION_ID}/index.html",
        "llms.txt",
        "llms-full.txt",
        "README.md",
    ]
    for path in paths:
        replace_text(path, LIVE_SOURCE, TAG_SOURCE)

    block = "  <script type=\"application/ld+json\" id=\"mot-c-listing-linked-data\">\n" + json.dumps(publication_node(), ensure_ascii=False, indent=2) + "\n  </script>"
    for path in ["index.html", "publications/index.html", "library/index.html", "downloads/index.html"]:
        upsert_block(path, "<!-- MOT-C-LISTING-LD:BEGIN -->", "<!-- MOT-C-LISTING-LD:END -->", block)


def main() -> None:
    update_indexes()
    update_human_surfaces()
    print("MOT-c stable-source and structured-discovery surfaces finalized.")


if __name__ == "__main__":
    main()
