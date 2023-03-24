
# a = 179
# b = 971
# c = (a ** 2 + b ** 2) ** 0.5
# print (c)

# print(type(2.1233))
# print(type('2.1233'))
# print(type(2))
# print(type(10%3))

# упражнение 4 Окружность
# import turtle
#
# turtle.shape('turtle')
# x=360
# while x>0:
#     turtle.left(1)
#     turtle.forward(1)
#     x-=1



# упражнение 5 10 вложенных квадратов
# import turtle
# x=10
# y=90
# z=10
# f = -5
# while z>0:
#     turtle.shape('turtle')
#     turtle.forward(x)
#     turtle.left(y)
#     turtle.forward(x)
#     turtle.left(y)
#     turtle.forward(x)
#     turtle.left(y)
#     turtle.forward(x)
#     turtle.left(y)
#     turtle.penup()
#     turtle.goto(f, f)
#     turtle.pendown()
#     x+=10
#     f-=5
#     z-=1

# упражнение 6 паук
# import turtle
# n=int(input())
# turtle.shape('turtle')
# x=360/n
# while n>0:
#     turtle.left(x)
#     turtle.forward(70)
#     turtle.stamp()
#     turtle.backward(70)
#     n-=1

# упражнение 7 спираль
# import turtle
# import math
# turtle.shape('turtle')
# turtle.color('red')
# pi = math.pi
# a = 5
# f = 1
# p = (a / (2 * pi)) / 360
# p1 = (a / (2 * pi)) / 360
# while p<=100:
#     turtle.left(f)
#     turtle.forward(p)
#     p+=p1

# упражнение 8 спираль квадрат
# import turtle
# turtle.shape('turtle')
# x=5
# y=90
# while x<100:
#     turtle.left(y)
#     turtle.forward(x)
#     x+=2