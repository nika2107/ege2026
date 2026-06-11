from functools import *
@lru_cache(None)
def f(n):
    if n < 110: return n
    if n >= 110: return (n - 7) * f(n - 8)

for i in range(1, 100000):
    f(i)

print((f(74914) - f(74898))//(16 * f(74890)))