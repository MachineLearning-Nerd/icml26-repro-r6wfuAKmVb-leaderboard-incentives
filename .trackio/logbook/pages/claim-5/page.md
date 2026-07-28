# Claim 5 — FALSIFIED

**Source contract.** Proposition 5.6 states that under its generalized-logit
scaling conditions and `c(e) >= kappa e`, a finite stabilizing threshold exists
and scales as `O(lambda^gamma)`.

**Counterexample family.**

```text
v(theta,e) = 1 - 1/(2+e+theta),  theta in [0,1]
```

This is the displayed generalized form with `U(theta)=1`,
`L(theta)=theta/(1+theta)`, `alpha(theta)=-log(1+theta)`,
`beta(theta)=1`, and `gamma=1`. Direct derivatives establish C1–C3.
With `c(e)=e`, capabilities one and zero, and reward gap two, the lower model’s
catch-up-effort infimum is exactly one for every TbT baseline. Its cost therefore
never reaches the reward gap, so no finite stabilizing threshold exists.

**Negative control.** With common bounds and monotone intercept
`alpha_high=log(2)>alpha_low=0`, required catch-up effort is `1+Delta`; reward
gap two stabilizes at `Delta=1`.

**Interpretation risk.** An earlier paragraph describes monotone `alpha(theta)`
as sufficient, but Proposition 5.6 does not state that restriction. The witness
satisfies its displayed conditions and inherited C1–C3. Confidence is MEDIUM
because a reviewer may import the unstated sufficient condition.

**Evidence.** [Verifier](/repro/src/exact_theory.py);
[raw certificate](/outputs/exact_theory.json);
[contract](/evidence/claim_5/claim_contract.json);
[source audit](/evidence/claim_5/source_audit.md);
[checker PASS](/evidence/claim_5/checker_output.txt);
[control](/evidence/claim_5/negative_control_output.txt).

Tested SHA: `8f8494d23146f77a0ed25520f32e9574df9e43be`.
