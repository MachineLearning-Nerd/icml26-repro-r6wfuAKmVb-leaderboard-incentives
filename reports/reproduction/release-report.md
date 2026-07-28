- Previous live judged score: `5/12`
- Conservative projected score range after the proposed change: `8–10/12`
- Best-supported possible new score: `10/12` (**forecast, not a judge result**)

# Release report

The current total score remains **5/12** at Hugging Face Head and Judge Head
`6dbff965ffdf5b7b1e668759d717fc161ee0a793`. Only the live evaluator can change
that score.

| Claim | Current points | Possible points | Confidence | Evidence status | Basis and remaining risk |
| --- | ---: | ---: | --- | --- | --- |
| 1 | 1 | 2 | HIGH | VERIFIED | exhaustive continuous-domain no-PNE witness; exact existential scope |
| 2 | 1 | 2 | HIGH | FALSIFIED | exact inverted PNE satisfies the written score, reward, cost, and tie assumptions |
| 3 | 1 | 2 | HIGH | FALSIFIED | exact PNE satisfies the just-overtake antecedent; the missing strictness step is isolated |
| 4 | 1 | 2 | MEDIUM | FALSIFIED | aggregate uniqueness fails; formal Proposition 5.3’s narrower conditional statement is not contradicted |
| 5 | 1 | 2 | MEDIUM | FALSIFIED | displayed generalized scaling conditions and C1–C3 admit the witness; an unstated monotone-alpha interpretation remains a review risk |
| 6 | 0 | 0 | LOW | BLOCKED | four different source routes reproduce the display but raw empirical inputs are absent |

## Changes since the live verdict

- Claim 1 replaces finite best-response trajectories with a complete symbolic
  partition over a continuous admitted game.
- Claims 2–4 replace finite corroboration with assumption-satisfying exact
  counterexamples and controls.
- Claim 5 replaces a fitted finite sweep with an exact generalized-logit
  counterexample and a stabilizing control.
- Claim 6 now has four documented routes, a source-hash-checked reconstruction
  of `384667.559495 → 384668`, an independent checker, and a failing wrong-axis
  control. It remains BLOCKED.

## Experiment tree

The campaign grew as a single descending chain:

1. `orx/frozen-judged-baseline` — locked environment and historical regression.
2. `orx/exact-theorem-contracts` — exact claims 1–4.
3. `orx/full-generalized-scaling-proof` — exact claim 5.
4. `orx/figure-1-source-reconstruction` — four claim-6 routes.
5. `orx/evaluator-visible-release-candidate` — cumulative evidence and public
   report.
6. `orx/publication-gate-and-canonical-release` — final immutable gate.

The latest completed cumulative evidence run before the final gate is
`7edf2d16-e61f-4a50-8c08-3fa3f022006a` at
`8f8494d23146f77a0ed25520f32e9574df9e43be`. The fixed command is:

```bash
uv run --frozen python repro/src/verify.py
```

## Compute and cost

Every formal component was estimated at one CPU core and under five minutes,
so the authorized local backend was used. No GPU ran. The latest theorem suite
used 0.01955 seconds wall and 0.9906 mean CPU core. Figure reconstruction used
0.61023 seconds wall and 0.06036 mean core. Hugging Face compute runtime and
cost are both zero.

## BLOCKED claim

Claim 6 remains BLOCKED after exactly three verification routes and a fourth
falsification route. The source archive contains no per-checkpoint Winogrande
measurements, fit parameters, training code, or checkpoints. It can be
unblocked by those author artifacts or by published CPU-feasible
logits/checkpoints sufficient to recreate the measurements and fit.

## Publication action

After the remaining manifest, historical-subset, secret, logbook, blind
traversal, and final regression gates pass, the exact action is a text-only
Hugging Face Hub API commit to the existing Space
`DineshAI/r6wfuAKmVb`, followed by a hash-verified download of that exact
revision and a fast-forward publication of the same text paths to GitHub
`master`. No second Space will be created.

The exact upload allowlist, SHA-256 manifest, final Space revision, historical
subset result, red-team record, and final winning Git SHA are filled from the
immutable candidate immediately before publication.
