from itertools import *

cnt = 0
for val in set (permutations('ШКОЛА', r = 5)):
    val = ''.join(val)
    cnt += 1
    if val == 'ШАЛАШ':
        print(cnt)