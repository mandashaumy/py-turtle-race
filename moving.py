import turtle
import time
import random

__Pen = turtle.Pen()


#Get start with Python
colors = ['red','green','blue','orange','purple','pink','yellow']
__Pen.shape('turtle')
__Pen.setheading(180)
__Pen.penup()
__Pen.hideturtle()
__Pen.goto(300, 0)
__Pen.showturtle()
while True:
    __Pen.color(random.choice(colors))
    for __count in range(60):
        __Pen.forward(10)
        time.sleep(0.05)
    __Pen.hideturtle()
    __Pen.goto(300, 0)
    __Pen.showturtle()
turtle.done()
