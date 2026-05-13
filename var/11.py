from math import *
L = 289
N = 10 + 1015
i = ceil(log2(N))
I = ceil(L * i/8)

print(I * 524288/2**20)
