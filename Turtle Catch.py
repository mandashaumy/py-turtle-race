import random
import turtle
import math

x = random.randint(1, 100)
y = random.randint(1, 100)
border = turtle.Turtle()
border.pensize(5)
border.penup()
border.goto((-100), (-100))
border.pendown()
for i in range(4):
    border.forward(240)
    border.left(90)
border.hideturtle()

block = turtle.Turtle()
block.shape('circle')
block.color('Green')
block.shapesize(0.3)
block.penup()
block.goto(x, y)

arrow = turtle.Turtle()
arrow.shape('turtle')
arrow.color('Blue')
arrow.penup()
speed = 1

def collision(p, e):
    d = math.sqrt(math.pow(p.xcor()-e.xcor(),2) + (math.pow(p.ycor()-e.ycor(),2)))
    if d < 20:
        return True
    else:
        return False

def turnleft():
    arrow.left(30)

def turnright():
    arrow.right(30)

def speedup():
    global speed
    speed += 1

def stop():
    global speed
    speed -=1

def stopp():
    global speed
    speed = 0

turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(speedup, "Up")
turtle.onkey(stop, "Down")

while True:
    arrow.forward(speed)
    if arrow.xcor() > 145 or arrow.xcor() < -100:
        arrow.left(180)
    elif arrow.ycor() > 145 or arrow.ycor() < -100:
        arrow.left(180)
    if collision(arrow, block):
        block.setpos(random.randint(1, 100), random.randint(1, 100))

turtle.done()
