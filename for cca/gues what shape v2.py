import turtle
import time
import random

#try to introduce typing coding to student

__Pen = turtle.Pen()

colors = ['#2D4356', '#435B66', '#A76F6F', '#EAB2A0', '#606C5D']
colors2 = ['#DBC4F0', '#FFCACC', '#D4E2D4', '#FAF3F0', '#C4DFDF']


def square(fillcolor): #parameter will decide what color to fill
    __Pen.fillcolor(fillcolor)
    __Pen.begin_fill()
    for __count in range(4):
        __Pen.forward(150)
        __Pen.right(90)
    __Pen.end_fill()

def triangle(fillcolor):
    __Pen.fillcolor(fillcolor)
    __Pen.begin_fill()
    for __count in range(3):
        __Pen.forward(200)
        __Pen.right(120)
    __Pen.end_fill()

def pentagon(fillcolor):
    __Pen.fillcolor(fillcolor)
    __Pen.begin_fill()
    for __count in range(5):
        __Pen.forward(150)
        __Pen.right(72)
    __Pen.end_fill()

def hexagon(fillcolor):
    __Pen.fillcolor(fillcolor)
    __Pen.begin_fill()
    for __count in range(6):
        __Pen.forward(150)
        __Pen.right(60)
    __Pen.end_fill()

def octagon(fillcolor):
    __Pen.fillcolor(fillcolor)
    __Pen.begin_fill()
    for __count in range(8):
        __Pen.forward(150)
        __Pen.right(45)
    __Pen.end_fill()

#Get start with Python
__Pen.pencolor("#999999")
__Pen.penup()
__Pen.goto((-80), 100)
__Pen.pendown()
turtle.bgcolor(random.choice(colors2))
octagon(random.choice(colors)) #pay attention to the parameter
time.sleep(1)
__Pen.clear()
hexagon(random.choice(colors))
turtle.bgcolor(random.choice(colors2))
time.sleep(1)
__Pen.clear()
triangle(random.choice(colors))
turtle.bgcolor(random.choice(colors2))
time.sleep(1)
__Pen.clear()
pentagon(random.choice(colors))
turtle.bgcolor(random.choice(colors2))
time.sleep(1)
turtle.done()
