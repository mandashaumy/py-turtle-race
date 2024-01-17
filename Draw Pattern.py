import turtle

__Pen = turtle.Pen()


#Get start with Python
forward = 100
__Pen.fillcolor("#ccccff")
__Pen.speed(1)
__Pen.penup()
__Pen.setx((-100))
__Pen.pendown()
__Pen.begin_fill()
while (forward > 0):
    for __count in range(6):
        __Pen.right(60)
        __Pen.forward(forward)
        __Pen.left(120)
        __Pen.forward(forward)
    __Pen.penup()
    __Pen.left(60)
    __Pen.forward(10)
    __Pen.right(60)
    __Pen.pendown()
    forward -= 10
__Pen.end_fill()
turtle.done()
