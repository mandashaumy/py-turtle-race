import turtle
import time

__Pen = turtle.Pen()


#Get start with Python
turtle.bgcolor("#333333")
__Pen.hideturtle()
__Pen.speed(20)
__Pen.fillcolor("#ff0000")
__Pen.pencolor("#333333")
__Pen.penup()
while True:
    __Pen.goto((-200), 0)
    for __count in range(10):
        __Pen.begin_fill()
        __Pen.pendown()
        __Pen.circle(25)
        __Pen.penup()
        __Pen.end_fill()
        __Pen.setx((__Pen.xcor() + 50))
        time.sleep(0.2)
        __Pen.clear()
turtle.done()
