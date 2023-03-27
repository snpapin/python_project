# Упражнение 11 - бабочка

import turtle as t
t.shape('turtle')
t.left(90)
def turtle_circle_right(step = 9, step2 = 10):
    t.speed(8)
    x = 360
    while x>0:
        t.right(step)
        t.forward(step2)
        x-=step
def turtle_circle_left(step = 9)
    t.speed(8)
    x = 360
    while x>0:
        t.left(step)
        t.forward(step2)
        x-=step

for i in range(10, 21, 1):
    turtle_circle_right(step2 = i)
    turtle_circle_left(step2 = i)




