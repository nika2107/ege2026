otvet = []
for x in range(1,150):
    P = 15 <= x <= 40
    Q = 21 <= x <= 63
    A = False
    F = P <= ((Q and (not A)) <= (not P))
    if F == 0:
        otvet.append(x)
print(otvet[-1] - otvet[0])