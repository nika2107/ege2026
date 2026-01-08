from itertools import *
def F(x, y, z, w):
    return (z <= y) or ((w <= x) <= y)
for a1, a2, a3, a4, a5, a6 in product([0,1], repeat = 6):
    table = [(a1, 0, 0, a2), (a3, a4, 1, a5), (a6, 1, 1, 1)]
    if len(set(table)) == len(table):
        for i in permutations('xyzw'):
            if [F(**dict(zip(i, r))) for r in table] == [0, 0, 0]:
                print(*i, sep='')
#ywxz