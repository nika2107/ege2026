def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num **.5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    d = set()
    for i in range(2, int(num **.5) + 1):
        if num % i == 0:
            if is_prime(i): d |= {i}
            if is_prime(num // i): d |= {num // i}
    if len(d) >= 4:
        d = sorted(d)
        M = d[0] + d[1] + d[-1] + d[-2]
        return M
    return 0

cnt = 0
for N in range(456789 + 1, 10 ** 20):
    M = f(N)
    if M and M % 114 == 39:
        cnt += 1
        print(N, M)
        if cnt == 5:
            break
