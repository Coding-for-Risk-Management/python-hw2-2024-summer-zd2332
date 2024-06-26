import numpy as np
# getBondprice
def getBondPrice(y, face, couponRate, m, ppy=1):
    n = m * ppy
    c = face * couponRate / ppy
    discount_factors = np.array([(1 + y/ppy)**(-t) for t in range(1, n + 1)])
    pv_coupons = c * discount_factors
    pv_face = face * discount_factors[-1]
    bond_price = np.sum(pv_coupons) + pv_face
    return bond_price

# Test values
y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 2
bond_price = getBondPrice(y, face, couponRate, m, ppy)
print(f"The bond price is: ${bond_price:.2f}")
