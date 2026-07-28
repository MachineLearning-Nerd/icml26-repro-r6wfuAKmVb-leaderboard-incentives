# Evaluator-blind pre-publication review

The reviewer used only a freshly assembled candidate Space and the evaluator
rubric. Repository history, OpenResearch descriptions, run logs, and dashboard
paths were not used to fill gaps.

## Pass 1 — issue found

Files opened, in order:

1. `README.md`
2. `logbook.json`
3. `pages/current-index/page.md`
4. `pages/current-verification/page.md`
5. `pages/claim-1/page.md` through `pages/claim-6/page.md`
6. `repro/src/verify.py`, both current verifiers, and both independent checkers
7. `outputs/exact_theory.json`, `outputs/claim6_reconstruction.json`, and
   `outputs/verdict.json`
8. linked claim contracts, checker outputs, controls, runtime records, source
   audits, and limitations under `evidence/`

Conclusion: every claim was discoverable, but the canonical run page and raw
output named the preceding candidate run, not the final immutable publication
gate. The candidate was rejected.

Fix: capture run `520b3579-596a-4b3f-85f6-8c2fbf0ed498`, replace the generated
JSON with that run’s output, update checker/runtime records, and cite tested SHA
`c6a0bf6f518b8b8506f75deaee14d2604179ef54` on every current claim page.

## Pass 2 — complete

The candidate was rebuilt from a fresh download of judged revision
`6dbff965ffdf5b7b1e668759d717fc161ee0a793`. The reviewer repeated the same
file sequence from `README.md` and `logbook.json`.

Findings:

- Current verification is first; the old verifier appears only under
  **Historical rejected baseline**.
- Every claim page states the exact contract or scope, method, numerical or
  symbolic result, control, verdict, tested SHA, and limitation.
- The shared canonical pages expose the fixed command, pinned environment,
  CPU estimate/allocation/runtime, deterministic seed policy, executable code,
  raw downloads, and failure semantics.
- Displayed statuses and numbers match the linked raw JSON.
- Claim 6 is visibly BLOCKED and does not present the reconstructed display as
  an empirical rerun.
- All six visibility-matrix rows are complete.

No conclusion required hidden paths or experiment-log knowledge. Pass 2 is
release-ready.
