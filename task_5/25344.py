import sys
from string import printable
def convert(num,sys):
    res = ''
    while num == 0:
        res += printable[num % sys]
        num //= sys
        return res[::-1] if res else '0'

ans = []
for N in range (0, 300):
    if N % 3 == 0:
        R = R + R[-2:]
    else:
        sum_d = sum(map(int, R))
        R += convert(sum_R * 3)
    R = int(R, 3)
    if R > 208 and R % 2:
        print(R)
        break

