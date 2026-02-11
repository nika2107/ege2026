from turtle import *
screensize(2000, 2000)
tracer(0)
m = 20

rt(90)

down()
for i in range(7):
    rt(45)
    fd(11 * m)
    rt(45)
up()

for x in range(-25,10):
    for y in range(-10,15):
        goto(x * m, y * m)
        dot(5, 'red')

update()
done()

