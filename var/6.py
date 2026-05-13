from turtle import *
screensize(1000, 1000)
tracer(0)
m = 15


rt(315)
for i in range(7):
    fd(12 * m)
    rt(45)
    fd(6 * m)
    rt(135)
up()

for x in range(-30,30):
    for y in range(-20,20):
        goto(x * m, y * m)
        dot(3, 'red')
update()
done()