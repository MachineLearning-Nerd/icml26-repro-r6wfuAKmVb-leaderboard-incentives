# Claim 6 — BLOCKED

**Exact empirical contract.** Figure 1 and Section 5.1 describe Qwen2.5 models
of 0.5B, 1.5B, 3B, 7B, and 14B, Winogrande LoRA post-training from zero to
3,000 steps with batch size eight, and fitted generalized scaling curves. At
TbT 3,000, the reported minimum adjacent additional effort is 384,668 steps.

## Four verification routes

1. **Direct vector reconstruction.** The unique right-panel red path in the
   hashed PDF source has 31 points. Calibrating only from its seven x-axis and
   nine y-axis ticks gives `384667.5594951132`, which rounds to `384668`.
2. **Endpoint-blind extrapolation.** A degree-six fit selected before revealing
   the last point and trained on the preceding 30 vector points predicts
   `384648.7961118833`, relative error `4.88e-5`.
3. **Independent text anchors.** The same `384668` statement appears once each
   in `Sections/equilibrium.tex`, `Sections/introv2.tex`, and
   `Sections/tune-before-test.tex`.
4. **Dedicated falsification search.** No alternate red curve, coordinate
   contradiction, or inconsistent axis mapping was found. This did not produce
   a valid counterexample.

**Negative control.** Mutating the top y-axis label from 400,000 to 350,000
decodes 336,584.115 and fails the 384,668 check.

## Why the verdict is BLOCKED

These routes verify the published display, not its empirical provenance. The
arXiv source contains no raw per-checkpoint Winogrande measurements, fit
parameters, training code, or checkpoints. A fresh CPU-only five-model
fine-tuning run would not recover the undisclosed measurements or fit choices.
The empirical claim therefore cannot be independently VERIFIED or FALSIFIED.

**Evidence.** [Figure verifier](/repro/src/claim6_figure.py);
[independent checker](/repro/src/check_claim6.py);
[raw reconstruction](/outputs/claim6_reconstruction.json);
[contract](/evidence/claim_6/claim_contract.json);
[source audit](/evidence/claim_6/source_audit.md);
[checker PASS](/evidence/claim_6/checker_output.txt);
[negative control](/evidence/claim_6/negative_control_output.txt);
[limitations](/evidence/claim_6/limitations.md).

Source bundle SHA-256:
`9f6d8668713011bee867b6c83a8e88a5f6b9cec201cc1806a30c891b11106ae8`.
Figure SHA-256:
`aa814bc7a08fe91b8ecc7ef5d0e079dea28fd9aa74b8cb6107c6d76608078032`.
Tested SHA: `8f8494d23146f77a0ed25520f32e9574df9e43be`.

Unblocker: author per-checkpoint measurements and fit configuration, or
published CPU-feasible logits/checkpoints sufficient to recreate them.
