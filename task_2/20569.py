from itertools import *

def F(x, y, z, w):
    return ((w <= z) == (x <= (not y))) and (x or z)

for a1, a2 in product([0, 1], repeat = 2):
    table = [(1, 0, 0, 1), (1, 1, 1, 0), (0, a1, 0, a2)]
    if len(set(table)) == len(table):
        for i in permutations('xyzw'):
            if [F(**dict(zip(i, r))) for r in table] == [1,0,1]:
                print(*i, sep='')
