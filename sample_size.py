"""
Compute sample size using Hoeffding's inequality.

[Hoeffding's inequality](https://en.wikipedia.org/wiki/Hoeffding%27s_inequality)
Let X1, ..., Xn be independent random variables bounded by the interval [0, 1].
We define the empirical mean of these variables by
Sn = 1/n(X1+ ... +Xn)
Hoeffding's inequality ==> P(|Sn - E(Sn)| > epsilon) < 2exp(-2epsilon^2*n), epsilon > 0.
Let gamma > 0,
so: P(|Sn - E(Sn)| > epsilon) < gamma <==> n > [-ln(gamma/2)]/[2*epsilon^2]
n = sample size.

Example:
sample_size(0.08, 0.01) = 16094
sample_size(0.001, 0.001) = 3800451

Author: [SofianeHADDADI](https://github.com/SofianeHADDADI)
"""

import numpy as np

def sample_size(gamma, epsilon):
    n = (-np.log(gamma/2))/(2*epsilon*epsilon)
    return int(n)
