def d(n, m):
    return n % m == 0

for A in range(1000, 0, -1):
    if d(70, A):
        if all(d(x, A) or not d(x, 18) or not d(x, 42) for x in range(1, 10000)):
            print(A)
            break