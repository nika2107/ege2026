from functools import *

@lru_cache(None)
def f(n):
    if n< 10: return 3
    if n >= 10: return (n + 4)*f(n - 5)

for i in range(100000,1, -1):
    f(i)
print((f(257487)//683 + 67 * f(257477))//f(257472))