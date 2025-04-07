import turtle
import time
POSITION=[(-40,0),(-20,0),(0,0)]
SNAKE=[]


class snake:
    def __init__(self):
        self.segments=SNAKE
        self.createsnake()

    def createsnake(self):
        for i in range(3):
            t = turtle.Turtle("square")
            x=POSITION[i][0]
            y=POSITION[i][1]
            t.speed(1)
            t.penup()
            t.color("white")
            t.setposition(x, y)
            SNAKE.append(t)
    def forward(self):
        SNAKE[0].forward(20)

    def up(self):
        if SNAKE[0].heading()!=270:
            SNAKE[0].setheading(90)

    def down(self):
        if SNAKE[0].heading() != 90:
            SNAKE[0].setheading(270)

    def left(self):
        if SNAKE[0].heading() != 0:
            SNAKE[0].setheading(180)

    def right(self):
        if SNAKE[0].heading() != 180:
            SNAKE[0].setheading(0)

    def move(self,game):
        for i in range(len(SNAKE) - 1, 0, -1):
            SNAKE[i].goto(SNAKE[i - 1].xcor(), SNAKE[i - 1].ycor())
        time.sleep(0)
        self.forward()
        if SNAKE[0].xcor() > 300 or SNAKE[0].xcor() < -300 or SNAKE[0].ycor() > 200 or SNAKE[0].ycor() < -200:
            print("Game Over !")
            print(len(self.segments))
            game=0
        return game

    def add(self):
        tx=turtle.Turtle("square")
        tx.color("white")
        tx.penup()
        tx.setposition(SNAKE[-1].xcor(),SNAKE[-1].ycor())
        SNAKE.append(tx)