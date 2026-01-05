from itertools import  *

def F(x, y, z, w):
    return (x == (not y)) <= ((x and w) == (z and(not w)))

for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat = 6):
    table = [(1, 1, a1, 1), (a2, 1, 1, a3), (0, a4, a5, a6)]
    if len(set(table)) == len(table):
        for i in permutations('xyzw'):
            if [F(**dict(zip(i, r))) for r in table] == [0,0,0]:
                print(*i, sep='')

