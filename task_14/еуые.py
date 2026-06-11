num = 343**1515 - 6*49**1520 + 5*49**1510 - 3*7**1530 - 1550
cnt_0 = 0
while num:
   if num % 7 == 0:
       cnt_0 += 1
   num //= 7
print(cnt_0)