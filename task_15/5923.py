from itertools import combinations
def f(x):
    P = 5 <= x <=280
    Q = 295 <= x <= 400
    R = 375 <= x <= 450
    A = A1 <= x <= A2
    return (Q <= P) or (not A) <= R

lineA = sorted([5, 280, 295, 400, 375, 450])
linex = [6, 281, 296, 401, 376, 451]

ans = []
for A1, A2 in combinations(lineA, 2):
    if all(f(x) for x in linex):
        ans.append(A2 - A1)

print(min(ans))

#80