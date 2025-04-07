import turtle
import random
turtle.colormode(255)
t1=turtle.Turtle()
t1.pensize(10)
t1.speed(15)
angle = 5
for i in range(10000):
    r = random.randint(1,225)
    g = random.randint(1, 225)
    b = random.randint(1, 225)
    t1.pencolor((r,g,b))
    t1.circle(radius=100)
    t1.left(angle)
turtle.exitonclick()