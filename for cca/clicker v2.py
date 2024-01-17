import turtle
import random


#Get start with Python
pen = turtle.Turtle()
screen = turtle.Screen()
turtle.bgcolor("#ffcccc")
pen.pencolor("#666666")

colors = ['#DBC4F0', '#FFCACC', '#D4E2D4', '#FAF3F0', '#C4DFDF']

def click(x,y):
    #count variable was outside the function, to call it inside function need to declare it as global
    global count 
    pen.clear()
    # turtle.bgcolor(random.choice(colors))
    count += 1
    pen.goto((-130), 100)
    pen.write('chasquear', font = ('Courier New', 40, 'bold'))
    pen.goto((-10), 0)
    pen.write(count, font = ('Courier New', 30, 'bold'))
    pen.goto((-50), (-80))
    pen.write('CLICKS', font = ('Courier New', 25, 'normal'))
    if count > 5:
        turtle.bgcolor(colors[0])
    if count > 10:
        turtle.bgcolor(colors[1])
    if count > 15:
        turtle.bgcolor(colors[2])
    if count > 20:
        turtle.bgcolor(colors[3])
    if count > 25:
        turtle.bgcolor(colors[4])

count = -1 #var to count the clicker
pen.speed(30)
pen.penup()
click(0, 0) #need to pass the parameter so u can just give a random number
screen.onclick(click, btn=1)

turtle.done()
