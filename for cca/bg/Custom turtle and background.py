import turtle


def get_mouse_coor(x,y):
    tiger.penup()
    tiger.speed(1)
    tiger.goto(x, y)

#link untuk gambar:
#https://drive.google.com/drive/folders/10mIkRyesMJdywZwN1rZ4louvOhukRlDP?usp=sharing

# gunakan format gif
#letakkan file gambar dalam folder yang sama dengan script python
turtle.bgpic("jungle.gif")

tiger = turtle.Turtle()

turtle.addshape('tiger.gif')
tiger.shape('tiger.gif')

turtle.onscreenclick(get_mouse_coor)

turtle.done()
