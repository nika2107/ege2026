from functools import *
@lru_cache(None)
def f(n):
    if n == 1: return 1
    if n > 1: return (3 * n + 5) * f(n - 1)
for i in range(1, 10000):
    f(i)
print(f(2073)//f(2070))