import turtle
import snake
import time
import food
import score
SCORE=0
screen=turtle.Screen()
screen.tracer(0)
screen.setup(600,400)
screen.bgcolor("black")
screen.listen()
g=1
s=snake.snake()
fd=food.Food()
screen.listen()
F=0
while g:
    time.sleep(0.1)
    screen.update()
    g=s.move(g)
    screen.update()
    screen.onkey(s.up,"Up")
    screen.update()
    screen.onkey(s.down, "Down")
    screen.update()
    screen.onkey(s.right,"Right")
    screen.update()
    screen.onkey(s.left,"Left")
    screen.update()
    F+=1
    if s.segments[0].distance(fd)<3:
        s.add()
        SCORE+=1
        fd.refresh()
    for i in range(3,len(s.segments)):
        if s.segments[0].distance(s.segments[i])<10:
            g=0
            print("Game Over !")
screen.exitonclick()