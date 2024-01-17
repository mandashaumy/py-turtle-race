import turtle
import random


turtle.bgcolor("#FAF3F0")
turtle1 = turtle.Turtle()
turtle1.shape('turtle')
turtle1.shapesize(2)
turtle1.color('#D4E2D4')
turtle1.speed(5)
turtle1.pensize(5)
turtle1.penup()
turtle1.goto(random.randint(-100, 100), random.randint(-100, 100))
turtle1.right(random.randint(0, 360))
turtle1.pendown()

turtle2 = turtle.Turtle()
turtle2.shape('turtle')
turtle2.shapesize(2)
turtle2.color('#FFCACC')
turtle2.speed(5)
turtle2.pensize(5)
turtle2.penup()
turtle2.goto(random.randint(-100, 100), random.randint(-100, 100))
turtle2.right(random.randint(0, 360))
turtle2.pendown()

turtle3 = turtle.Turtle()
turtle3.shape('turtle')
turtle3.shapesize(2)
turtle3.color('#DBC4F0')
turtle3.speed(5)
turtle3.pensize(5)
turtle3.penup()
turtle3.goto(random.randint(-100, 100), random.randint(-100, 100))
turtle3.right(random.randint(0, 360))
turtle3.pendown()

while True:
    for i in range(random.randint(3, 6)):
        turtle1.forward(10)
        turtle2.forward(10)
        turtle3.forward(10)
        turtle1.penup()
        turtle2.penup()
        turtle3.penup()
        turtle1.forward(10)
        turtle2.forward(10)
        turtle3.forward(10)
        turtle1.pendown()
        turtle2.pendown()
        turtle3.pendown()
    turtle1.circle(random.randint(-50, 50), random.randint(30, 180))
    turtle2.circle(random.randint(-50, 50), random.randint(30, 180))
    turtle2.circle(random.randint(-50, 50), random.randint(30, 180))
    

turtle.done()
