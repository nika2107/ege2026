for x in range(1, 5556):
    num = 5**150 + 5**135 - x
    s = ''
    while num > 0:
        s = str(num % 5) + s
        num //= 5
    if s.count('4') == 134:
        print(x)
        
