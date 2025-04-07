import turtle
import random
turtle.colormode(255)
common_colors = [
    "blue",
    "red",
    "green",
    "yellow",
    "black",
    "gray",
    "brown",
    "orange",
    "purple",
    "pink",
    "turquoise",
    "beige",
    "teal",
    "maroon",
    "navy",
    "lavender",
    "magenta",
    "cyan",
    "olive",
    "indigo",
    "violet",
    "silver",
    "gold",
    "coral",
    "salmon"
]
tim=turtle.Turtle()
tim.speed(10)
tim2=turtle.Turtle()
tim2.speed(10)
tim.pensize(10)
tim2.pensize(10)
def move1(x):
    r = random.randint(1,255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    tim.pencolor((r,g,b))
    tim.right(90*x)
    tim.forward(50)
def move2(x):
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    tim2.pencolor((r, g, b))
    tim2.right(90*x)
    tim2.forward(50)
for i in range(100):
    y1=random.randint(1,4)
    y2 = random.randint(1, 4)
    move1(y1)
    move2(y2)
turtle.exitonclick()