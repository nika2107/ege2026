with open(r'.\files\17_9748.txt') as file:
    data = [int(i) for i in file]

max_15 = 0
for i in data:
    if i % 100 == 15 and i > max_15:
        max_15 = max(max_15, i)

cnt = 0
max_summa = 0

for i in range(len(data) - 2):
    cnt_four = 0
    if 1000 <= data[i] <= 9999: cnt_four += 1
    if 1000 <= data[i + 1] <= 9999: cnt_four += 1
    if 1000 <= data[i + 2] <= 9999: cnt_four += 1

    if cnt_four == 1:
        s = data[i] + data[i + 1] + data[i + 2]
        if s >= max_15:
            cnt += 1
            if s > max_summa:
                max_summa = s

print(cnt, max_summa) #299 196183


#############################################

with open(r'.\files\17_9748.txt') as file:
    data = [int(i) for i in file]


max_15 = max(i for i in data if i % 100 == 15)

ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = len(str(num1)) == 4
    u2 = len(str(num2)) == 4
    u3 = len(str(num3)) == 4
    if u1 + u2 + u3 == 1 and sum([num1, num2, num3]) >= max_15:
        ans += [num1 + num2 + num3]

print(len(ans), max(ans))  #299 196183