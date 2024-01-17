import turtle

#try to introduce typing coding to student
#since after this a lot of function project and conditional require a lot of typing
#doesnt mean u cannot use blocks anymore
#but some of the built in function might doesnt work on blocks

pen = turtle.Turtle()
colors = ['#F6D6D6','#FFE7C1','#7BD3EA','#A1EEBD','#F6F7C4']
number = 0
size = 150
move = 40
turtle.bgcolor("#F2F1EB")
pen.speed(10)
for i in range(5):
    pen.fillcolor(colors[number]) #explain indexing in list
    pen.color(colors[number])
    number += 1
    pen.begin_fill()
    pen.circle(size)
    pen.end_fill()
    size -= 40
    pen.penup()
    pen.goto(0, move)
    move += 40
    pen.pendown()

pen.penup()
pen.goto(0, 0)
pen.pensize(5)
pen.pencolor("#666666")
pen.pendown()
pen.circle(150)
pen.right(90)
pen.pensize(50)
pen.forward(200)
# pen.circle(90)
# pen.penup()
# pen.goto(0, 20)
# pen.pendown()
# pen.circle(80)
turtle.done()
