def F(A, x, y):
    return (x > 67)or(y >= x) or (3*x - y < A)

for A in range(0,1000):
    if all(F(A, x, y) for x in range(0, 1000)\
    for y in range(0, 1000)):
        print(A)