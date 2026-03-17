from itertools import *

def f(x, y, z, w):
    return (not z and y and x and not w) or (not z and y and not x and not w) or (z and y and x and not w)
for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat = 7):
    table = [(a1, 1, a2, a3),
             (a4, 0, 1, a5),
             (0, a6, 0, a7)]
    if len(set(table)) == len(table):
        for i in permutations('xyzw'):
            if [f(**dict(zip(i, r))) for r in table] == [1, 1, 1]:
                print(*i, sep = '')



