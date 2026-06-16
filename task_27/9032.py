from math import *

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]


with open(r'.\files\27-122a.txt') as file:
    dots = []
    stars = []
    for i in file:
        X, Y, info = i.replace(',', '.').split()
        dots.append([float(X), float(Y)])
        if info[0] == 'L' and info[1] == '3':
            stars.append([float(X), float(Y)])

cluster_1 = [d for d in dots if d[1] < 8]
cluster_2 = [d for d in dots if 8 < d[1]]

stars_1 = [d for d in stars if d[1] < 8]
stars_2 = [d for d in stars if 8 < d[1]]

center_1 = center(cluster_1)
center_2 = center(cluster_2)

if len(cluster_1) < len(cluster_2):
    small_center = center_1
    big_center = center_2
else:
    small_center = center_2
    big_center = center_1

A1 = max(dist(small_center, s) for s in stars)
A2 = max(dist(big_center, s) for s in stars)

print(int(A1 * 10_000), int(A2 * 10_000))

#73624 70820

