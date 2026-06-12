from string import *
from itertools import *

cnt = 0
for val in product(printable[:12], repeat = 5):
    val = ''.join(val)
    if val[0] != '0':
        for i in '13579b':
            val = val.replace(i, '*')
        if sum(val[i] == '*' and val[i+1] == '*' for i in range(4)) <=2:
            cnt += 1
print(cnt)

