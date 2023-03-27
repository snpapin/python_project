# упражнение 9 многоугольники
import turtle
import math
turtle.shape('turtle')
turtle.speed(10)
def manyangle(angles, rad):
    angle = 360/angles
    a = rad * 2 * math.sin(math.radians(360 / (2 * angles)))
    while angles>0:
        turtle.left(angle)
        turtle.forward(a)
        angles-=1
rad = 20
for i in range(3,12):
    angle1 = (180 - 360/i)/2
    turtle.left(angle1)
    manyangle(i, rad)
    turtle.right(angle1)
    turtle.penup()
    turtle.goto(rad, 0)
    turtle.pendown()
    rad+=20