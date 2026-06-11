ans = []
for n in range(1, 1000):
    r = f'{n:b}'
    if n % 3 == 0:
        r += r[-3:]
    else:
        r =  r + f'{(n % 3) * 3:b}'
    res = int(r, 2)
    ans.append([abs(res - 130), -n, n, res])
ans.sort()
print(ans[0][2])
