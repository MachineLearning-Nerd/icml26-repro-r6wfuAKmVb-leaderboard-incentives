# Claim 5 method

Use the continuous family `v(theta,e)=1-1/(2+e+theta)`. It has generalized
parameters `U=1`, `L=theta/(1+theta)`, `alpha=-log(1+theta)`, and `beta=1`.
For capabilities one and zero, the lower model beats the higher model at a
common TbT baseline `D` iff its additional effort is strictly greater than one.
Thus the required-effort infimum is exactly one for every `D`. With linear cost
and reward gap two, no stabilizing threshold exists. Z3 checks the cancellation
for arbitrary nonnegative `D`.
