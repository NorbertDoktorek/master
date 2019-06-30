import turtle
kolory = ['red', 'purple', 'green', 'orange', 'blue', 'yellow']
t = turtle.Pen()
t.speed(11)
turtle.bgcolor('black')
t.pensize(4)
for x in range(270):
    t.pencolor(kolory[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(90)

turtle.done()