def f(x, y):
    if x == y: return 1
    if x == 30: return 0
    if x > y: return 0
    if x < y: return f(x + 1, y) + f(x * 2, y) + f(x * 3, y)

print(f(10, 60) * f(60, 70))