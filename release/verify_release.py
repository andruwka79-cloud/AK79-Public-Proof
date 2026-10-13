"""Release verifier. Uses explicit checks, not assert, so it cannot be disabled by python -O."""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RELEASE_DIR = Path(__file__).resolve().parent
MANIFEST = RELEASE_DIR / "RELEASE_MANIFEST.json"
SUMS = ROOT / "SHA256SUMS"
SELF_REFERENCED = {"release/RELEASE_MANIFEST.json", "SHA256SUMS"}
EXPECTED_VERSION = "1.0.1"
SKIP_DIRS = {".git", "__pycache__"}


def fail(code: str) -> None:
    print(f"AK79_PUBLIC_PROOF_V1_VERIFY_FAIL:{code}")
    sys.exit(1)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def repo_files():
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or SKIP_DIRS & set(path.relative_to(ROOT).parts):
            continue
        yield path.relative_to(ROOT).as_posix()


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if manifest.get("release") != "AK79 Public Proof v1":
        fail("release_name")
    if manifest.get("version") != EXPECTED_VERSION:
        fail("version")

    listed = {item["path"]: item["sha256"] for item in manifest["files"]}
    for rel, digest in listed.items():
        path = ROOT / rel
        if not path.is_file():
            fail(f"missing:{rel}")
        if sha256(path) != digest:
            fail(f"hash_mismatch:{rel}")

    # Completeness: every file in the repository is either listed in the manifest or self-referenced.
    for rel in repo_files():
        if rel not in listed and rel not in SELF_REFERENCED:
            fail(f"unlisted_file:{rel}")

    # SHA256SUMS must agree with the files on disk and cover every file except itself.
    sums = {}
    for line in SUMS.read_text(encoding="utf-8").splitlines():
        digest, _, rel = line.partition("  ")
        sums[rel] = digest
    for rel in repo_files():
        if rel == "SHA256SUMS":
            continue
        if rel not in sums:
            fail(f"sums_missing:{rel}")
        if sha256(ROOT / rel) != sums[rel]:
            fail(f"sums_mismatch:{rel}")
    for rel in sums:
        if not (ROOT / rel).is_file():
            fail(f"sums_orphan:{rel}")

    json.loads((ROOT / "benchmark/visible_vectors.json").read_text(encoding="utf-8"))
    results = json.loads((ROOT / "results/public_results_v1.json").read_text(encoding="utf-8"))
    if results["external_certification"] is not False or results["production_claim"] is not False:
        fail("results_claims")
    if results["boundaries"]["final_hidden_holdout_published"] is not False:
        fail("results_holdout")
    if results["boundaries"]["commercial_moat_proven"] is not False:
        fail("results_moat")

    # Internal-marker scan covers every text file, including files without an extension.
    markers = [
        "D:" + chr(92) + "A.K79",
        "C:" + chr(92) + "Users",
        "8753adb2" + "-2e1e-4b92-8eff-d5d6db59df72",
        "andruwka79-cloud/" + "AK79-OS",
    ]
    for rel in repo_files():
        text = (ROOT / rel).read_text(encoding="utf-8", errors="replace")
        for marker in markers:
            if marker in text:
                fail(f"internal_marker:{rel}")

    p = subprocess.run(
        [sys.executable, "-B", "-m", "unittest", "discover", "-s", str(ROOT / "tests"), "-v"],
        capture_output=True, text=True, timeout=120,
    )
    if p.returncode != 0:
        fail("unit_tests")

    print("AK79_PUBLIC_PROOF_V1_VERIFY_PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
