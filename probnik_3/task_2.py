from itertools import *
def f(x, y, z, w):
    return ((z == x) <= w) and (w <= ( y and x))

for a1, a2, a3 in product([0,1], repeat = 3):
    table = [(1, 1, a1, 0), (1, a2, a3, 0), (1, 0, 1, 1)]
    if len(set(table)) == len(table):
        for i in permutations('xyzw'):
            if [f(**dict(zip(i, r))) for r in table] == [1, 1, 1]:
                print(*i, sep='')