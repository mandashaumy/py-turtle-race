import turtle


pen = turtle.Pen()
screen = turtle.Screen()

def draw(x,y):
    pen.pendown()
    pen.goto(x, y)

def move(x,y):
    pen.penup()
    pen.goto(x, y)

screen.onclick(draw, btn= 1)
screen.onclick(move, btn= 3)

turtle.done()
