def f(A, x):
    return (x % 2 == 0) <= (not(x % 3 == 0)) or (x + A >= 100)

for A in range(1, 1000):
    if all(f(A, x) for x in range(1,1000)):
        print(A)
        break
#94