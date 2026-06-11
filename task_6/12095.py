from turtle import *
screensize(1000, 1000)
tracer(0)
m = 30

for i in range(12):
    fd(4 * m)
    rt(144)
    fd(4 * m)
    lt(72)

up()

for x in range(-15, 20):
    for y in range(-25, 5):
        goto(x * m, y * m)
        dot(5, 'red')
update()
done()