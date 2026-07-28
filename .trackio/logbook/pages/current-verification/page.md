# Current verification run

The tested current verifier is [`repro/src/verify.py`](/repro/src/verify.py) at
Git SHA `c6a0bf6f518b8b8506f75deaee14d2604179ef54`. It supersedes the old
finite-grid verifier under **Historical rejected baseline**.

```bash
uv run --frozen python repro/src/verify.py
```

## Failure semantics

The exact verifier constructs continuous-domain Z3 obligations. Every
obligation must be `unsat`, meaning no counterexample exists to its local proof
step. A satisfiable or unknown result raises `AssertionError`. Separately
implemented readers validate the raw JSON, verdicts, calibration bounds, and
negative controls. Any mismatch exits nonzero.

The successful cumulative run
`520b3579-596a-4b3f-85f6-8c2fbf0ed498` printed:

```text
EXACT_SUMMARY {"c1":"VERIFIED","c2":"FALSIFIED","c3":"FALSIFIED","c4":"FALSIFIED","c5":"FALSIFIED"}
INDEPENDENT_CHECKER PASS
CLAIM6_INDEPENDENT_CHECKER PASS
{"rounded": 384668, "status": "BLOCKED"}
```

All historical claim 1–5 regressions also printed `PASS`.

## Evidence map

- Cumulative entrypoint: [`verify.py`](/repro/src/verify.py)
- Exact theory verifier: [`exact_theory.py`](/repro/src/exact_theory.py)
- Figure verifier: [`claim6_figure.py`](/repro/src/claim6_figure.py)
- Independent checkers: [`check_exact_theory.py`](/repro/src/check_exact_theory.py)
  and [`check_claim6.py`](/repro/src/check_claim6.py)
- Raw theory output: [`exact_theory.json`](/outputs/exact_theory.json)
- Raw Figure output:
  [`claim6_reconstruction.json`](/outputs/claim6_reconstruction.json)
- Compact verdict: [`verdict.json`](/outputs/verdict.json)
- Pinned environment: [`pyproject.toml`](/pyproject.toml),
  [`uv.lock`](/uv.lock), [`.python-version`](/.python-version)
- Paper/source hash audit:
  [`source_audit.md`](/evidence/startup/source_audit.md)
- Complete command record:
  [`commands.md`](/reports/reproduction/commands.md)
- Illustrated report:
  [`report.md`](/reports/reproduction/report.md)

## Compute

Both components were estimated at one core and under five minutes and therefore
used the authorized local backend. The theorem component used 0.02027 seconds
wall and 0.9880 mean CPU core. Figure reconstruction used 0.23965 seconds wall
and 0.1496 mean core. Selected remote flavor: none. Hugging Face compute cost:
zero. GPU use: none.

## Limitation

Claim 6 remains BLOCKED. The exact source display is reproducible, but the
arXiv bundle contains no raw Winogrande measurements, fit parameters, training
code, or checkpoints, so the empirical fit cannot be independently rerun.
