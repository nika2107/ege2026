num =

cnt = 0
while num:
    if num % 125 <= 37:
        cnt += 1
    num //= 125
print(cnt)