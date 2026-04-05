m = []

for x in range(1, 2031):
    num = 6**2030 + 6**100 - x
    cnt = 0
    while num > 0:
        if num % 6 == 0: cnt += 1
        num = num // 6
    m.append(cnt)
print(min(m))