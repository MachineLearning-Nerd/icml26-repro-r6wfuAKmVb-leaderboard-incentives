# Claim 4 — FALSIFIED

**Scope separation.** The abstract and Section 5 say TbT induces a unique
quality-ordered equilibrium. Formal Proposition 5.3 is narrower: if all-zero is
a PNE at one TbT level, it stays a PNE at every higher level. The counterexample
falsifies the aggregate uniqueness claim, not Proposition 5.3’s conditional
implication.

**Counterexample.** With the paper-admissible flat cost, exponential score,
capabilities `(1,1/2)`, and rewards `(0.1,0)`, both `(1,0)` and `(1,1)` are PNE
for every `Delta >= 0`. The common TbT baseline cancels from comparisons of
`theta+Delta+e`. The all-zero profile is not a PNE because the lower player can
move to effort `3/4`, overtake for free, and gain `0.1`.

The obligations are symbolic in `Delta`, not a finite sweep.

**Negative control.** Strict linear cost yields the unique all-zero PNE for the
same reward gap, removing both nonzero equilibria.

**Evidence.** [Verifier](/repro/src/exact_theory.py);
[raw certificate](/outputs/exact_theory.json);
[contract](/evidence/claim_4/claim_contract.json);
[checker PASS](/evidence/claim_4/checker_output.txt);
[control](/evidence/claim_4/negative_control_output.txt);
[limitations](/evidence/claim_4/limitations.md).

Tested SHA: `8f8494d23146f77a0ed25520f32e9574df9e43be`.
Confidence is MEDIUM because the imported claim combines the aggregate
uniqueness language with a narrower formal proposition.
