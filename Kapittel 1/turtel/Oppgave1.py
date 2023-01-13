#Oppgave 1 
import TK as tkinter
import turtle

turtle.colormode(255)

def stjerne():
    turtle.begin_fill()
    turtle.color(100,100,100)
    turtle.fillcolor(255,200,0)
    turtle.penup()
    turtle.setpos(0,0)
    turtle.pendown()
    for i in range(5):
        turtle.forward(100)
        turtle.right(144)
    turtle.end_fill()

stjerne()  
