import turtle

__Pen = turtle.Pen()


#Get start with Python
__Pen.speed(10)
turtle.bgcolor("#333333")
__Pen.pencolor("#6666cc")
__Pen.fillcolor("#ccccff")
__Pen.penup()
__Pen.goto((-100), 0)
__Pen.pendown()
__Pen.begin_fill()
for __count in range(36):
    __Pen.forward(200)
    __Pen.left(170)
__Pen.end_fill()
__Pen.forward((-200))
__Pen.right(90)
__Pen.circle(150)
__Pen.left(90)
__Pen.forward(300)
__Pen.right(90)
__Pen.circle(150)
turtle.done()
