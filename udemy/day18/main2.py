import turtle
timmy=turtle.Turtle()
timmy.shape("turtle")
timmy.speed(1)
timmy.color("red")
timmy.pencolor("white")
timmy.setposition(-700,0)
timmy.pencolor("black")
for i in range(100):
    timmy.forward(5)
    timmy.pencolor("white")
    timmy.forward(5)
    timmy.pencolor("black")
turtle.exitonclick()
