from math import *
for L in range(1, 100_000):
    N = 10 + 26 + 34
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if 1142 * I > 305 * 2**10:
        print(L)
        break