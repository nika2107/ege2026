f = open('files/26_4712.txt')
data = list(map(int, f.read().split()))

n = data[0]
a = data[1:]

box = [0] * 10004

for x in a:
    box[x] = 1
dp = [0] *10004
mx = [0] * 10007

for x in range(10000, 0, -1):
    if box[x]:
        dp[x] = 1 + mx[x + 3]
    mx[x] = max(mx[x + 1], dp[x])

ko1 = max(dp)

for x in range(10000, 0, -1):
    if dp[x] == ko1:
        print(ko1, x)
        break
