import turtle
import time

led1 = turtle.Turtle()
led2 = turtle.Turtle()
led3 = turtle.Turtle()
led4 = turtle.Turtle()

#Get start with Python
turtle.bgcolor("#333333")
led1.hideturtle()
led1.speed(20)
led1.pencolor("#ff0000")
led1.pensize(10)
led1.penup()

led2.hideturtle()
led2.speed(20)
led2.pencolor("#ff0000")
led2.pensize(10)
led2.penup()

led3.hideturtle()
led3.speed(20)
led3.pencolor("#ff0000")
led3.pensize(10)
led3.penup()
led3.right(90)

led4.hideturtle()
led4.speed(20)
led4.pencolor("#ff0000")
led4.pensize(10)
led4.penup()
led4.left(90)
while True:
    led1.goto((-200), 0)
    led2.goto(200, 0)
    led3.goto(0, 200)
    led4.goto(0, -200)
    for __count in range(10):
        led1.pendown()
        led2.pendown()
        led3.pendown()
        led4.pendown()
        led1.forward(10)
        led2.forward(-10)
        led3.forward(10)
        led4.forward(10)
        led1.penup()
        led2.penup()
        led3.penup()
        led4.penup()
        led1.forward(10)
        led2.forward(-10)
        led3.forward(10)
        led4.forward(10)
        time.sleep(0.2)
    
    led1.clear()
    led2.clear()
    led3.clear()
    led4.clear()

turtle.done()
