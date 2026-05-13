ans = []
for x in range(1, 1000):
    P = 25 <= x <= 64
    Q = 40 <= x <= 115
    A = False
    F = P <= ((Q and not A) <= (not P))
    if F == 0:
        ans.append(x)
print(ans[-1] - ans[0])