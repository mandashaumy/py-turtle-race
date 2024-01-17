import turtle
import time

turtle.bgpic('space.png')
turtle.addshape('spacecat.gif')

pen = turtle.Turtle()

pen.shape('spacecat.gif')
while True:
    pen.forward(90)
    time.sleep(1)

turtle.done()
