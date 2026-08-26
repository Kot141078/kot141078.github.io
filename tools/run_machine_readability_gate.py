from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

PYTHON_STEPS = (
    "tools/build_beacon_v0_1_site_surfaces.py",
    "tools/build_diary.py",
    "tools/build_corpus.py",
    "tools/build_machine_layer.py",
    "tools/check_machine_readability.py",
    "tools/validate_search_indexability.py",
    "tools/check_tap_surface.py",
)

SCHEMA_DOCUMENT_PAIRS = (
    ("schemas/machine-index-v1.schema.json", "machine-index.json"),
    ("schemas/scientific-corpus-index-v1.schema.json", "scientific-corpus-index.json"),
    ("schemas/term-registry-v1.schema.json", "term-registry.json"),
    ("schemas/semantic-bridges-v1.schema.json", "semantic-bridges.json"),
    ("schemas/public-repositories-v1.schema.json", "public-repositories.json"),
)

BEACON_VALIDATOR = "tools/validate_beacon_v0_1_site.py"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the complete machine-readability gate.")
    parser.add_argument(
        "--allow-beacon-mock",
        action="store_true",
        help=(
            "Permit the reserved Beacon AGI mock commit for offline package validation. "
            "The normal gate rejects it."
        ),
    )
    return parser.parse_args()


def run(command: list[str]) -> None:
    print("+ " + " ".join(command), flush=True)
    subprocess.run(command, cwd=ROOT, check=True)


def find_npm() -> str:
    npm = shutil.which("npm") or shutil.which("npm.cmd")
    if npm is None:
        raise RuntimeError("npm is required for JSON Schema validation")
    return npm


def main() -> int:
    args = parse_args()
    for script in PYTHON_STEPS:
        run([sys.executable, script])

    beacon_validation = [sys.executable, BEACON_VALIDATOR]
    if args.allow_beacon_mock:
        beacon_validation.append("--allow-mock-commit")
    run(beacon_validation)

    npm = find_npm()
    for schema, document in SCHEMA_DOCUMENT_PAIRS:
        run(
            [
                npm,
                "exec",
                "--yes",
                "--package=ajv-cli@5.0.0",
                "--package=ajv-formats@3.0.1",
                "--",
                "ajv",
                "validate",
                "--spec=draft2020",
                "-c",
                "ajv-formats",
                "-s",
                schema,
                "-d",
                document,
            ]
        )

    run(["git", "diff", "--check"])
    print(
        f"PASS full machine-readability gate "
        f"({len(PYTHON_STEPS) + 1} Python steps, {len(SCHEMA_DOCUMENT_PAIRS)} schema contracts)",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, RuntimeError, subprocess.CalledProcessError) as exc:
        print(f"FAIL full machine-readability gate: {exc}", file=sys.stderr)
        raise SystemExit(1)
