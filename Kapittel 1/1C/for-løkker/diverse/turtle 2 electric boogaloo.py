#turtel 2: electric boogaloo
import turtle

turtle.penup()
turtle.setpos(-350,0)
turtle.pendown()
turtle.fillcolor('red')

for i in range(100):
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()

    turtle.penup()
    turtle.forward(60)
    turtle.pendown()

