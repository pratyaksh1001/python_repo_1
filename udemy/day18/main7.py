from main6 import c
import random
import turtle
turtle.colormode(255)
t1=turtle.Turtle()
t1.speed(15)
x=0
t1.penup()
t1.setposition(300,-300)
t1.pensize(20)
for i in range(10):
    if x % 2 == 0:
        t1.left(90)
        t1.penup()
        t1.forward(50)
        t1.pendown()
        t1.forward(1)
        t1.left(90)
    else:
        t1.right(90)
        t1.penup()
        t1.forward(50)
        t1.pendown()
        t1.forward(1)
        t1.right(90)
    x += 1
    for j in range(10):
        t1.pencolor(random.choice(c))
        t1.penup()
        t1.forward(50)
        t1.pendown()
        t1.forward(1)
turtle.exitonclick()