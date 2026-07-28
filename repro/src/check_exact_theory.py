"""Independent checker for the exact-theory raw output."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "outputs" / "exact_theory.json"


def main() -> int:
    data = json.loads(RAW.read_text())
    expected = {
        "c1": "VERIFIED",
        "c2": "FALSIFIED",
        "c3": "FALSIFIED",
        "c4": "FALSIFIED",
        "c5": "BLOCKED",
    }
    got = {key: value["status"] for key, value in data["claims"].items()}
    if got != expected:
        raise AssertionError(f"verdict mismatch: {got} != {expected}")
    for claim in ["c1", "c2", "c3", "c4"]:
        obligations = data["claims"][claim]["obligations"]
        if not obligations or any(row["result"] != "unsat" for row in obligations):
            raise AssertionError(f"{claim}: missing or failed proof obligation")
    rows = data["claims"]["c5"]["calibration_rows"]
    groups: dict[tuple[float, float], list[float]] = {}
    for row in rows:
        groups.setdefault((row["gamma"], row["K"]), []).append(row["normalized"])
    if any(max(values) > 3.0 for values in groups.values()):
        raise AssertionError(f"claim 5 normalized thresholds not bounded: {groups}")
    ratios = data["claims"]["c5"]["negative_control"]["ratios_to_lambda_pow_gamma"]
    if not all(a < b for a, b in zip(ratios, ratios[1:])):
        raise AssertionError("claim 5 exponential control did not diverge")
    print("INDEPENDENT_CHECKER PASS")
    print(json.dumps(expected, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
