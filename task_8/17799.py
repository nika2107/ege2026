from itertools import *
alph = sorted('АРГУМЕНТ')
cnt = 0

for pos, val in enumerate(product(alph, repeat = 4), start = 1):
    cnt += 1
    val = ''.join(val)
    if len(set(val)) == 4 and val == ''.join(sorted(val)):
        ans = cnt
print(ans)
