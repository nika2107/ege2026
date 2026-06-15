from math import *

L = 23
N = 26 + 26 + 10 + 25
i = ceil(log2(N))
I = ceil(L * i / 8) + 15

print(3 * 2**20/I)
