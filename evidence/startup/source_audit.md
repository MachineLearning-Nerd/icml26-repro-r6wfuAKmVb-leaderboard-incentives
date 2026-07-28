# Paper source audit

- Paper: *Leaderboard Incentives: Model Rankings under Strategic Post-Training*
- arXiv identifier/version: `2603.08371v1`
- Retrieval date: `2026-07-28` (Asia/Kolkata)
- Retrieval User-Agent: `OpenResearch-Reproduction/1.0 (paper audit; contact via github.com/MachineLearning-Nerd)`
- Primary HTML URL: `https://ar5iv.labs.arxiv.org/html/2603.08371`
- Primary HTML SHA-256: `3779b433938d92d88d9522ccef506645139eccaf7a2fb5d3f12a5518f8c4cf51`
- arXiv PDF URL: `https://arxiv.org/pdf/2603.08371`
- arXiv PDF SHA-256: `fba1d7c5d9bb365aba7e2f7b044ba62276d30858b24b71e5aeebea284f68ba74`
- TeX source URL: `https://export.arxiv.org/e-print/2603.08371`
- TeX source SHA-256: `9f6d8668713011bee867b6c83a8e88a5f6b9cec201cc1806a30c891b11106ae8`

## Anchors and exact scope

- Assumption 4.1, Section 4.1: `c : R_{\ge 0} -> R_{\ge 0}` is non-decreasing and
  convex, `c(0)=0`, and `lim_{e->infinity} c(e)=infinity`.
- Assumption 4.2, Section 4.1: continuous `v : Theta x R_{\ge 0} -> [0,1]`;
  C1 strictly increasing in capability at fixed effort; C2 non-decreasing,
  concave, and saturating in effort; C3 the higher-capability effort advantage is
  weakly non-decreasing in every attainable target score.
- Proposition 4.3, Section 4.2: for every `Delta_tbt >= 0`, every PNE, and every
  pair `i,j`, `theta_i > theta_j` implies the equilibrium score of `i` is at
  least that of `j`.
- Theorem 4.6, Section 4.3: for every fixed `Delta_tbt >= 0`, with deterministic
  tie-breaking that does not favor lower capability, any PNE must be all-zero;
  if any adjacent just-overtake cost is strictly below its reward gap, no PNE
  exists.
- Proposition 5.3, Section 5.2: for every `0 <= Delta_1 <= Delta_2`, if the
  all-zero profile is a PNE at `Delta_1`, it is also a PNE at `Delta_2`.
- Proposition 5.6, Section 5.4: under the generalized logit power-law scaling
  form and `c(e) >= kappa e`, a pairwise stabilizing threshold exists; in the
  feasible catch-up regime it is `O(lambda_r ** gamma_r)`, up to a factor
  depending only on baseline catch-up effort.
- Figure 1 caption and Section 5.1: Qwen2.5 models (0.5B, 1.5B, 3B, 7B, 14B)
  receive Winogrande LoRA post-training for 0--3,000 steps, batch size 8. Fitted
  generalized scaling curves imply
  `min_{r in {2,...,n}} e_req_r(Delta_tbt=3000) = 384,668` additional steps.

These theorem claims are universally quantified. Finite numerical sweeps are
corroboration only and cannot establish them.
