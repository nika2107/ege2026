def convert(num):
    res = ''
    while num != 0:
        res += str(num % 3)
        num //= 3
    return res[::-1]

ans = []
for n in range(1, 10000):
    r = convert(n)
    if n % 3 == 0:
        s = sum(map(int, r)) * 8
        r += convert(s)
    if n % 3 != 0:
        r = '1' + r + r[-3:]

    res = int(r, 3)
    ans.append([abs(res - 1220), res, n])
ans.sort()
print(ans[0][1])


