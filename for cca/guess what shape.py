import turtle
import time

#try to introduce typing coding to student
#since after this a lot of function project and conditional require a lot of typing
#doesnt mean u cannot use blocks anymore
#but some of the built in function might doesnt work on blocks

__Pen = turtle.Pen()


def square():
    for __count in range(4):
        __Pen.forward(150)
        __Pen.right(90)

def triangle():
    for __count in range(3):
        __Pen.forward(200)
        __Pen.right(120)

def pentagon():
    for __count in range(5):
        __Pen.forward(150)
        __Pen.right(72)

def hexagon():
    for __count in range(6):
        __Pen.forward(150)
        __Pen.right(60)

def octagon():
    for __count in range(8):
        __Pen.forward(150)
        __Pen.right(45)

#Get start with Python
__Pen.pencolor("#999999")
__Pen.penup()
__Pen.goto((-80), 100)
__Pen.pendown()
__Pen.fillcolor("#ffcccc")
__Pen.begin_fill()
octagon()
__Pen.end_fill()
turtle.bgcolor("#ccffff")
time.sleep(1)
__Pen.clear()
__Pen.fillcolor("#9999ff")
__Pen.begin_fill()
hexagon()
__Pen.end_fill()
turtle.bgcolor("#ffffcc")
time.sleep(1)
__Pen.clear()
__Pen.fillcolor("#99ffff")
__Pen.begin_fill()
triangle()
__Pen.end_fill()
turtle.bgcolor("#cccccc")
time.sleep(1)
__Pen.clear()
__Pen.fillcolor("#99ff99")
__Pen.begin_fill()
pentagon()
__Pen.end_fill()
turtle.bgcolor("#ffcc99")
time.sleep(1)
turtle.done()
