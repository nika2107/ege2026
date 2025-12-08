from string import printable

def most_num (data):
    most = []
    for i in data:
        most.append([data.count(i), i])
    return int(max(most)[1])

for x in printable [1:35]:
    num1 = int(f'6{x}QR{x}', 35)
    num2 = int(f'{x}59SH', 35)
    num3 = int (f'PH{x}69YW', 35)
    num = num1 + num2 + num3
    if num % most_num(str(num)) == 0:
        print( num // most_num(str(num)))

