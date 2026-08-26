from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
BUILDER = ROOT / "tools" / "build_beacon_v0_1_site_surfaces.py"
TOKEN = b"__BEACON_AGI_" + b"PUBLICATION_COMMIT__"
MOCK_COMMIT = "1" * 40
COMMIT_RE = re.compile(r"[0-9a-f]{40}\Z")

BUILD_STEPS = (
    "tools/build_beacon_v0_1_site_surfaces.py",
    "tools/build_diary.py",
    "tools/build_corpus.py",
    "tools/build_machine_layer.py",
)


class FinalizationError(RuntimeError):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Bind the Beacon Profile v0.1 website package to the signed AGI "
            "publication commit and regenerate its deterministic site surfaces."
        )
    )
    parser.add_argument(
        "--agi-commit",
        required=True,
        help="Lowercase 40-hex commit of the published AGI Beacon bridge.",
    )
    parser.add_argument(
        "--allow-mock-commit",
        action="store_true",
        help=(
            "Permit the reserved 40-times-'1' commit for offline regression "
            "validation only. It is never accepted by the normal final gate."
        ),
    )
    return parser.parse_args()


def validate_commit(value: str, allow_mock: bool) -> None:
    if not COMMIT_RE.fullmatch(value):
        raise FinalizationError("--agi-commit must be exactly 40 lowercase hexadecimal characters")
    if value == "0" * 40:
        raise FinalizationError("the all-zero commit is not a valid publication binding")
    if value == MOCK_COMMIT and not allow_mock:
        raise FinalizationError(
            "the reserved mock commit requires --allow-mock-commit and cannot be used for final publication"
        )


def token_inventory() -> tuple[int, list[str]]:
    count = 0
    locations: list[str] = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or ".git" in path.parts or "__pycache__" in path.parts:
            continue
        try:
            payload = path.read_bytes()
        except OSError as exc:
            raise FinalizationError(f"cannot read {path.relative_to(ROOT).as_posix()}: {exc}") from exc
        occurrences = payload.count(TOKEN)
        if occurrences:
            relative = path.relative_to(ROOT).as_posix()
            locations.extend([relative] * occurrences)
            count += occurrences
    return count, locations


def atomic_replace_token(commit: str) -> None:
    count, locations = token_inventory()
    expected = BUILDER.relative_to(ROOT).as_posix()
    if count != 1 or locations != [expected]:
        rendered = ", ".join(locations) if locations else "none"
        raise FinalizationError(
            f"expected exactly one publication token in {expected}; found {count} at {rendered}"
        )

    original = BUILDER.read_bytes()
    if original.count(TOKEN) != 1:
        raise FinalizationError("builder token count changed during finalization preflight")
    finalized = original.replace(TOKEN, commit.encode("ascii"), 1)

    # Compile before mutating the source so a malformed replacement cannot be installed.
    compile(finalized.decode("utf-8"), str(BUILDER), "exec")

    mode = BUILDER.stat().st_mode
    temporary_name: str | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb",
            prefix=BUILDER.name + ".",
            suffix=".tmp",
            dir=BUILDER.parent,
            delete=False,
        ) as temporary:
            temporary.write(finalized)
            temporary.flush()
            os.fsync(temporary.fileno())
            temporary_name = temporary.name
        os.chmod(temporary_name, mode)
        os.replace(temporary_name, BUILDER)
        temporary_name = None
    finally:
        if temporary_name is not None:
            Path(temporary_name).unlink(missing_ok=True)


def run(command: list[str]) -> None:
    print("+ " + " ".join(command), flush=True)
    subprocess.run(command, cwd=ROOT, check=True)


def main() -> int:
    args = parse_args()
    validate_commit(args.agi_commit, args.allow_mock_commit)
    atomic_replace_token(args.agi_commit)

    for script in BUILD_STEPS:
        run([sys.executable, script])

    validator = [sys.executable, "tools/validate_beacon_v0_1_site.py"]
    if args.allow_mock_commit:
        validator.append("--allow-mock-commit")
    run(validator)

    if args.agi_commit == MOCK_COMMIT:
        print(
            "PASS Beacon v0.1 site finalizer MOCK_EXTERNAL_LINK_PENDING",
            flush=True,
        )
    else:
        print(
            f"PASS Beacon v0.1 site finalizer bound to AGI commit {args.agi_commit}",
            flush=True,
        )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FinalizationError, OSError, UnicodeError, subprocess.CalledProcessError) as exc:
        print(f"FAIL Beacon v0.1 site finalizer: {exc}", file=sys.stderr)
        raise SystemExit(1)
