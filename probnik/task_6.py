from turtle import *

screensize(1500,1500)
tracer(0)
m = 15
rt(90)

for i in range(2):
    fd(14 * m)
    lt(270)
    bk(12 * m)
    rt(90)
up()

fd(9 * m)
rt(90)
bk(7)
lt(90)

down()

for i in range(2):
    fd(13 * m)
    rt(90)
    fd(6 * m)
    rt(90)
up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(5, 'red')

update()
done()

#279