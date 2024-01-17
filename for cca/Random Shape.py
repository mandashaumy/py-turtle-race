import turtle
import random

__Pen = turtle.Pen()


#Get start with Python
turtle.bgcolor('#967E76')
while True:
    colors = ['#D7C0AE','#EEE3CB','#B7C4CF']
    __Pen.pencolor(random.choice(colors))
    __Pen.fillcolor(random.choice(colors))
    __Pen.begin_fill()
    __Pen.penup()
    __Pen.goto(random.randint((-200), 200), random.randint((-200), 200))
    __Pen.pendown()
    __Pen.circle(random.randint(10, 50), steps=random.randint(3, 10))
    __Pen.end_fill()
