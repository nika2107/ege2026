from itertools import *

def F(a, b, c, d):
    return (not a and not b) or (b == c) or d

for x1, x2, x3, x4 in product([0, 1], repeat = 4):
    table = [(x1, x2, 1, x3), (1, 0, x4, 1), (0, 0, 1, 1)]
    if len(set(table)) == len(table):
        for i in permutations('abcd'):
            if [F(**dict(zip(i, r))) for r in table] == [0,0,0]:
                print(*i, sep='')

#cdba