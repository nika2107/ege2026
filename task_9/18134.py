cnt = 0

with open('9.txt') as f:
    for line in f:
        a = list(map(int, line.split()))

        b = []
        c = []

        for x in a:
            if a.count(x) == 2 and x not in b:
                b.append(x)
            if a.count(x) == 1:
                c.append(x)

        if len(b) == 2 and len(c) == 2:
            if max(b) ** 2 > c[0] * c[1]:
                cnt += 1

print(cnt)