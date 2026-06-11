from itertools import *
def f(x, y, z, w):
    return not(w <= (x == y)) and (z <= x)

for a1, a2, a3, a4, a5 in product([0, 1], repeat = 5):
    table = [(a1, 0, 1, 0), (0, a2, a3, 0), (a4, 1, 1, a5)]
    if len(set(table)) == len(table):
        for i in permutations('xyzw'):
            if [f(**dict(zip(i, r))) for r in table] == [1, 1, 1]:
                print(*i, sep='')

#yxwz