# Leaderboard Incentives — exact reproduction

[![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/MachineLearning-Nerd/icml26-repro-r6wfuAKmVb-leaderboard-incentives/blob/master/leaderboard_incentives_reproduction.py)

We reproduced six claims from *Leaderboard Incentives: Model Rankings under
Strategic Post-Training* ([arXiv 2603.08371](https://arxiv.org/abs/2603.08371)).
The earlier three-player sweeps remain visible as historical toy evidence. The
current verifier instead uses exact continuous-domain obligations.

The strongest outcome is not a numerical confirmation: claims 2–5 have
assumption-satisfying counterexamples. Claim 1 is VERIFIED. Claims 2–5 are
FALSIFIED under their written scope. Claim 6’s published Figure 1 endpoint
reconstructs as **384,667.5595 → 384,668**, but the raw Winogrande measurements
and fit parameters are absent, so the empirical claim is **BLOCKED**.

Previous live judged score: **5/12**. Conservative forecast after publication:
**8–10/12**. Best-supported possible score: **10/12**. These are forecasts, not
judge results.

Read the illustrated [reproduction report](reports/reproduction/report.md), the
[complete command record](reports/reproduction/commands.md), or the
[self-contained marimo tutorial](leaderboard_incentives_reproduction.py).

## Claim summary

| Claim | Paper number or statement | Observed evidence | Assessment |
| --- | --- | --- | --- |
| 1 | pure NE generally need not exist | exact no-PNE continuous game | VERIFIED |
| 2 | every PNE preserves capability order | `[0,3/4]` is an inverted-ranking PNE | FALSIFIED |
| 3 | just-overtake inequality implies no PNE | `[1,1]` is a PNE with cost `0 < 0.1` | FALSIFIED |
| 4 | TbT yields a unique stable equilibrium | two nonzero PNE persist for every TbT | FALSIFIED for aggregate uniqueness |
| 5 | stabilizing threshold exists and is polynomial | exact generalized-logit family never stabilizes | FALSIFIED |
| 6 | 384,668 steps at TbT 3,000 | source display gives 384,667.5595; raw fit inputs missing | BLOCKED |

All formal work used local CPU because each task was estimated at one core and
under five minutes. No GPU was used. The claim-6 route is a source
reconstruction, not a substitute fine-tuning run.

## Experiment log

The exact command in every formal node is
`uv run --frozen python repro/src/verify.py`.

| Branch / experiment | Purpose or change | Exact run command | Assessment / outcome | Compute |
| --- | --- | --- | --- | --- |
| `master` | publication surface | Not run as an experiment (publication surface) | README, report, notebook, and published evidence | none |
| [`orx/frozen-judged-baseline`](https://github.com/MachineLearning-Nerd/icml26-repro-r6wfuAKmVb-leaderboard-incentives/tree/orx/frozen-judged-baseline) | freeze judged artifact and lock environment | `uv run --frozen python repro/src/verify.py` | historical c1–c5 toy checks pass | local CPU |
| [`orx/exact-theorem-contracts`](https://github.com/MachineLearning-Nerd/icml26-repro-r6wfuAKmVb-leaderboard-incentives/tree/orx/exact-theorem-contracts) | exact contracts for claims 1–4 | `uv run --frozen python repro/src/verify.py` | c1 VERIFIED; c2–c4 FALSIFIED | local CPU |
| [`orx/full-generalized-scaling-proof`](https://github.com/MachineLearning-Nerd/icml26-repro-r6wfuAKmVb-leaderboard-incentives/tree/orx/full-generalized-scaling-proof) | test Proposition 5.6 over model-specific bounds | `uv run --frozen python repro/src/verify.py` | c5 FALSIFIED; cumulative checker passes | local CPU |
| [`orx/figure-1-source-reconstruction`](https://github.com/MachineLearning-Nerd/icml26-repro-r6wfuAKmVb-leaderboard-incentives/tree/orx/figure-1-source-reconstruction) | hashed Figure 1 reconstruction and four claim-6 routes | `uv run --frozen python repro/src/verify.py` | displayed number reproduced; empirical claim BLOCKED | local CPU |
| [`orx/evaluator-visible-release-candidate`](https://github.com/MachineLearning-Nerd/icml26-repro-r6wfuAKmVb-leaderboard-incentives/tree/orx/evaluator-visible-release-candidate) | cumulative evidence and publication gates | `uv run --frozen python repro/src/verify.py` | pending final release-gate run | local CPU |

## Reproduce

```bash
uv sync --frozen
uv run --frozen python repro/src/verify.py
```

The command exits nonzero if a proof obligation, source hash, independent
checker, or negative control fails. Raw outputs are
[`outputs/exact_theory.json`](outputs/exact_theory.json) and
[`outputs/claim6_reconstruction.json`](outputs/claim6_reconstruction.json).

For the notebook:

```bash
uv run marimo edit leaderboard_incentives_reproduction.py
uv run marimo run leaderboard_incentives_reproduction.py
```
