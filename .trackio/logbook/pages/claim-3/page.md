# Claim 3 — FALSIFIED

**Source contract.** Theorem 4.6 states that, with deterministic tie-breaking
not favoring lower capability, if an adjacent just-overtake cost is strictly
below its reward gap, no PNE exists.

**Counterexample.** Use the same paper-admissible score and flat convex cost as
claim 2, rewards `(0.1,0)`, and efforts `(1,1)`. The high-capability player
already gets reward `0.1` at zero cost. The lower player cannot win within the
free-cost interval and cannot profit by paying positive cost beyond it. Hence
`(1,1)` is a PNE.

At the all-zero profile, the lower model’s catch-up-effort infimum is `1/2`.
Its cost is zero, strictly below the `0.1` reward gap, so the exact theorem
antecedent holds.

**Proof defect exposed.** The paper’s argument turns “a player can weakly
improve by lowering effort” into “equilibrium effort must be zero.” The written
cost assumption does not supply that strictness.

**Negative control.** Under strict linear cost, dropping from effort one to zero
is profitable, destroying the witness.

**Evidence.** [Verifier](/repro/src/exact_theory.py);
[raw certificate](/outputs/exact_theory.json);
[contract](/evidence/claim_3/claim_contract.json);
[checker PASS](/evidence/claim_3/checker_output.txt);
[control](/evidence/claim_3/negative_control_output.txt);
[method](/evidence/claim_3/method.md).

Tested SHA: `c6a0bf6f518b8b8506f75deaee14d2604179ef54`.
Deterministic local CPU; shared theorem runtime 0.02027 seconds.
