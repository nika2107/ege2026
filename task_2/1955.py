from itertools import *

def F(x, y, z, w):
    return not(y <= (x == w)) and (z <= x)

for a1, a2, a3, a4, a5 in product([0, 1], repeat = 5):
    table = [(a1, 1, 1, a2), (0, a3, a4, 0), (a5, 0, 1, 0)]
    if len(set(table)) == len(table):
        for i in permutations('xyzw'):
            if [F(**dict(zip(i, r))) for r in table] == [1, 1, 1]:
                print(*i, sep = '')



