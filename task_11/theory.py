from math import *
# 1855
L = 101
N = 10 + 4090
i = ceil(log2(N)) #byte
I = ceil(L * i / 8) # из бит в байты => в большую

print(I * 2048 / 1024)


#23270
for L in range(1, 100_000):
    N = 10 + 27
    i = ceil(log2(N)) #byte
    I = ceil(L * i / 8) # из бит в байты => в большую
    if 3548 * I > 12 * 2**10:
        print(L)
        break


#23195
for N in range(1, 100000):
    L = 172
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if 356_984 * I >= 54 * 2 ** 20:
        print(N)
        break