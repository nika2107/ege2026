from math import *

f = open('27_A_28946(1).txt')

cl1 = []
cl2 = []

for i in f:
    a = i.split()
    x,y = float(a[0]), float(a[1])
    if x > 15:
        cl2.append([x, y])
    if x < 15:
        cl1.append([x, y])

def center(cl):
    rast = []
    for i in cl:
        s = 0
        for j in cl:
            d = dist(i, j)
            s += d
        rast.append([s, i])
    return min(rast)[1]

x1, y1 = center(cl1)
x2, y2 = center(cl2)

