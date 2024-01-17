import turtle
import random
import time

colors = ['#F6D6D6','#FFE7C1','#7BD3EA','#A1EEBD','#F6F7C4']

pen = turtle.Turtle()
pen.speed(30)
pen.color('#FFFFFF')

while True:
    count = 3
    for i in range (3):
        pen.clear()
        turtle.bgcolor('#cccccc')
        pen.penup()
        pen.goto(-200, 0)
        pen.write('Guess the Color!', font = ('Arial', 40, 'bold'))
        pen.goto(-20, -50)
        pen.write(count, font = ('Arial', 30, 'normal'))
        time.sleep(1)
        count -= 1
        
        
    turtle.bgcolor(random.choice(colors))
    time.sleep(3)
    pen.clear()




