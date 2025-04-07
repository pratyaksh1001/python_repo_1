import turtle
t1=turtle.Turtle()
t1.shape("turtle")
t1.color("coral")
t1.speed(5)
a=-200
b=-200
for i in range(100):

    t1.setposition(a,b)
    t1.forward(50)
    t1.backward(50)
    b+=5
    a+=5
My_screen=turtle.Screen()
print(My_screen.canvheight)
My_screen.exitonclick()