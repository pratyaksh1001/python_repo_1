import turtle
t1=turtle.Turtle()
screen=turtle.Screen()
t1.pensize(10)
def forward():
    t1.forward(10)
def right():
    t1.right(30)
def left():
    t1.left(30)
def backward():
    t1.backward(1)
def clear():
    t1.penup()
    t1.clear()
    t1.home()
    t1.pendown()
screen.listen()
screen.onkey(forward,"w")
screen.onkey(right,"d")
screen.onkey(left,"a")
screen.onkey(backward,"s")
screen.onkey(clear,"c")
turtle.exitonclick()