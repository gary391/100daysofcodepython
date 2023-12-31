from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__() # call to the super class
        self.shape("circle")
        self.penup()
        # create a smaller size turtle, which is 20 by 20
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
