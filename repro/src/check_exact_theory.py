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
        "c5": "FALSIFIED",
    }
    got = {key: value["status"] for key, value in data["claims"].items()}
    if got != expected:
        raise AssertionError(f"verdict mismatch: {got} != {expected}")
    for claim in ["c1", "c2", "c3", "c4", "c5"]:
        obligations = data["claims"][claim]["obligations"]
        if not obligations or any(row["result"] != "unsat" for row in obligations):
            raise AssertionError(f"{claim}: missing or failed proof obligation")
    c5 = data["claims"]["c5"]
    if c5["counterexample"]["catchup_infimum_for_every_tbt"] != 1:
        raise AssertionError("claim 5 catch-up gap is not constant")
    if c5["counterexample"]["reward_gap"] <= c5["counterexample"]["catchup_infimum_for_every_tbt"]:
        raise AssertionError("claim 5 counterexample does not prevent stabilization")
    print("INDEPENDENT_CHECKER PASS")
    print(json.dumps(expected, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
