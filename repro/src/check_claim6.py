"""Independent checker for the Figure 1 source reconstruction."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "outputs" / "claim6_reconstruction.json"


def main() -> int:
    data = json.loads(RAW.read_text())
    direct, endpoint_blind, anchors, falsification = data["routes"]
    if data["status"] != "BLOCKED":
        raise AssertionError("claim 6 must remain BLOCKED without raw training data")
    if direct["rounded_y"] != 384668 or direct["x"] != 3000:
        raise AssertionError(f"direct reconstruction mismatch: {direct}")
    if endpoint_blind["relative_error"] >= 0.0001:
        raise AssertionError(f"held-out endpoint prediction mismatch: {endpoint_blind}")
    if anchors["total_occurrences"] != 3:
        raise AssertionError(f"source anchors missing: {anchors}")
    if falsification["valid_falsification_found"]:
        raise AssertionError("unexpected falsification")
    if data["negative_control"]["passes_384668_check"]:
        raise AssertionError("negative control unexpectedly passed")
    if data["raw_training_data_present_in_source"]:
        raise AssertionError("source-data availability audit changed")
    print("CLAIM6_INDEPENDENT_CHECKER PASS")
    print(json.dumps({"rounded": direct["rounded_y"], "status": data["status"]}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
