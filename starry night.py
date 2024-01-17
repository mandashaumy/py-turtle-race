import turtle
import random
import colorsys

star = turtle.Turtle()
star.color('yellow')
turtle.bgcolor('black')
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
c = colorsys.hsv_to_rgb(r, g, b)

while True:
    x = random.randint(-300,300)
    y = random.randint(-200,200)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    c = colorsys.hsv_to_rgb(r, g, b)
    size = random.randint(10, 50)
    star.penup()
    star.goto(x, y)
    star.pendown()
    star.fillcolor(c)
    star.begin_fill()
    for i in range(5):
        star.left(216)
        star.forward(size)
    star.end_fill()

turtle.done()