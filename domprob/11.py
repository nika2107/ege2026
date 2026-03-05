from math import *
for L in range(1, 100_000):
    N = 10 + 26 + 8164
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if 835 * I > 156 * 2**10:
        print(L)
        break