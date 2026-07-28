# Claim 2 — FALSIFIED

**Source contract.** Proposition 4.3 says that for every TbT level and every
PNE under Assumptions 4.1–4.2, higher capability implies weakly higher score.

**Counterexample.** Capabilities are `(1,1/2)`, rewards are equal `(1,1)`,
ties favor higher capability, and
`v(theta,e)=1-exp(-(theta+e))`. The cost
`c(e)=max(e-1,0)^2` is nonnegative, non-decreasing, convex, zero at zero, and
divergent. At efforts `(0,3/4)`, both players receive the maximum utility one,
so no deviation can improve utility. The lower-capability player nevertheless
has strictly higher score because `1/2+3/4 > 1+0`.

Z3 independently proves both PNE optimality and strict rank inversion.

**Negative control.** Replacing the permitted flat cost with `c(e)=e` makes the
lower player’s positive effort costly and creates a profitable reduction, so
the inverted profile is no longer a PNE.

**Evidence.** [Verifier source](/repro/src/exact_theory.py);
[raw certificate](/outputs/exact_theory.json);
[contract](/evidence/claim_2/claim_contract.json);
[assumption audit](/evidence/claim_2/source_audit.md);
[checker PASS](/evidence/claim_2/checker_output.txt);
[control](/evidence/claim_2/negative_control_output.txt);
[limitations](/evidence/claim_2/limitations.md).

Tested SHA: `8f8494d23146f77a0ed25520f32e9574df9e43be`.
Deterministic local CPU; shared theorem runtime 0.01955 seconds.
