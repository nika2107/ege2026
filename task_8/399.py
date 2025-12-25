from itertools import permutations

cnt = 0
for val in set (permutations('ВОРОТА', r = 6)):
    val = ''.join(val)
    cnt += 1
    if val[0] != ''
print(cnt)