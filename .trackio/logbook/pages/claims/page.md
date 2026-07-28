# Claims


---
<!-- trackio-cell
{"type": "markdown", "id": "cell_b39a9b870fb8", "created_at": "2026-07-28T08:42:36+00:00", "title": "Anchored claims"}
-->
## Anchored claims

1. The paper proves that current leaderboard benchmarks induce a Stackelberg ranking game in which no pure-strategy Nash equilibrium generally exists among competing model developers (Section 3).
2. Proposition 4.3 shows that whenever a pure-strategy Nash equilibrium does exist, the resulting equilibrium ranking preserves the latent capability ordering of the models (Section 4, Proposition 4.3).
3. Theorem 4.6 identifies 'just-overtake' incentives as the failure mode: if there exists a rank r such that the cost of the required effort to overtake is less than the reward gap between ranks r-1 and r, the follower game admits no pure-strategy Nash equilibrium (Section 4, Theorem 4.6).
4. The tune-before-test (TbT) protocol is proven to induce a benchmark game with a unique Nash equilibrium that ranks models by latent quality, with monotone stabilizing effects as the TbT level increases (Section 5, Proposition 5.3).
5. Under power-law capability scaling, the TbT threshold needed to stabilize rankings grows only polynomially in the reward gaps between adjacent ranks (Section 5, Proposition 5.6).
6. An empirical demonstration on Winogrande shows that after applying TbT with 3,000 training steps, at least 384,668 additional training steps would be required to change the induced model ranking (Figure 1).

## Verdict

| claim | status | detail |
|---|---|---|
| c1 | VERIFIED | R=0.2: converged=False cycle_len=238 just-overtake(cost0.0828<R)=True | R=0.5: converged=False cycle_len=0 just-overtake(cost0.0828<R)=True | R=1.0: converged=False cycle |
| c2 | VERIFIED | 18 NE instances checked, 0 violate capability ordering/exactness | e.g. R=0.5,Delta=1.5: scores=[2.554 3.054 3.554] ordered=True exact_ne=True ; R=0.5,Delta=2.5: scores=[ |
| c3 | VERIFIED | NE-exists iff R<=0.0828(overtake cost); sweep=[np.float64(0.02), np.float64(0.04), np.float64(0.06), np.float64(0.07), np.float64(0.083), np.float64(0.09), np.float64(0.1 |
| c4 | VERIFIED | Delta sweep conv=[np.int64(0), np.int64(0), np.int64(0), np.int64(0), np.int64(1), np.int64(1), np.int64(1), np.int64(1), np.int64(1)] monotone=True; at Delta=1.2: 6/6 se |
| c5 | VERIFIED | alpha=0.5: theory_exp=1.00 fitted=1.43 power-law R2=0.9854 vs exponential R2=0.6961 D*=[np.float64(0.02), np.float64(0.06), np.float64(0.15), np.float64(0.32), np.float64 |
| c6 | DEFERRED | Winogrande empirical (Fig 1): after 3,000 TbT steps, >=384,668 more steps needed to flip ranking. Deferred — requires real LM fine-tuning on Winogrande, not a clean-room  |
