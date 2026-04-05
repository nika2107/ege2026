with open(r'.\files\17_9786.txt') as file:
    data = [int(i) for i in file]

max_25 = 0
for i in data:
    if abs(i) % 100 == 25 and i > max_25:
        max_25 = i

cnt = 0
max_sum = -10 ** 10

for i in range(len(data) - 2):
    sum_3 = data[i] + data[i + 1] + data[i + 2]
    cnt_u = 0
    if 1000 <= abs(data[i]) <= 9999: cnt_u += 1
    if 1000 <= abs(data[i + 1]) <= 9999: cnt_u += 1
    if 1000 <= abs(data[i + 2]) <= 9999: cnt_u += 1

    if cnt_u <= 2 and sum_3 <= max_25:
        cnt += 1
        if sum_3 > max_sum:
            max_sum = sum_3

print(cnt, max_sum) #6315 84523
