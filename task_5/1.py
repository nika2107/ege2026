for N in range(1, 30):
    N_bin = f'{N:b}'
    if N % 3 == 0:
        N_bin += N_bin[-3:]
    else:
        N_bin += f'{((N % 3) * 3):b}'
    R = int(N_bin, 2)
    if R >= 200:
        print(N)
        break


for N in range(1, 30):
    N_bin = f'{N:b}'
    remainder = N % 3
    if remainder == 0:
        N_bin += N_bin[-3:]
    else:
        N_bin += f'{(remainder * 3):b}'
    R = int(N_bin, 2)
    if R >= 200:
        print(N)
        break