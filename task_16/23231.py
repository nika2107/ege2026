def G(n):
    if n <= 7:
        return n
    return 4*n - 21

def F(n):
    if n <= 7:
        return n
    return 3 * G(n - 3)

print(F(43000))
