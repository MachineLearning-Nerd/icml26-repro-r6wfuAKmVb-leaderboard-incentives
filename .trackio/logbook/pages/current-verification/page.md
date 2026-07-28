# Current verification run

The fixed experiment command is:

```bash
uv run --frozen python repro/src/verify.py
```

## Failure semantics

The exact verifier constructs continuous-domain Z3 obligations. Every obligation
must be `unsat`, meaning no counterexample exists to the stated local proof
step. A satisfiable or unknown result raises `AssertionError`. A separately
implemented checker reads only `outputs/exact_theory.json`, validates verdicts,
proof-obligation results, calibration bounds, and the negative control, and
also exits nonzero on mismatch.

## Counterexamples

For claims 2–4, the flat cost `max(e-1,0)^2` satisfies the paper’s written Cost
Assumption but makes every effort through one free.

- Claim 2: rewards `[1,1]`, efforts `[0,3/4]`. Both players attain the maximum
  utility one, so this is a PNE, while the lower-capability model strictly
  outranks the higher-capability model.
- Claim 3: rewards `[1/10,0]`, efforts `[1,1]`. This is a PNE. At all zero, the
  required overtake-effort infimum is `1/2`, its cost is zero, and zero is
  strictly below the reward gap `1/10`.
- Claim 4: for every `Delta_tbt >= 0`, both `[1,0]` and `[1,1]` are PNE, while
  all zero is not. Because the common baseline cancels from score comparisons,
  no TbT level restores uniqueness in this admitted game.

Replacing the flat cost by `c(e)=e` destroys each claims 2–4 counterexample for
the intended reason. Claim 1’s below-threshold reward-gap control instead makes
all zero a PNE.

For claim 5, `v(theta,e)=1-1/(2+e+theta)` is an exact generalized-logit family
that satisfies C1–C3. Between capabilities one and zero, required catch-up
effort is always one, at every TbT baseline. With linear cost and reward gap
two, stabilization never occurs, contradicting Proposition 5.6’s existence
claim. The control with common lower bound and monotone alpha has catch-up
effort `1+Delta` and stabilizes at `Delta=1`.

## Formal run record

The formal run has not yet completed on this branch. Until raw output and the
independent checker result are captured here, this page is **not release-ready**.
