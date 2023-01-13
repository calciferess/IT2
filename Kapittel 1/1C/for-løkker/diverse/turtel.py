#turtel

import turtle
x_pos= 0
y_pos= 0
radius= 50

for i in range(10):
    turtle.circle(radius)

    turtle.penup()
    turtle.setpos(x_pos,y_pos)
    turtle.pendown()
    x_pos= x_pos+10
    y_pos= y_pos+20
    radius=radius+10
