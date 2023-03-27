# упражнение 10 цветок

import turtle
turtle.shape('turtle')
def turtle_circle(corner=0):
    turtle.left(corner)
    turtle.speed(10)
    x = 360
    while x>0:
        turtle.left(10)
        turtle.forward(10)
        x-=10

for i in range(6):
    turtle_circle(60)
