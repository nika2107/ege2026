def convert(num):
    res = ''
    while num != 0:
        res += str(num % 3)
        num //= 3
    return res[::-1]

ans = []
for N in range(1, 1000):
    R = convert(N)
    if N % 3 == 0:
        R += R[-2:]
    else:
        s = sum(map(int,R)) * 2
        R += convert(s)
    res = int(R, 3)

    if res > 520 and res % 2 == 1:
        ans.append(res)
print(min(ans))