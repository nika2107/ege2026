def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num **.5) + 1):
        if num % i == 0:
            return False
    return True

def odna_5(num):
    return str(odna_5).count('5') == 1

def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2
    i = 3
    while i * i <= num:
        while num % i == 0:
            d += []