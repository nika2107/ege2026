from functools import *
@lru_cache(None)
def F(n):
    return G(n - 3)

@lru_cache(None)
def G(n):
    if n <= 20:
        return n
    if n > 20:
        return G(n - 2) + 1
for i in range(1, 3000):
    F(i)
print(F(25000))