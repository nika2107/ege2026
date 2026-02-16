cnt = 0

for n in range(699999, 1, -1):
    summa = 0
    kolvodelit = 0

    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            summa += d
            kolvodelit += 1
            if d != n // d:
                summa += n // d
                kolvodelit += 1

    if kolvodelit == 0:
        M = 0
    else:
        M = summa // kolvodelit

    if M % 1000 == 313:
        print(n, M)
        cnt += 1
        if cnt == 7:
            break