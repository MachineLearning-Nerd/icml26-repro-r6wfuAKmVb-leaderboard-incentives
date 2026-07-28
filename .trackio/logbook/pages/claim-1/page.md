# Claim 1 — VERIFIED

**Source contract.** Section 3’s existential claim is that the admitted class
contains ranking games with no pure-strategy Nash equilibrium. It is not a
universal no-equilibrium claim.

**Exact witness.** Two players have capabilities `(1,1/2)`,
`v(theta,e)=1-exp(-(theta+e))`, cost `c(e)=e`, rewards `(1,0)`, and ties favor
the higher capability. The verifier symbolically partitions every pair of
nonnegative real efforts into all high-winner and low-winner boundary/interior
cases. Z3 proves a profitable deviation in each case; all five coverage
obligations are `unsat`.

**Negative control.** Reducing the reward gap from one to `1/4`, below the
catch-up effort `1/2`, makes `(0,0)` a PNE. The control obligation is also
`unsat`, so the witness is not vacuous.

**Evidence.** [Verifier source](/repro/src/exact_theory.py);
[raw certificate](/outputs/exact_theory.json);
[claim contract](/evidence/claim_1/claim_contract.json);
[checker PASS](/evidence/claim_1/checker_output.txt);
[control output](/evidence/claim_1/negative_control_output.txt);
[runtime](/evidence/claim_1/actual_runtime_cpu.json).

Tested SHA: `8f8494d23146f77a0ed25520f32e9574df9e43be`.
Deterministic, no seed. Local CPU, estimated one core and under five minutes;
actual shared theorem suite 0.01955 seconds and 0.9906 mean core.

**Limitation.** This verifies the exact existential claim with one complete
continuous-domain witness; it does not assert that every admitted game lacks a
PNE.
