cnt = 0

for n in range(800001, 10 ** 10):
    for d in range(19, n, 10):
        if n % d == 0:
            print(n, d)
            cnt += 1
            break
    if cnt == 5:
        break

####################################################

def f(num):
    d = set()
    for i in range(2, int(num **.5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    for i in sorted(d):
            if i % 10 == 9 and i != 9:
                return i
    return 0

cnt = 0
for N in range (800001, 10 ** 10):
    if M := f(N):
        print(N, M)
        cnt += 1
        if cnt == 5: break
