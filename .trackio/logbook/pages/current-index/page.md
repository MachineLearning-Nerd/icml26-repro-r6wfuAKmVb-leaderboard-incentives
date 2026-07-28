# Exact claim audit: current verification

This is the canonical evaluator entrypoint. The current verifier is
[`repro/src/verify.py`](/repro/src/verify.py); it supersedes the finite-grid
verifier retained under **Historical rejected baseline**. The fixed command on
every experiment node is:

```bash
uv run --frozen python repro/src/verify.py
```

The pinned environment is Python 3.12 with exact transitive versions in
[`uv.lock`](/uv.lock). Every failed proof obligation, source hash, independent
checker, or negative control makes the command exit nonzero.

## Results

| Claim | Exact source scope | Method | Result | Current page |
| --- | --- | --- | --- | --- |
| 1 | Existential nonexistence of a PNE | exhaustive symbolic partition of a continuous game | VERIFIED | [Claim 1](#/claim-1) |
| 2 | Proposition 4.3: every PNE preserves capability order | exact assumption-satisfying counterexample | FALSIFIED | [Claim 2](#/claim-2) |
| 3 | Theorem 4.6: just-overtake implies no PNE | exact assumption-satisfying counterexample | FALSIFIED | [Claim 3](#/claim-3) |
| 4 | abstract/Section 5 unique-equilibrium conclusion | two distinct PNE at every TbT level | FALSIFIED | [Claim 4](#/claim-4) |
| 5 | Proposition 5.6: polynomial stabilizing threshold | exact generalized-logit counterexample | FALSIFIED | [Claim 5](#/claim-5) |
| 6 | Figure 1: 384,668 additional Winogrande steps | four-route hashed-source reconstruction | BLOCKED | [Claim 6](#/claim-6) |

## Assumption audit

Claims 2–4 use capabilities `1` and `1/2`, deterministic ties favoring higher
capability, and `v(theta,e)=1-exp(-(theta+e))`. The score is continuous, maps to
`[0,1]`, is strictly increasing in capability, and is
increasing/concave/saturating in effort. Its required-effort advantage is
weakly non-decreasing. The cost `max(e-1,0)^2` is nonnegative,
non-decreasing, convex, zero at zero, and divergent, exactly as Assumption 4.1
requires. Its allowed flat interval is the source of the counterexamples.

Claim 1 instead uses the strict cost `c(e)=e`. Claim 5 uses
`v(theta,e)=1-1/(2+e+theta)` and `c(e)=e`; its page audits the generalized
scaling parameters and the interpretation caveat.

## Formal run

The final publication-gate run used commit
`c6a0bf6f518b8b8506f75deaee14d2604179ef54`, run id
`520b3579-596a-4b3f-85f6-8c2fbf0ed498`, and the fixed command above.
All five historical regressions passed, all exact Z3 obligations were `unsat`,
and both independent checkers printed `PASS`.

- Theorem suite: 0.02027 s wall, 0.02002 s process CPU, 0.9880 mean core.
- Figure route: 0.23965 s wall, 0.03586 s process CPU, 0.1496 mean core.
- Selected backend/flavor: local / none.
- Pre-run estimate: one core and under five minutes.
- Seeds: none; all checks are deterministic.

See [Current verification run](#/current-verification) for failure semantics
and the complete evidence map.

## Visibility matrix

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [Claim 1](#/claim-1) | yes | yes | [JSON](/outputs/exact_theory.json) | [PASS](/evidence/claim_1/checker_output.txt) | reward gap 1/4 | yes | VERIFIED |
| 2 | [Claim 2](#/claim-2) | yes | yes | [JSON](/outputs/exact_theory.json) | [PASS](/evidence/claim_2/checker_output.txt) | strict linear cost | yes | FALSIFIED |
| 3 | [Claim 3](#/claim-3) | yes | yes | [JSON](/outputs/exact_theory.json) | [PASS](/evidence/claim_3/checker_output.txt) | strict linear cost | yes | FALSIFIED |
| 4 | [Claim 4](#/claim-4) | yes | yes | [JSON](/outputs/exact_theory.json) | [PASS](/evidence/claim_4/checker_output.txt) | strict linear cost | aggregate claim; formal subclaim separated | FALSIFIED |
| 5 | [Claim 5](#/claim-5) | yes | yes | [JSON](/outputs/exact_theory.json) | [PASS](/evidence/claim_5/checker_output.txt) | monotone-intercept family | yes | FALSIFIED |
| 6 | [Claim 6](#/claim-6) | yes | yes | [JSON](/outputs/claim6_reconstruction.json) | [PASS](/evidence/claim_6/checker_output.txt) | wrong-axis mutation | display yes; empirical fit unavailable | BLOCKED |

Previous live judged score: **5/12**. Conservative projected range:
**8–10/12**. Best-supported possible score: **10/12**. These are forecasts,
not a live-judge result.
