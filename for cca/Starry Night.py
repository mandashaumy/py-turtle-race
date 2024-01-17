import turtle
import random


#Get start with Python
star = turtle.Turtle()
turtle.bgcolor("#2A2F4F")
#create moon
star.pencolor("#2A2F4F")
star.penup()
star.goto((-200), 100)
star.pendown()
star.fillcolor("#FDF4F5")
star.begin_fill()
star.circle(50)
star.end_fill()
star.penup()
star.goto((-170), 110)
star.pendown()
star.fillcolor("#2A2F4F")
star.begin_fill()
star.circle(50)
star.end_fill()
#create stars
while True:
    size = random.randint(5, 20)
    star.color('yellow')
    star.speed(100)
    star.penup()
    star.goto(random.randint((-300), 300), random.randint((-200), 200))
    star.pendown()
    star.fillcolor('white')
    star.begin_fill()
    for i in range(5):
        star.left(216)
        star.forward(size)
    star.end_fill()

turtle.done()
