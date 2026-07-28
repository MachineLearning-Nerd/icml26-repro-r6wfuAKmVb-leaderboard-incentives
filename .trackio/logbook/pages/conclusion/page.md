# Conclusion


---
<!-- trackio-cell
{"type": "markdown", "id": "cell_da03be672002", "created_at": "2026-07-28T08:42:39+00:00", "title": "Executive summary"}
-->
## Executive summary

**5/6 claims verified (10 pts).**

Mechanisms: c1 no pure NE under just-overtake (best-response cycle); c2 (Prop 4.3) every NE preserves capability ordering (18/18 instances, exact-NE checked); c3 (Thm 4.6) NE-exists iff reward-gap <= overtake-cost (9/9, sharp flip at the cost threshold); c4 (Prop 5.3) TbT monotonically stabilizes to a unique theta-ordered NE; c5 (Prop 5.6) the TbT threshold grows as a power law in reward gaps (log-log R^2>0.98, beating the exponential fit) under power-law capability scaling.

Deferred: c6 (Winogrande empirical, Fig 1) — needs real LM fine-tuning, not a game-theory reproduction.

## Negative controls
- A: below-threshold reward gap -> a pure NE DOES exist (no-NE result is conditional on just-overtake, not vacuous).
- B: Prop 4.3 is NE-specific; transient best-response-cycle scores can violate capability ordering.
- C: c5 power-law fit (R^2>0.98) decisively beats the exponential alternative (R^2<0.76).
