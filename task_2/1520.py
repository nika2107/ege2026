from itertools import *

def F(a, b, c):
    return(a <= b) and ((a and b) <= (not c))

table = [
    (0, 0, 0),
    (0, 0, 1),
    (0, 1, 0),
    (0, 1, 1),
    (1, 0, 0),
    (1, 0, 1),
    (1, 1, 0),
    (1, 1, 1)
]
if len(set(table)) == len(table):
    for i in permutations('abc'):
        if [F(**dict(zip(i, r))) for r in table] == [1, 0, 1, 1, 1, 0, 1, 0]:
            print(*i, sep='')