"""Leaderboard Stackelberg game (clean-room, arXiv 2603.08371, Chen/Zhang/Hardt).

n developers, latent capability theta_i, benchmark-specific effort e_i.
  post-effort score  v(theta, e) = theta + h(e),  h(e)=A(1-exp(-e))  (concave, saturating)
  cost               c(e) = e^2  (convex)
  payoff_i           = reward(rank_i) - c(e_i)   (rank 1 = highest score = highest reward)
Tune-before-test (TbT): designer mandates effort Delta for all (e -> Delta + e).

c1 (Sec 3):  Stackelberg ranking game; no pure-strategy NE generally exists.
c2 (Prop 4.3): whenever a pure NE exists, the equilibrium ranking preserves the
              latent capability ordering (theta_i > theta_j => s_i >= s_j).
c3 (Thm 4.6): just-overtake failure mode — if cost(effort to overtake rank r-1) <
              reward gap(r-1,r), the follower game has NO pure NE.
c4 (Prop 5.3): TbT induces a unique NE ranked by quality, with monotone stabilizing
              effects as the TbT level Delta grows.
c5 (Prop 5.6): under power-law capability scaling, the TbT threshold needed to
              stabilize rankings grows only polynomially in the reward gaps.

Pure numpy, CPU, seeded.  All best-responses are vectorized over the effort grid.
"""
from __future__ import annotations
import numpy as np


def h(e, A=0.5):
    return A * (1.0 - np.exp(-np.maximum(e, 0.0)))


def h_inv(s, A=0.5):
    """inverse of h on [0,A): effort needed for capability gain s."""
    s = np.clip(s, -1e9, A * (1.0 - 1e-9))
    return -np.log(1.0 - s / A)


def score(theta, e, Delta=0.0, A=0.5):
    return theta + h(Delta + e, A)


def cost(e):
    return np.maximum(e, 0.0) ** 2


def reward_table(reward_fn, n):
    """reward(rank) for rank=1..n as a length-n array (index rank-1)."""
    return np.array([float(reward_fn(r)) for r in range(1, n + 1)])


def best_response(theta_i, others_scores, rtab, Delta=0.0, A=0.5, e_grid=None):
    """Maximize reward(rank(s_i)) - c(e_i) over effort e_i, vectorized over e_grid.

    rtab: length-n reward lookup (index rank-1).  Returns the best effort.
    """
    if e_grid is None:
        e_grid = np.linspace(0.0, 4.0, 4000)
    others = np.asarray(others_scores, dtype=float)
    s_i = theta_i + h(Delta + e_grid, A)                       # (G,)
    ranks = 1 + (others[:, None] > s_i[None, :]).sum(axis=0)   # (G,), rank 1=best
    pays = rtab[np.clip(ranks - 1, 0, len(rtab) - 1)] - cost(e_grid)
    return float(e_grid[int(np.argmax(pays))])


def best_response_profile(thetas, es, reward_fn, Delta=0.0, A=0.5, e_grid=None):
    """One round of simultaneous best responses (Jacobi update)."""
    n = len(thetas)
    rtab = reward_table(reward_fn, n)
    scores = score(thetas, es, Delta, A)
    new = np.empty(n)
    for i in range(n):
        others = np.delete(scores, i)
        new[i] = best_response(thetas[i], others, rtab, Delta, A, e_grid)
    return new


def find_ne(thetas, reward_fn, Delta=0.0, A=0.5, iters=400, e_grid=None,
            tol=1e-7, seed=0):
    """Iterate best responses; return (converged, final_e, cycle_len).

    converged=True  -> a fixed point reached (a pure NE exists).
    converged=False -> a best-response cycle detected (no pure NE)."""
    rng = np.random.default_rng(seed)
    e = rng.uniform(0.0, 0.3, len(thetas))
    seen = {}
    for t in range(iters):
        e_new = best_response_profile(thetas, e, reward_fn, Delta, A, e_grid)
        if np.max(np.abs(e_new - e)) < tol:        # fixed point -> pure NE
            return True, e_new, 0
        key = tuple(np.round(e_new, 5))
        if key in seen:                            # cycle -> no stable pure NE
            return False, e_new, t - seen[key]
        seen[key] = t
        e = e_new
    return False, e, 0


def is_ne(thetas, es, reward_fn, Delta=0.0, A=0.5, e_grid=None, tol=1e-6):
    """True iff no single developer can profitably deviate (exact NE check)."""
    n = len(thetas)
    rtab = reward_table(reward_fn, n)
    scores = score(thetas, es, Delta, A)
    for i in range(n):
        others = np.delete(scores, i)
        cur_pay = rtab[int(np.clip(1 + (others > scores[i]).sum() - 1, 0, n - 1))] - cost(es[i])
        br = best_response(thetas[i], others, rtab, Delta, A, e_grid)
        if br - es[i] > tol:                       # a strictly better response exists
            return False
    return True
