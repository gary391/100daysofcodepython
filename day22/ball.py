from turtle import Turtle
import random
UP_RIGHT = 30
MOVE_DISTANCE = 20
class Ball(Turtle):

    def __init__(self):
        super().__init__() # call to the super class
        self.shape("circle")
        self.penup()
        # create a smaller size turtle, which is 20 by 20
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("red")
        self.speed("fastest")
        self.x_move = 10
        self.y_move = 10

    # def move(self):
    #     self.setheading(UP_RIGHT)
    #     self.forward(MOVE_DISTANCE)
    def move(self):
        new_x = self.xcor() + self.x_move
        print(f"new_x: {new_x}")
        new_y = self.ycor() + self.y_move
        print(f"new_y: {new_y}")
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset(self):
        self.goto(0, 0)
        self.bounce_x()



