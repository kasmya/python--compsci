import turtle
a=turtle.Turtle()
b=turtle.Screen()
b.bgcolor('gray')
a.speed(0)
c=('yellow','orange','red','pink','turquoise','purple')
for i in range(150):
    a.pencolor(c[i%6])
    a.circle(190-i/2,90)
    a.lt(90)
    a.circle(190-i/3,90)
    a.lt(60)
b.exitonclick()
