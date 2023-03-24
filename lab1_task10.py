# упражнение 10 цветочек
# forward(X) - Пройти вперёд X пикселей
# backward(X) - Пройти назад X пикселей
# left(X) - Повернуться налево на X градусов
# right(X) - Повернуться направо на X градусов
# penup() - Не оставлять след при движении
# pendown() - Оставлять след при движении
# shape(X) - Изменить значок черепахи (“arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”)
# stamp() - Нарисовать копию черепахи в текущем месте
# color() - Установить цвет
# begin_fill() - Необходимо вызвать перед рисованием фигуры, которую надо закрасить
# end_fill() - Вызвать после окончания рисования фигуры
# width() - Установить толщину линии
# goto(x, y) - Переместить черепашку в точку (x, y)

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
