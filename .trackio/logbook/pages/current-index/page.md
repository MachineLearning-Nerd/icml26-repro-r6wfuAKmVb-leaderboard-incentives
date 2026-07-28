# Exact claim audit: current candidate

This page is the canonical evaluator entrypoint. The current verifier is
`repro/src/verify.py` on branch `orx/exact-theorem-contracts`; it supersedes the
finite-grid verifier retained under **Historical rejected baseline**. The fixed
command on every experiment node is:

```bash
uv run --frozen python repro/src/verify.py
```

The environment is Python 3.12 with exact transitive versions in `uv.lock`.
Every failed proof obligation raises an exception, so the command exits nonzero.

## Current claim contracts

| Claim | Exact source scope | Method | Current result |
| --- | --- | --- | --- |
| 1 | Existential nonexistence of a PNE in a paper-admissible continuous ranking game | Exhaustive symbolic partition of all nonnegative two-player effort profiles | VERIFIED |
| 2 | Proposition 4.3: every PNE preserves capability order under Assumptions 4.1–4.2 | Assumption-satisfying exact counterexample plus independent checker | FALSIFIED |
| 3 | Theorem 4.6: just-overtake inequality implies no PNE | Assumption-satisfying exact counterexample to the all-zero-only step | FALSIFIED |
| 4 | The abstract/Section 5 unique-equilibrium conclusion, together with Proposition 5.3 monotonicity | Two distinct nonzero PNE persist at every TbT level; formal Proposition 5.3 alone is not contradicted | FALSIFIED |
| 5 | Proposition 5.6: a stabilizing threshold exists and is `O(lambda^gamma)` over the generalized scaling family | Exact continuous counterexample with model-specific lower bound and constant catch-up effort | FALSIFIED |
| 6 | Figure 1: Winogrande fit gives 384,668 additional steps at TbT 3,000 | Not part of this theorem-contract node | BLOCKED |

## Shared assumptions and numerical audit

Claims 2–4 use two capabilities `theta_high=1`, `theta_low=1/2`, deterministic
tie-breaking favoring the higher capability, and
`v(theta,e)=1-exp(-(theta+e))`. This score is continuous, maps into `[0,1]`,
is strictly increasing in capability, increasing/concave/saturating in effort,
and has non-decreasing required-effort gaps. The cost
`c(e)=max(e-1,0)^2` is nonnegative, non-decreasing, convex, zero at zero, and
diverges. Its allowed flat interval is what invalidates the paper proof’s move
from “weakly improve by reducing effort” to “effort must equal zero.”

Claim 1 instead uses the strictly increasing cost `c(e)=e`, rewards `[1,0]`,
and the same score. The symbolic cases cover every pair of nonnegative efforts,
not a grid or best-response trajectory.

## Evaluator-visible evidence

- Executable source: `repro/src/exact_theory.py`
- Independent checker: `repro/src/check_exact_theory.py`
- Cumulative entrypoint: `repro/src/verify.py`
- Pinned environment: `pyproject.toml`, `uv.lock`, `.python-version`
- Source audit and hashes:
  `.openresearch/artifacts/startup/source_audit.md`
- Per-claim contracts:
  `.openresearch/artifacts/claim_1/claim_contract.json` through
  `.openresearch/artifacts/claim_5/claim_contract.json`
- Raw output: `outputs/exact_theory.json` after the fixed command
- Compact verdict: `outputs/verdict.json`

The current run page records checker/control output, Git SHA, CPU allocation,
runtime, limitations, and deviations after the formal experiment completes.

## Visibility matrix

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | This page | yes | contract inline | `outputs/exact_theory.json` | independent | reward gap 1/4 | yes | pending formal run |
| 2 | This page | yes | counterexample inline | `outputs/exact_theory.json` | independent | strict linear cost | yes | pending formal run |
| 3 | This page | yes | counterexample inline | `outputs/exact_theory.json` | independent | strict linear cost | yes | pending formal run |
| 4 | This page | yes | two PNE inline | `outputs/exact_theory.json` | independent | strict linear cost | aggregate claim; formal subclaim separated | pending formal run |
| 5 | This page | yes | counterexample inline | `outputs/exact_theory.json` | independent | monotone-intercept family stabilizes | yes | pending formal run |
| 6 | This page | not yet | no | no | no | no | no | BLOCKED |

This is a research candidate, not a live-judge result. The previous live judged
score remains **5/12**.
