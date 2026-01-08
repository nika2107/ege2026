def F(a, x, y):
    return (x > a) or ( y > a) or ((x + 2*y) < 110)
for a in range(0,1000):
    if all(F(a, x, y) for x in range(0,1000)\
    for y in range(0,1000)):
        print(a)