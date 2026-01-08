from itertools import *

graph = 'ГБ БА АД ДЕ ЕВ ВБ ВД'.split()
matrix = '245 136 25 15 134 2'.split()

print(*range(1, 7 ))
for i in permutations('АБВГДЕ'):
    if all(str(i.index(x) + 1)in matrix[i.index(y)] for x, y in graph):
        print(*i)
