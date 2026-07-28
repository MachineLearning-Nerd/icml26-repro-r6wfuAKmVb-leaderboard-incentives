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

## Evaluator-visible matrix

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `#/claim-1` | yes | yes | `outputs/exact_theory.json` | PASS | reward gap 1/4 | yes | VERIFIED |
| 2 | `#/claim-2` | yes | yes | `outputs/exact_theory.json` | PASS | strict linear cost | yes | FALSIFIED |
| 3 | `#/claim-3` | yes | yes | `outputs/exact_theory.json` | PASS | strict linear cost | yes | FALSIFIED |
| 4 | `#/claim-4` | yes | yes | `outputs/exact_theory.json` | PASS | strict linear cost | aggregate claim; formal subclaim separated | FALSIFIED |
| 5 | `#/claim-5` | yes | yes | `outputs/exact_theory.json` | PASS | monotone-intercept family | yes | FALSIFIED |
| 6 | `#/claim-6` | yes | yes | `outputs/claim6_reconstruction.json` | PASS | wrong-axis mutation | display yes; empirical fit unavailable | BLOCKED |

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

The winning immutable experiment branch is
`orx/publication-gate-and-canonical-release`. Its final run is
`520b3579-596a-4b3f-85f6-8c2fbf0ed498` at
`c6a0bf6f518b8b8506f75deaee14d2604179ef54`. The fixed command is:

```bash
uv run --frozen python repro/src/verify.py
```

## Compute and cost

Every formal component was estimated at one CPU core and under five minutes,
so the authorized local backend was used. No GPU ran. The latest theorem suite
used 0.02027 seconds wall and 0.9880 mean CPU core. Figure reconstruction used
0.23965 seconds wall and 0.1496 mean core. Hugging Face compute runtime and
cost are both zero.

## BLOCKED claim

Claim 6 remains BLOCKED after exactly three verification routes and a fourth
falsification route. The source archive contains no per-checkpoint Winogrande
measurements, fit parameters, training code, or checkpoints. It can be
unblocked by those author artifacts or by published CPU-feasible
logits/checkpoints sufficient to recreate the measurements and fit.

## Publication action

All manifest, historical-subset, secret, logbook, blind-traversal, and final
regression gates pass. The exact action is a text-only Hugging Face Hub API
commit to the existing Space
`DineshAI/r6wfuAKmVb`, followed by a hash-verified download of that exact
revision and a fast-forward publication of the same text paths to GitHub
`master`. No second Space will be created.

## Release gates

- Historical subset: all 18 judged paths are present. Six historical Markdown
  pages and ten static assets are byte-identical. `README.md` and
  `logbook.json` have only additive current-navigation changes.
- Candidate validity: JSON, Markdown link targets, Python syntax, strict marimo
  check, SVG XML, and text-only MIME checks pass.
- Regression: the final fixed-command run passes all historical and exact
  checks at `c6a0bf6f518b8b8506f75deaee14d2604179ef54`.
- Controls: every current negative control produces the intended discriminating
  result; both independent checkers pass.
- Visibility: the second evaluator-blind traversal has no missing matrix cell.
- Secrets: the release allowlist scan found no credential-bearing file.

The exact upload allowlist and SHA-256 manifest are
[`upload-allowlist.txt`](upload-allowlist.txt) and
[`candidate-manifest.sha256`](candidate-manifest.sha256). The detailed blind
review and subset audit are
[`red-team.md`](red-team.md) and
[`historical-subset-check.md`](historical-subset-check.md).
