import turtle
import random
turtle.colormode(255)
screen=turtle.Screen()
screen.setup(800,500)
w=800
h=500
tt=turtle.Turtle()
tt.penup()
tt.setposition(w/2-50,-h/2)
tt.pendown()
tt.setposition(w/2-50,h/2)
tt.penup()

def prepare(t):
    t.penup()
    r=random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    t.color((r,g,b))
    t.shape("turtle")
t_list=[]
for i in range(4):
    x=turtle.Turtle()
    prepare(x)
    t_list.append(x)
x=-230
y=60
for i in range(4):
    t_list[i].goto(x,y)
    y-=50
winner=""
user_bet=int(screen.textinput("make your bet","enter the number of turtle on whom you want to place bet"))
l=0
while l==0:
    for i in range(4):
        if t_list[i].xcor()>=350:
            print(t_list[i].xcor())
            winner=i+1
            l+=1
        p = random.randint(0, 10)
        t_list[i].forward(p)
if winner==user_bet:
    print("You Won !")
else:
    print("You Lost")
    print("your bet was on: ",user_bet,"but the winner is: ",winner)
turtle.exitonclick()