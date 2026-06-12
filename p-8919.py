ans = 0

for x in range(1, 3000):
    num = 12*19**12 + 9*19**9 + 5*19**5 - x

    cnt = 0
    while num > 0:
        if num % 19 == 0:
            cnt += 1
        num //= 19
    if cnt % 2 == 0:
        ans += x
print(ans)