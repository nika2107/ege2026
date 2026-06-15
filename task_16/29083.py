from sys import *
def f(n):
    if n < 17: return 6
    return (n + 5) * f(n - 9)
setrecursionlimit(10**5)
print((f(234561)//436 + f(234552)//218)//f(234534))