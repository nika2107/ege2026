from functools import *

def F(n):
    return G(n -1)

@lru_cache(None)
def G(n):
     if n <= 9: return 3 * n
     if n > 9: return G(n - 2)

for i in range(1, 48000):
    G(i)
print(F(47995))