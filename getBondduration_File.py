import numpy as np
#getBondduration

def getBondDuration(y, face, couponRate, m, ppy=1):
    n = m * ppy
    c = face * couponRate / ppy
    t = np.arange(1, n + 1)
    discount_factors = (1 + y/ppy) ** -t
    cash_flows = np.full(n, c)
    cash_flows[-1] += face
    pv_cf = cash_flows * discount_factors
    w = pv_cf / np.sum(pv_cf)
    weighted_times = w * t
    duration = np.sum(weighted_times)
    return duration

# Test values
y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 2

# Calculate bond duration
duration = getBondDuration(y, face, couponRate, m, ppy)
print(f"The bond duration is: {duration:.2f}")