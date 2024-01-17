import turtle
import time

def p1():
    if spider1.ycor() > -300 and spider2.ycor() > -300:
        spider1.forward(5)
    if spider1.ycor() <= -300:
        win(1)
        time.sleep(2)
        quit()

def p2():
    if spider1.ycor() > -300 and spider2.ycor() > -300:
        spider2.forward(5)
    if spider2.ycor() <= -300:
        win(2)
        time.sleep(2)
        quit()
        
def win(player):
    if player == 1:
        __Pen.write('Spider 1 Win!!', font = ('Arial', 30, 'bold'))
    if player == 2:
        __Pen.write('Spider 2 Win!!', font = ('Arial', 30, 'bold'))

turtle.bgpic("web_background.gif")
turtle.addshape("spider.gif")

spider1 = turtle.Turtle()
spider1.shape("spider.gif")
spider2 = turtle.Turtle()
spider2.shape("spider.gif")
__Pen = turtle.Pen()
__Pen.pencolor("#ffffff")
__Pen.pensize(5)
__Pen.penup()
__Pen.goto((-110), 350)
__Pen.write('Spider Race', font = ('Arial', 30, 'bold'))
__Pen.goto((-170), 310)
__Pen.write('P1 = "A" ; P2 = "L"', font = ('Arial', 30, 'normal'))
__Pen.goto((-600), 300)
__Pen.pendown()
__Pen.forward(1200)
__Pen.penup()
__Pen.goto((-600), (-300))
__Pen.pendown()
__Pen.forward(1200)
__Pen.penup()
__Pen.goto((-70), (-350))
__Pen.write('FINISH', font = ('Arial', 30, 'bold'))
__Pen.goto(-120, 0)
__Pen.hideturtle()

spider1.penup()
spider2.penup()
spider1.goto(-300,300)
spider1.right(90)
spider2.goto(300,300)
spider2.right(90)
spider1.pencolor("#ffffff")
spider1.pensize(2)
spider2.pencolor("#ffffff")
spider2.pensize(2)
spider1.pendown()
spider2.pendown()


turtle.listen()
turtle.onkey(p1,"a")
turtle.onkey(p2,"l")



turtle.done()
