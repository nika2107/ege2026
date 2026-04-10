from itertools  import *

cnt = 0

for num in product(range(7), repeat = 5):
    if num[0] == 0:
        continue
    if num.count(0) == 1 and num.count(1) <= 2:
        cnt += 1

print(cnt)