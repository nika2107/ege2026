ans = []
for n in range(1, 1000):
    r = f'{n:b}'
    if sum(map(int, r)) % 2 == 0: r = '10' + r
    else:  r = '01' + r + '1'
    if n > 18:
     res = int(r, 2)
     ans.append(res)
print(min(ans))


