# Historical evidence subset check

Baseline Space: `DineshAI/r6wfuAKmVb` at
`6dbff965ffdf5b7b1e668759d717fc161ee0a793`.

- Judged file paths: 18
- Judged paths present in candidate: 18
- Missing judged paths: 0
- Byte-identical judged files: 16
- Additively changed metadata/navigation files: `README.md`, `logbook.json`

All six historical Markdown pages are byte-identical:

- `pages/index.md`
- `pages/overview/page.md`
- `pages/claims/page.md`
- `pages/evidence/page.md`
- `pages/conclusion/page.md`
- `pages/verification-run/page.md`

All old static assets are also byte-identical. The modified Space README keeps
its original title and Trackio description under a new historical heading.
`logbook.json` retains the complete old page hierarchy under the child titled
exactly **Historical rejected baseline** and adds the current verifier first.

The protected judged manifest remains available at
`evidence/startup/judged_space_manifest.sha256`.
