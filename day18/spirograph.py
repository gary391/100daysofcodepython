import random
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)

timmy_the_turtle = Turtle()

timmy_the_turtle = Turtle()
named_colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]
# direction = [10, 20, 30, 45, 60, 90, 120, 145, 160, 180, 240, 270, 300, 360]
direction = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330]

angle = """
10
20
30
40
50
60
70
80
90
100
110
120
130
140
150
160
170
180
190
200
210
220
230
240
250
260
270
280
290
300
310
320
330
340
350
360
"""
r_dir = angle.strip().split()
r_direction = [int(i) for i in r_dir]
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


timmy_the_turtle.pensize(1)
timmy_the_turtle.speed("fastest") # fastest
# timmy_the_turtle.speed(10)

#
#
# for to_angle in r_direction:
#     timmy_the_turtle.pencolor(random_color())
# #TODO: Repeatedly draw a circle and change the tilt of the circle each time.
#     timmy_the_turtle.setheading(to_angle)
#     #TODO: How to create a circle with a radius of 100
#     timmy_the_turtle.circle(100, 360, 100)
def draw_spirograph(size_of_gap):

    for _ in range(int(360 / size_of_gap)):
        timmy_the_turtle.pencolor(random_color())
        timmy_the_turtle.circle(100, 360, 100)
        # this how we are setting the heading based on the current value of the heading.
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)

draw_spirograph(5)
#Allows the screen to remain on.

screen = Screen()
screen.exitonclick()