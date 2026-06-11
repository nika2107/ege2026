from itertools import *
def f(x, y, z, w):
    return ((x <= w) or y and not z) and ((y <= (not z)) or x and not w)

for a1, a2, a3, a4, a5 in product([0, 1], repeat = 5):
    table = [(a1, 0, 0, a2), (a3, 0, a4, 0), (0, 0, 0, a5)]
    if len(set(table)) == len(table):
        for i in permutations('xyzw'):
            if [f(**dict(zip(i, r))) for r in table] == [0, 0, 0]:
                print(*i,sep = '')

