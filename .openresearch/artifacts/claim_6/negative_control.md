# Claim 6 negative control

The verifier mutates the labeled y-axis maximum from 400,000 to 350,000. The
same vector endpoint then decodes to about 336,584 rather than 384,668, and the
claim check must fail. This demonstrates that the extractor uses the axis
calibration rather than hard-coding the paper number.
