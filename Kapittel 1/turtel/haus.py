#Haus

import turtle

turtle.penup()
turtle.setpos(-300,-200)
turtle.pendow()

turtle.fillcolor("red")
turtle.begin_fill()

turtle.forward(400)
turtle.left(90)
turtle.forward(200)
turtle.left(45)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(45)
turtle.forward(200)

turtle.end_fill()

turtle.fillcolor("yellow")
turtle.penup()
turtle.setpos(200,300)

turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

