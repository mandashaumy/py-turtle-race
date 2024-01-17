import turtle
import random

__Pen = turtle.Pen()


#Get start with Python
turtle.bgcolor("#1374E7")
__Pen.speed(20)
__Pen.pensize(3)
__Pen.penup()
__Pen.goto((-150), 150)
__Pen.pendown()
__Pen.fillcolor("#F4F4F4")
__Pen.begin_fill()
for __count in range(4):
    __Pen.forward(300)
    __Pen.right(90)
__Pen.end_fill()
__Pen.fillcolor("#DFBDDA")
__Pen.begin_fill()
__Pen.forward(300)
__Pen.right(90)
__Pen.forward(25)
__Pen.left(90)
__Pen.backward(300)
__Pen.end_fill()
__Pen.write('enchanting blossoms.png       - x', font = ('Arial', 15, 'normal'))

__Pen.goto((-150), 150)
__Pen.fillcolor("#ABABAB")
__Pen.begin_fill()
__Pen.right(120)
__Pen.forward(25)
__Pen.left(30)
__Pen.forward(290)
__Pen.left(90)
__Pen.forward(300)
__Pen.left(60)
__Pen.forward(10)
__Pen.left(120)
__Pen.forward(290)
__Pen.right(90)
__Pen.forward(300)
__Pen.end_fill()
__Pen.right(90)

__Pen.pensize(2)
__Pen.pencolor("#AED8CC")
__Pen.fillcolor("#D4E2D4")
for __count in range(5):
    __Pen.penup()
    __Pen.goto(random.randint((-110), 110), random.randint((-110), 110))
    __Pen.pendown()
    __Pen.begin_fill()
    for __count in range(4):
        __Pen.circle(15)
        __Pen.left(90)
    __Pen.end_fill()

turtle.done()
