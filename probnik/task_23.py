def F(x, y):
    if x < y or x == 13:
        return 0
    if x == y or x == 6:
        return 1
    return F(x -1, y) + F(x - 2, y) + F(x // 3, y)

print(F(19,4))