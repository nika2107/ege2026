ans = 10000

for x in range(1, 2030):
    num = 6**2030 + 6**100 - x
    cnt = 0
    while num > 0:
        if num % 6 == 0:
            cnt += 1
        num //= 6
    ans = min(ans, cnt)
print(ans)
