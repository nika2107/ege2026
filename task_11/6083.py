from math import *
L = 196
N = 1550 + 10
i = ceil(log2(N))
I = ceil(L * i / 8)

print(((604 * 2**10) // 2048) - I)