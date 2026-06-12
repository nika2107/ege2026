from functools import *
from sys import *

setrecursionlimit(10**9)
@lru_cache(None)
def f(n):
    if n < 17: return 6
    if n >= 17: return (n + 5) * f(n - 9)

print((f(234561)//436 + f(234552)//218)//f(234534))