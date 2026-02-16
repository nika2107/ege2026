from fnmatch import fnmatch

for N in range(1, 10**8):
    if fnmatch(str(N), '1234*7') and N %141 == 0:
        print(N, N//141)