from turtle import *
screensize(2000, 2000)
tracer(0)
m = 15
rt(90)

for i in range(5):
    fd( 31 * m)
    rt(90)
    fd(46 * m)
    rt(90)

up()

fd(19 * m)
rt(90)
fd(17 * m)
lt(90)

down()

for i in range(5):
    fd(34 * m)
    rt(90)
    fd( 15 * m)
    rt(90)

up()
for x in range(-29,-13):
    for y in range(-12, 1):
        goto(x * m, y * m)
        dot(3, 'red')
update()
done()

