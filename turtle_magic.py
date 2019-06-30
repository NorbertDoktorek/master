import turtle
kolory = ['red', 'purple', 'green', 'orange', 'blue', 'yellow']
t = turtle.Pen()
t.speed(11)
turtle.bgcolor('black')
t.pensize(2)
for x in range(180):
    t.pencolor(kolory[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)
    t.goto(100, 0)
    t.goto(100, 100)
    t.goto(0, 100)
    t.goto(0, 0)

turtle.done()