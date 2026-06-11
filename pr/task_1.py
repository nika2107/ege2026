from itertools import *

graph = 'DC CF FG GE EA AD DB BC BH HG HA '.split()
matrix = '346 348 12 127 678 15 458 257'.split()

print(*range(1, 9))
for i in permutations('ABCDEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

#47