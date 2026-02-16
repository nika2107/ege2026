from turtle import *
screensize(1500,1500)
tracer(0)
m = 10
rt(90)

for i in range(3):
    fd(39 * m)
    rt(90)
    fd(48 * m)
    rt(90)

up()

fd(27 * m)
rt(90)
fd (24 * m)
lt(90)

down()

for i in range(3):
    fd(29 * m)
    rt(90)
    fd(18 * m)
    rt(90)
up()

for x in range(-50,50):
    for y in range(-70,50):
        goto(x * m, y * m)
        dot(3, 'red')
update()
done()

print(((49*40)-(49*2 + 40 * 2)) + ((43 * 19)- (43 * 2 + 19 * 2)) - 247)