import turtle

__Pen = turtle.Pen()


#Get start with Python
__Pen.speed(3)
__Pen.pencolor("#00cccc")
__Pen.fillcolor("#ffccff")
__Pen.penup()
__Pen.goto((-100), 0)
__Pen.pendown()
__Pen.forward(200)
__Pen.begin_fill()
while True:
    __Pen.left(170)
    __Pen.forward(200)
    if (__Pen.xcor() == -100 and __Pen.ycor() == 0):
        __Pen.forward(0)
__Pen.end_fill()
turtle.done()
