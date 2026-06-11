for N in range(1, 1000):
    R = f'{N:b}'
    if sum(map(int, R)) % 2 == 0:
        R += '0'
        R = '10' + R[2:]
    else:
        R += '1'
        R = '11' + R[2:]
    res = int(R, 2)
    if res <= 19:
        ans = N
print(ans)


