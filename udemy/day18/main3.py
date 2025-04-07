import turtle
import random
timmy=turtle.Turtle()
timmy.shape("turtle")
timmy.speed(10)
timmy.penup()
timmy.setposition(0,300)
timmy.pendown()
common_colors = [
    "Blue",
    "Red",
    "Green",
    "Yellow",
    "Black",
    "Gray",
    "Brown",
    "Orange",
    "Purple"
]
shape=3
side=20
def draw_shape(sides):
    timmy.pencolor(random.choice(common_colors))
    angle=360/sides
    for _ in range(sides):
        timmy.forward(50)
        timmy.right(angle)

for i in range(3,101):
    draw_shape(i)
turtle.exitonclick()