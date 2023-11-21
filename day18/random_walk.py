import random
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)

timmy_the_turtle = Turtle()
named_colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]
# direction = [10, 20, 30, 45, 60, 90, 120, 145, 160, 180, 240, 270, 300, 360]
direction = [0, 90, 180, 270] # east, north, west, south
# make the line thicker

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


timmy_the_turtle.pensize(10)
# timmy_the_turtle.speed("fastest") # fastest
timmy_the_turtle.speed(9)
for _ in range(300):
    # angle = 360 / sides
    # print(sides)
    n_color = random.choice(named_colors)
    r_color = random_color()
    # number = random.randint(-100, 100)
    # print(number)


    # timmy_the_turtle.pencolor(n_color)

    # using random color
    timmy_the_turtle.pencolor(r_color)

    #sets the orientation of the turtle to to_angle.
    timmy_the_turtle.setheading(random.choice(direction))
    timmy_the_turtle.forward(30)
screen = Screen()
screen.exitonclick()