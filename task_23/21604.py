def f(x, y):
    if x == y: return 1
    if x < y: return 0
    if x == 24: return 0
    if x > y: return f(x - 1, y) + f(x - 4, y) + f(x // 2, y)

print(f(34, 30) * f(30, 20) * f(20, 9))