# Constants
from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]  # This has to after creating the snake or this will cause an error.

    # Create a snake
    def create_snake(self):
        """
        Each turtle segment is first created and than moved to a specific location
        We can turn off the animation using a tracer which is part of the screen class,
        once the tracer is turned off. we can than use screen update method to update the segments.
        make a change --> update --> make a change --> update --> make a change --> update --> make a change
        """
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")  # Create the turtle
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)  # Turtle will go to that location
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):

        '''
        in order to move all the segments such that they are linked together
        we will have to replace third, segment with second segment and the first segment will
        move forward. This will allow snake to move.
        '''
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
