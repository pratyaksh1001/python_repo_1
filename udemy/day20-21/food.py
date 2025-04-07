import turtle
import random

class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("green")
        self.speed("fastest")
        self.goto(random.randrange(-300+20,301-20,20),random.randrange(-200+20,201-20,20))
    def refresh(self):
        self.goto(random.randrange(-300 + 20, 301 - 20, 20), random.randrange(-200 + 20, 201 - 20, 20))
