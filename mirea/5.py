n = int(input('Введите число: '))
k = 0

for i in range(1, n + 1):
    if n % i == 0:
        k = k + 1
if k == 2:
    print('Число простое')
else:
    print('Число не простое')