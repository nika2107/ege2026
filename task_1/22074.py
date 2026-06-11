from itertools import *
graph = 'ЖА АБ БВ ВД ДЖ БГ ГЕ ЕВ ЕЖ'.split()
matrix = '347 456 156 12 23 237 16'.split()

print(*range(1, 8))
for i in permutations('АБВГДЕЖ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)