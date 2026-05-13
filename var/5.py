for N in range(1, 10_000):
    R = f'{N:b}'
    R += str(sum(map(int, R)) % 2)
    R += str(sum(map(int, R)) % 2)
    R_10 = int(R,2)

    if R_10 > 253:
        print(N)
        break

