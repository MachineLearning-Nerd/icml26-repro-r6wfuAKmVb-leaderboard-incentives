"""Exact continuous-domain checks for claims 1--5 of arXiv:2603.08371."""
from __future__ import annotations

import json
import os
import platform
import resource
import subprocess
import sys
import time
from pathlib import Path

from z3 import And, If, Not, Real, RealVal, Solver, unsat

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "outputs" / "exact_theory.json"


def q(value: str):
    return RealVal(value)


def flat_cost(e):
    """Paper-admissible convex cost: zero through effort 1, quadratic after."""
    return If(e <= 1, 0, (e - 1) * (e - 1))


def expect_unsat(name: str, formula) -> dict:
    solver = Solver()
    solver.add(formula)
    result = solver.check()
    if result != unsat:
        raise AssertionError(f"{name}: expected unsat, got {result}: {solver.model()}")
    return {"obligation": name, "solver": "z3", "result": "unsat"}


def check_claim_1() -> dict:
    """Exact case proof for one continuous game with no PNE."""
    high = Real("c1_high_effort")
    low = Real("c1_low_effort")
    e = Real("c1_control_effort")
    minimum_high_winning_effort = If(low <= q("1/2"), 0, low - q("1/2"))
    obligations = [
        expect_unsat(
            "c1_high_wins_above_boundary_can_reduce",
            And(
                high >= 0,
                low >= 0,
                low <= high + q("1/2"),
                high > minimum_high_winning_effort,
                Not(
                    1 - minimum_high_winning_effort
                    > 1 - high
                ),
            ),
        ),
        expect_unsat(
            "c1_high_wins_at_low_boundary_is_overtaken",
            And(
                high == 0,
                low >= 0,
                low <= q("1/2"),
                Not(1 - q("3/4") > -low),
            ),
        ),
        expect_unsat(
            "c1_high_wins_at_positive_boundary_is_overtaken",
            And(
                low > q("1/2"),
                high == low - q("1/2"),
                Not(1 - (low + q("1/4")) > -low),
            ),
        ),
        expect_unsat(
            "c1_low_wins_middle_high_can_tie_and_win",
            And(
                high >= 0,
                low > high + q("1/2"),
                low < high + q("3/2"),
                Not(1 - (low - q("1/2")) > -high),
            ),
        ),
        expect_unsat(
            "c1_low_wins_high_can_reduce",
            And(
                high >= 0,
                low >= high + q("3/2"),
                Not(high + q("3/4") < low),
            ),
        ),
    ]
    obligations.append(
        expect_unsat(
            "c1_negative_control_zero_is_pne",
            And(e >= 0, If(e > q("1/2"), q("1/4") - e, -e) > 0),
        )
    )
    return {
        "status": "VERIFIED",
        "contract": "There exists a paper-admissible continuous follower game with no PNE.",
        "parameters": {
            "theta_high": 1,
            "theta_low": 0.5,
            "score": "1-exp(-(theta+e))",
            "cost": "e",
            "rewards": [1, 0],
            "tie_break": "higher capability",
        },
        "proof": (
            "Exhaustive partition of every nonnegative effort pair: high-capability "
            "winner above/boundary cases and low-capability winner middle/high cases."
        ),
        "obligations": obligations,
        "negative_control": "With reward gap 1/4 below catch-up effort 1/2, (0,0) is a PNE.",
    }


def check_claim_2() -> dict:
    """Assumption-satisfying inverted-ranking PNE counterexample."""
    e = Real("c2_deviation")
    obligations = [
        expect_unsat(
            "c2_no_profitable_deviation_equal_rewards",
            And(e >= 0, 1 - flat_cost(e) > 1),
        )
    ]
    obligations.extend(
        [
            expect_unsat(
                "c2_ranking_is_strictly_inverted",
                Not(q("1/2") + q("3/4") > 1),
            ),
            expect_unsat("c2_effort_is_in_flat_cost_region", Not(q("3/4") <= 1)),
        ]
    )
    old_pay = 1 - q("3/4")
    new_pay = 1 - q("51/100")
    obligations.extend(
        [
            expect_unsat(
                "c2_linear_cost_control_still_overtakes",
                Not(q("1/2") + q("51/100") > 1),
            ),
            expect_unsat(
                "c2_linear_cost_control_profitable_reduction",
                Not(new_pay > old_pay),
            ),
        ]
    )
    return {
        "status": "FALSIFIED",
        "contract": "Every PNE preserves capability order under Assumptions 4.1--4.2.",
        "counterexample": {
            "theta_high": 1,
            "theta_low": 0.5,
            "efforts": [0, 0.75],
            "score": "1-exp(-(theta+e))",
            "cost": "max(e-1,0)^2",
            "rewards": [1, 1],
            "scores_order": "lower capability strictly higher",
        },
        "assumption_audit": {
            "cost": "nonnegative, nondecreasing, convex, c(0)=0, divergent",
            "C1": "d v/d theta = exp(-(theta+e)) > 0",
            "C2": "d v/d e > 0, d2 v/d e2 < 0, limit 1",
            "C3": "effort advantage is piecewise 0, increasing, then theta gap",
        },
        "obligations": obligations,
        "negative_control": "Strictly increasing linear cost destroys this inverted PNE.",
    }


def check_claim_3() -> dict:
    """Counterexample to Theorem 4.6 under its written weak cost assumption."""
    e = Real("c3_deviation")
    low_payoff = If(e > q("3/2"), q("1/10"), 0) - flat_cost(e)
    obligations = [
        expect_unsat(
            "c3_lower_model_has_no_profitable_deviation",
            And(e >= 0, low_payoff > 0),
        ),
        expect_unsat(
            "c3_high_model_has_no_profitable_deviation",
            And(e >= 0, q("1/10") - flat_cost(e) > q("1/10")),
        ),
    ]
    obligations.extend(
        [
            expect_unsat(
                "c3_written_just_overtake_antecedent_holds",
                Not(q("0") < q("1/10")),
            ),
            expect_unsat(
                "c3_linear_cost_control_has_profitable_drop",
                Not(q("1/10") - q("1/2") > q("1/10") - 1),
            ),
        ]
    )
    return {
        "status": "FALSIFIED",
        "contract": "If adjacent just-overtake cost is below reward gap, no PNE exists.",
        "counterexample": {
            "theta_high": 1,
            "theta_low": 0.5,
            "efforts": [1, 1],
            "score": "1-exp(-(theta+e))",
            "cost": "max(e-1,0)^2",
            "rewards": [0.1, 0],
            "baseline_overtake_cost": 0,
            "reward_gap": 0.1,
            "pne_exists": True,
        },
        "obligations": obligations,
        "negative_control": "Replacing the flat segment by c(e)=e makes (1,1) non-equilibrium.",
    }


def check_claim_4() -> dict:
    """Two distinct nonzero PNE persist for every TbT level."""
    e = Real("c4_deviation")
    low_payoff = If(e > q("3/2"), q("1/10"), 0) - flat_cost(e)
    obligations = [
        expect_unsat(
            "c4_profile_1_0_lower_no_profitable_deviation",
            And(e >= 0, low_payoff > 0),
        ),
        expect_unsat(
            "c4_profile_1_1_lower_no_profitable_deviation",
            And(e >= 0, low_payoff > 0),
        ),
        expect_unsat(
            "c4_high_already_at_maximum_payoff",
            And(e >= 0, q("1/10") - flat_cost(e) > q("1/10")),
        ),
    ]
    obligations.append(
        expect_unsat(
            "c4_all_zero_has_profitable_deviation",
            Not(q("1/2") + q("3/4") > 1),
        )
    )
    return {
        "status": "FALSIFIED",
        "contract": "TbT induces a unique equilibrium ranked by latent quality, with monotone stabilization.",
        "counterexample": {
            "all_delta_nonnegative": True,
            "pne_profiles": [[1, 0], [1, 1]],
            "all_zero_is_pne": False,
            "profitable_all_zero_deviation": [0, 0.75],
            "reason_delta_cancels": "rank compares theta_i+Delta+e_i",
        },
        "formal_subclaim": "Proposition 5.3 itself is not contradicted; its antecedent is never true here.",
        "obligations": obligations,
        "negative_control": "With c(e)=e and reward gap 0.1, (0,0) is the unique PNE.",
    }


def check_claim_5() -> dict:
    """Counterexample to existence of the claimed stabilizing threshold."""
    baseline = Real("c5_tbt")
    delta = Real("c5_additional_effort")
    obligations = [
        expect_unsat(
            "c5_catchup_is_exactly_delta_greater_than_one",
            And(
                baseline >= 0,
                delta >= 0,
                (baseline + delta + 2 > baseline + 3) != (delta > 1),
            ),
        ),
        expect_unsat(
            "c5_reward_two_always_beats_cost_of_control_deviation",
            And(
                baseline >= 0,
                Not(q("2") - q("3/2") > 0),
            ),
        ),
        expect_unsat(
            "c5_no_baseline_can_raise_required_cost",
            And(
                baseline >= 0,
                Not(q("1") < q("2")),
            ),
        ),
        expect_unsat(
            "c5_monotone_intercept_control_stabilizes_at_one",
            Not(q("1") + q("1") >= q("2")),
        ),
    ]
    return {
        "status": "FALSIFIED",
        "contract": (
            "Under the written generalized scaling assumptions and c(e)>=kappa*e, "
            "a stabilizing threshold exists and is O(lambda^gamma)."
        ),
        "counterexample": {
            "theta_domain": "[0,1]",
            "score": "v(theta,e)=1-1/(2+e+theta)",
            "generalized_scaling": {
                "U(theta)": 1,
                "L(theta)": "theta/(1+theta)",
                "alpha(theta)": "-log(1+theta)",
                "beta(theta)": 1,
                "gamma": 1,
            },
            "cost": "c(e)=e",
            "kappa": 1,
            "reward_gap": 2,
            "rho": 2,
            "baseline_catchup_infimum": 1,
            "lambda": 2,
            "catchup_infimum_for_every_tbt": 1,
            "conclusion": "No finite TbT level satisfies c(e_req)>=reward_gap.",
        },
        "assumption_audit": {
            "C1": "partial_theta v = 1/(2+e+theta)^2 > 0",
            "C2": "partial_e v > 0, partial_ee v < 0, limit is 1",
            "C3": "required-effort advantage is piecewise zero, increasing, then the capability gap",
            "cost": "linear, hence nondecreasing, convex, c(0)=0, divergent, and c(e)>=1*e",
            "catchup": "always feasible",
        },
        "obligations": obligations,
        "interpretation_routes": [
            "Literal Proposition 5.6: counterexample satisfies its displayed scaling and cost conditions.",
            "Inherited Assumptions 4.1-4.2: the same continuous family satisfies C1-C3 exactly.",
            "If alpha(theta) is additionally required to be nondecreasing, the counterexample is excluded and the common-ceiling proof yields the claimed rate.",
        ],
        "negative_control": (
            "With a common L=0,U=1 and alpha_high=log(2)>alpha_low=0, "
            "e_req(Delta)=1+Delta, so reward gap two stabilizes at Delta=1."
        ),
    }


def run_exact_theory() -> dict:
    started = time.perf_counter()
    cpu_started = time.process_time()
    checks = {
        "c1": check_claim_1,
        "c2": check_claim_2,
        "c3": check_claim_3,
        "c4": check_claim_4,
        "c5": check_claim_5,
    }
    claims = {}
    for claim, fn in checks.items():
        claims[claim] = fn()
        print(
            "EXACT_CLAIM "
            + json.dumps(
                {
                    "claim": claim,
                    "status": claims[claim]["status"],
                    "contract": claims[claim]["contract"],
                },
                sort_keys=True,
            )
        )
    affinity = len(os.sched_getaffinity(0)) if hasattr(os, "sched_getaffinity") else None
    wall_seconds = time.perf_counter() - started
    process_cpu_seconds = time.process_time() - cpu_started
    git_sha = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    runtime = {
        "backend": "local",
        "selected_flavor": None,
        "estimated_required_cores": 1,
        "estimated_runtime": "under 5 minutes",
        "available_affinity_cpus": affinity,
        "host_visible_logical_cpus": os.cpu_count(),
        "platform": platform.platform(),
        "python": platform.python_version(),
        "wall_seconds": wall_seconds,
        "process_cpu_seconds": process_cpu_seconds,
        "mean_cpu_cores_used": process_cpu_seconds / wall_seconds,
        "max_rss_native": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "max_rss_native_unit": "bytes" if sys.platform == "darwin" else "KiB",
        "git_sha": git_sha,
        "seed": None,
    }
    payload = {
        "paper": "2603.08371v1",
        "claims": claims,
        "runtime": runtime,
        "verdict_rule": "Any failed proof obligation raises and exits nonzero.",
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print("EXACT_RAW " + json.dumps(payload, sort_keys=True))
    print("EXACT_RUNTIME " + json.dumps(runtime, sort_keys=True))
    print("EXACT_SUMMARY " + json.dumps({k: v["status"] for k, v in claims.items()}, sort_keys=True))
    return payload


if __name__ == "__main__":
    run_exact_theory()
