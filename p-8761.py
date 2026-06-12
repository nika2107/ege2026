from itertools import *

alph = sorted('ПОЛЕНИЦА')

for pos, val in enumerate(product(alph, repeat = 5), start = 1):
    val = ''.join(val)
    if pos % 2 == 1 and val[0] != 'А' and val [-1] != 'А' and val.count('Л') >= 3:
        print(pos)
        break
