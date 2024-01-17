import turtle

#better doing this project by typing
#please give a brief about function parameters before doing this project
#just use a very simple example
#try to modify the project by adding some colors or other decoration

pen = turtle.Pen() #define turtle name it pen
screen = turtle.Screen() #should define screen for the onclick function

#define a function to be call whenever the left click mouse occur
def draw(x,y): #parameters receive the mouse pos on x & y var
    pen.pendown() 
    pen.goto(x, y) #move the turtle to the exact positon based on the number in the parameters

#define a function to be call whenever the right click mouse occur
def move(x,y): 
    pen.penup()#parameters receive the mouse pos on x & y var
    pen.goto(x, y)#move the turtle to the exact positon based on the number in the parameters

#use the onclick function
screen.onclick(draw, btn= 1) #call the draw function when left click, mouse pointer position also send as the parameters
screen.onclick(move, btn= 3) #call the move function when right click, mouse pointer position also send as the parameters

turtle.done()
