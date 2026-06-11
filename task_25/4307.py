from fnmatch import fnmatch

for x in range(68, 10**9 + 1, 68):
    if fnmatch(str(x), '12345?7?8'):
        print(x, x//68)