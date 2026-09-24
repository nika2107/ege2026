a = int(input('Введите A: '))
m = int(input('Введите m: '))
s = ''
while a > 0:
    s = str(a % m) + s
    a = a // m

print(s)
