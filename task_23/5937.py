def f(x, y, cnt):
    if x % 2 == 0: cnt += 1
    if x == y and cnt <= 15: return 1
    if x > y or cnt > 15: return 0
    if x < y: return f(x + 2, y, cnt) + f(x + 3, y, cnt) + f(x * 2 + 1, y, cnt)

print(f(1, 55, 0))

#4197234