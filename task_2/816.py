from itertools import *

def F(x, y, z):
    return not(x == (y <= z))

table = [(0,0,1), (0,1,1)]
if len(set(table)) == len(table):
    for i in permutations('xyz'):
        if [F(**dict(zip(i,r))) for r in table] == [1,0]:
            print(*i, sep='')