def f(x, s):
    if x <= 15: return s % 2 == 0
    if s == 0: return False
    h = [f(x - 3, s - 1),
         f(x - 8, s - 1),
         f(x // 3, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)

print('19:', [x for x in range(16, 10000) if f(x, 2)]) #[48, 49, 50]
print('20:', [x for x in range(16, 10000) if f(x, 3) and not f(x, 1)]) #[51, 52, 53, 56, 57, 58, 144, 145, 146, 147, 148, 149, 150, 151, 152]
print('21:', [x for x in range(16, 10000) if f(x, 4) and not f(x, 2)]) #[54, 55, 59, 60, 61, 153, 154, 155]