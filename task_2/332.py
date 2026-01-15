from itertools import *

def F(x, y, z, w):
    return (x or y and not z) and not w

table = [(1, 0, 0, 0,), (0, 0, 1, 0), (0, 1, 0, 1)]
if len(set(table)) == len(table):
    for i in permutations('xyzw'):
        if [F(**dict(zip(i, r))) for r in table] == [1, 1, 0]:
            print(*i, sep='')
#4