otvet = []
for x in range (1, 150) :
    C = 48 <= x <= 94
    J = 83 <= x <= 100
    A = True
    F =(not (C or J)) <= (not A)
    if F == 1:
        otvet.append(x)
print(otvet[-1] - otvet[0])
