import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = Path(__file__).resolve().with_name("RELEASE_MANIFEST.json")

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
assert manifest["release"] == "AK79 Public Proof v1"
assert manifest["version"] == "1.0.0"

for item in manifest["files"]:
    path = ROOT / item["path"]
    assert path.is_file(), f"missing:{item['path']}"
    assert sha256(path) == item["sha256"], f"hash_mismatch:{item['path']}"

json.loads((ROOT / "benchmark/visible_vectors.json").read_text(encoding="utf-8"))
results = json.loads((ROOT / "results/public_results_v1.json").read_text(encoding="utf-8"))
assert results["external_certification"] is False
assert results["production_claim"] is False
assert results["boundaries"]["final_hidden_holdout_published"] is False
assert results["boundaries"]["commercial_moat_proven"] is False

forbidden_internal_markers = [
    "D:" + chr(92) + "A.K79",
    "C:" + chr(92) + "Users",
    "8753adb2" + "-2e1e-4b92-8eff-d5d6db59df72",
    "andruwka79-cloud/" + "AK79-OS",
]
for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    if path.suffix.lower() not in {".md", ".json", ".py", ".yml", ".yaml", ".txt"}:
        continue
    text = path.read_text(encoding="utf-8", errors="replace")
    for marker in forbidden_internal_markers:
        assert marker not in text, f"internal_marker:{marker}:{path.relative_to(ROOT)}"

p = subprocess.run(
    [sys.executable, "-B", "-m", "unittest", "discover", "-s", str(ROOT / "tests"), "-v"],
    capture_output=True,
    text=True,
    timeout=30,
)
assert p.returncode == 0, p.stdout + p.stderr

print("AK79_PUBLIC_PROOF_V1_VERIFY_PASS")
