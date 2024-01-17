import turtle
import random
import time

__Pen = turtle.Pen()


#Get start with Python
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgpic("gradient.png")
__Pen.pencolor("#F6F4EB")
__Pen.speed(1)
__Pen.left(90)
__Pen.pensize(2)
for __count in range(6):
    __Pen.backward(15)
    __Pen.left(60)
    __Pen.forward(15)
    __Pen.backward(15)
    __Pen.right(120)
    __Pen.forward(15)
    __Pen.backward(15)
    __Pen.left(60)
__Pen.backward(15)
__Pen.right(60)
turtle.done()
