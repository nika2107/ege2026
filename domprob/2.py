from itertools import *

def f(x, y, w, z):
    return (z <= (x == w)) or not(y <= w)

for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat = 7):
    table = [(a1, 0, a2, 0),(0, a3, a4, 0),(1, a5, a6, a7)]
    if len(set(table)) == len(table):
        for i in permutations('xyzw'):
            if [f(**dict(zip(i, r))) for r in table] == [0, 0, 0]:
                print(*i, sep = '')