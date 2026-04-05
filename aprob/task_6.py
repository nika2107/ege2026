from turtle import *
screensize(2500,2500)
tracer(0)
m = 15
rt(90)

for i in range(2):
    fd(1 * m)
    lt(270)
    fd(16 * m)
    rt(90)
up()

bk(4 * m)
rt(90)
fd(10 * m)
lt(90)

down()

for i in range(2):
    fd(17 * m)
    rt(90)
    fd(7 * m)
    rt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(5, 'red')
update()
done()
