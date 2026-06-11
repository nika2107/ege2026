with open(r'.\files\24_23281.txt') as file:
    data = file.readline()

data = data.replace('2025', '***5')

ans = 0

for i in range(len(data)):
    for j in range(i + ans, len(data) + 1):

        s = data[i:j]

        if s.count('Y') > 80:
            break

        if s.count('Y') == 80 and s.count('*') >= 90:
            ans = max(ans, len(s))

print(ans)