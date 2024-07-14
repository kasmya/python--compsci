import turtle
from turtle import *
a=Screen()
a.bgcolor('pink')
b=turtle.Turtle()
b.pencolor('white')
def curve():
    for i in range(200):
        b.rt(1)
        b.fd(1)
def heart():
    b.fillcolor('red')
    b.begin_fill()
    b.lt(140)
    b.fd(113)
    curve()
    b.lt(120)
    curve()
    b.fd(112)
    b.end_fill()
heart()
b.ht()
def write(message,pos):
    x,y=pos
    b.penup()
    b.goto(x,y)
    b.color('white')
    style=('Stencil Std',18,'italic')
    b.write(message,font=style)
write('P',(-68,95))
write('R',(-54,95))
write('O',(-40,95))
write('M',(-24,95))
write('?',(-7,95))

