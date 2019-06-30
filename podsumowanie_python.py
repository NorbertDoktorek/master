import turtle
import random

kolory = ['red', 'purple', 'green', 'orange', 'blue', 'yellow']

turtle.penup()
turtle.setpos(0,150)
turtle.pendown()
x=turtle.color(random.sample(kolory,1))
turtle.write("Python od Podstaw", align='center', font=(x,30))

turtle.penup()
turtle.setpos(0,75)
turtle.pendown()
x=turtle.color(random.sample(kolory,1))

turtle.write("Poznań", align='center', font=(x,30))

turtle.penup()
turtle.setpos(0,0)
turtle.pendown()
x=turtle.color(random.sample(kolory,1))

turtle.write("Kontakt: ", align='center', font=(x,30))

turtle.penup()
turtle.setpos(0,-75)
turtle.pendown()
x=turtle.color(random.sample(kolory,1))

turtle.write("Email: malgorzata.lyczywek@codeme.pl", align='center', font=(x,30))

turtle.penup()
turtle.setpos(0,-150)
turtle.pendown()
x=turtle.color(random.sample(kolory,1))

turtle.write("Tel: +48 724 379 836", align='center', font=(x,30))

turtle.penup()
turtle.setpos(0,-225)
turtle.pendown()
x=turtle.color(random.sample(kolory,1))

turtle.write("URL: https://codeme.pl", align='center', font=(x,30))

turtle.done()