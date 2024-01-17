import turtle
import random

__Pen = turtle.Pen()


def finishline():
    __Pen.penup()
    __Pen.pensize(10)
    __Pen.pencolor("#009900")
    __Pen.goto(200, 200)
    __Pen.pendown()
    __Pen.right(90)
    __Pen.forward(400)

def createtext():
    __Pen.pencolor("#666666")
    __Pen.penup()
    __Pen.goto((-100), 200)
    __Pen.write('Turtle Race', font = ('Arial', 30, 'normal'))

#Get start with Python
turtle.bgcolor("#ffcc99")
finishline()
createtext()

turtle1 = turtle.Pen()
turtle1.pencolor("#3366ff")
turtle1.shape("turtle")
turtle1.color("#3366ff")
turtle1.penup()
turtle1.goto((-300), 100)
turtle2 = turtle.Pen()

turtle2.pencolor("#cc0000")
turtle2.shape("turtle")
turtle2.color("#cc0000")
turtle2.penup()
turtle2.goto((-300), 0)

turtle3 = turtle.Pen()
turtle3.pencolor("#ff9900")
turtle3.shape("turtle")
turtle3.color("#ff9900")
turtle3.penup()
turtle3.goto((-300), (-100))

while True:
    turtle1.forward(random.randint(1, 10))
    turtle2.forward(random.randint(1, 10))
    turtle3.forward(random.randint(1, 10))
    if (turtle1.xcor() >= 200):
        __Pen.pencolor("#3366ff")
        __Pen.goto((-70), 150)
        __Pen.write('Blue Turtle WINS', font = ('Arial', 15, 'normal'))
        break
    if (turtle2.xcor() >= 200):
        __Pen.pencolor("#cc0000")
        __Pen.goto((-70), 150)
        __Pen.write('Red Turtle WINS', font = ('Arial', 15, 'normal'))
        break
    if (turtle3.xcor() >= 200):
        __Pen.pencolor("#ff6600")
        __Pen.goto((-70), 150)
        __Pen.write('Orange Turtle WINS', font = ('Arial', 15, 'normal'))
        break

turtle.done()
