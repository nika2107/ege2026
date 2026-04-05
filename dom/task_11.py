from math import *
for L in range(1, 100000):
    N = 8164 + 36
    i = ceil(log2(N))
    I = ceil(L * i/8)
    if 835 * I > 156 * 2**10:
        print(L)
        break