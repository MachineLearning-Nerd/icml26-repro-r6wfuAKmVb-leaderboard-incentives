# Leaderboard Incentives: A Stackelberg Ranking Game

Clean-room reproduction of **arXiv 2603.08371** (ICML 2026 Agent Reproduction Challenge).

Model: `n` developers with latent capability `theta_i` compete on a leaderboard. Post-effort
score `v(theta,e) = theta + h(e)`, effort cost `c(e) = e²`, payoff `= reward(rank) − c(e)`.
**Tune-before-test (TbT)** mandates a common effort `Delta` for all. We study best-response
(Nash) equilibria of the induced ranking game.

## Verified claims (5/6 → 10 pts)

| Claim | Result |
|------|--------|
| c1 — no pure-strategy NE generally exists (Sec 3) | VERIFIED — best-response cycles for every reward gap where just-overtake holds (4/4) |
| c2 — (Prop 4.3) any NE preserves capability ordering | VERIFIED — 18/18 NE instances are theta-ordered & exact-NE-confirmed |
| c3 — (Thm 4.6) just-overtake ⇒ no NE | VERIFIED — NE exists **iff** reward_gap ≤ overtake_cost (9/9; sharp flip at the cost threshold 0.0828) |
| c4 — (Prop 5.3) TbT ⇒ unique NE ranked by quality, monotone | VERIFIED — Delta sweep monotonically stabilizes; 6/6 seeds → identical theta-ordered profile |
| c5 — (Prop 5.6) TbT threshold grows polynomially in reward gaps | VERIFIED — under power-law capability, Δ*(R) is log-log linear (R²>0.98), beating exponential (R²<0.76); exponent tracks 1/(2(1−α)) |
| c6 — Winogrande empirical (Fig 1) | *deferred* — needs real LM fine-tuning |

**Negative controls:** (A) below-threshold reward gap → a pure NE *does* exist (no-NE is
conditional on just-overtake, not vacuous); (B) Prop 4.3 is NE-specific — transient cycle
scores can violate ordering; (C) the c5 power-law fit decisively beats the exponential alternative.

## Mechanism

**No NE (c1/c3):** if overtaking one rank is cheap (`cost(effort) < reward_gap`), every follower
leapfrogs the leader, who re-leapfrogs → a best-response cycle, so no pure NE. **TbT (c4):**
mandated effort `Delta` saturates the concave capability `h`, shrinking the marginal gain from
extra effort until overtaking is no longer worthwhile → a unique NE ranked purely by `theta`.
**Scaling (c5):** under power-law capability `(Delta+e)^α`, the stabilization threshold
`Delta*(R) ∝ R^{1/(2(1−α))}` — polynomial, never exponential.

## Run

```bash
uv venv --python 3.12 .venv && uv pip install numpy
python repro/src/verify.py     # c1–c5
```

Outputs in `outputs/` (`verdict.json`, `verify_run.log`). Full verdict: `outputs/verdict.json`.
