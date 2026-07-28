# Reproduction command record

The fixed command for every formal node was:

```bash
uv run --frozen python repro/src/verify.py
```

Formal orchestration:

```bash
orx exp run 10b7145e-dfc5-42fe-b3ef-3399f1d6630b --backend local
orx exp run df7aa6aa-48f0-4a84-be84-e63a22538c91 --backend local
orx exp run 563f0c98-59c5-4609-a4c1-025c7500fa9d --backend local
orx exp run 14ce811d-2e5a-43e2-a545-6adeee83c4bc --backend local
```

Evidence was read only with:

```bash
orx logs 0cc08953-60b3-49bd-980a-134dcb8de7f8
orx logs aca2cd3d-34b4-4e86-bc83-e10889fa19b8
orx logs 04a6b05c-72b1-4be0-aae7-4c7336dc6dec
orx logs 2c3e5881-2014-4ccc-93cc-16de3d7e1c4b
orx logs 75e9d7b5-a1bc-4001-a5b4-55659a898285
```

The failed `2c3e...` run exposed a null-width PDF drawing parser bug and
produced no claim-6 result. Commit `93d5371` fixed the guard; `75e9...` is the
successful cumulative evidence run.

Startup and source commands included `orx projects --json`, `orx runs
8ea3634c-552d-4d91-b35d-e260be2b6dd6`, `orx project view`, `orx exp status`,
`orx exp wait`, `orx exp desc`, `git status --short`, `git branch -a`,
`git rev-parse`, `git fetch`, `git checkout`, `git commit`, `git push`,
`hf download`, `orx paper 2603.08371 --full`, `pdfinfo`, `pdftotext`, and
SHA-256 checks. Paper retrieval used an explicit
`OpenResearch-Reproduction/1.0` User-Agent.
