from turtle import *
screensize(2500,2500)
tracer(0)
m = 15

for i in range(4):
    fd(10 * m)
    rt(270)
up()

fd(3 * m)
rt(270)
fd(5 * m)
rt(90)

down()

for i in range(2):
    fd(10 * m)
    rt(270)
    fd(12 * m)
    rt(270)

up()

for x in range(0, 14):
    for y in range(0, 18):
        goto(x * m, y * m)
        dot(5, 'red')
update()
done()