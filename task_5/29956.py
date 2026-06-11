from string import printable as alph
def convert(num, sys):
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1] if res else '0'

for N in range(1, 10000):
    R = convert(N, 3)
    if N % 3 == 0:
        R = '1' + R +'02'
    else:
        R += convert((N % 3) * 5, 3)

    R2 = int(R, 3)

    if R2 >= 177:
        print(N)
        break