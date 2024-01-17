import turtle

__Pen = turtle.Pen()


#Get start with Python
pen = turtle.Turtle()
screen = turtle.Screen()
turtle.bgcolor("#ffcccc")
pen.pencolor("#666666")

def click(x,y):
    global count
    pen.clear()
    count += 1
    pen.goto((-130), 100)
    pen.write('chasquear', font = ('Courier New', 40, 'bold'))
    pen.goto((-10), 0)
    pen.write(count, font = ('Courier New', 30, 'bold'))
    pen.goto((-50), (-80))
    pen.write('CLICKS', font = ('Courier New', 25, 'normal'))

#var to count the clicker
count = -1
pen.speed(30)
pen.penup()
#need to pass the parameter so u can just give a random number
click(0, 0)
screen.onclick(click, btn=1)

turtle.done()
