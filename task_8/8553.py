from itertools import *
alph = sorted ('НОРМАЛЬЕ')
cnt = 1
for pos, val in enumerate(product(alph, repeat = 6),start = 1):
     val = ''.join(val)
     if val [:4] == 'НОРМ':
         print(val,cnt)
     if val [:6] == 'НЕНОРМ':
         print(val,cnt)

     cnt += 1
print(cnt)
print(154817-137588-1) #17228