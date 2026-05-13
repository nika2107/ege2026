from itertools import *
graph = 'АБ БД ДК КЕ ЕВ ВА ВБ ДГ ГЕ ГК'.split()
matrix = '457 346 24 123 167 257 156'.split()

print(*range(1, 8))
for i in permutations('АБВГДЕК'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

