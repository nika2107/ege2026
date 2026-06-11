def convert(num):
    res = ''
    while num != 0:
        res += str(num % 3)
        num //= 3
    return res[::-1]

ans = []
for n in range(1, 1000):
    r = convert(n)
    if n % 3 == 0:
        r = '1' + r + r[-2:]
    else:
        s = sum(map(int, r)) * 5
        r += convert(s)
    res = int(r, 3)
    ans.append([abs(res - 1000), res, n])
ans.sort()
print(ans[0][1])