from itertools import *
def F(x, y, z, w):
    return ((x or y) <= z) or (y == w) or z

for a1, a2, a3, a4 in product([0,1], repeat = 4):
    table = [(0, 1, a1, a2), (1, a3, 1, 0), (a4, 1, 1, 0)]
    if len(set(table)) == len(table):
        for i in permutations('xyzw'):
            if [F(**dict(zip(i,r))) for r in table] == [0,0,0]:
                print(*i, sep='')

