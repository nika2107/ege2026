from fnmatch import *
for x in range(12001506 - 120001506 % 271, 10**8 + 1, 271):
    if fnmatch(str(x), '12??15*6'):
        print(x, x // 271)