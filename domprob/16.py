from functools import *

@lru_cache(None)
def F(n):
    if n <= 7: return n
    return G(n - 3) * 3

@lru_cache(None)
def G(n):
    if n <= 7: return n
    return G(n - 1) + 4

for i in range(1, 200000):
    F(i)
for i in range(1, 200000):
    G(i)

print(F(43000))


