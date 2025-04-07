import turtle
from snakegame import SCORE
class Score(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.write(f"Score: {self.score}",align="centre",font=("ariel",24,""))
        self.goto(0,280)
    def increase(self,SCORE):
        SCORE+=1