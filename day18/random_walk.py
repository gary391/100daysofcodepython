import random
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]
# direction = [10, 20, 30, 45, 60, 90, 120, 145, 160, 180, 240, 270, 300, 360]
direction = [0, 90, 180, 270] # east, north, west, south
timmy_the_turtle.pensize(10)
timmy_the_turtle.speed(9)
for _ in range(300):
    # angle = 360 / sides
    # print(sides)
    color = random.choice(colors)
    # number = random.randint(-100, 100)
    # print(number)


    timmy_the_turtle.pencolor(color)
    timmy_the_turtle.setheading(random.choice(direction))
    timmy_the_turtle.forward(30)
screen = Screen()
screen.exitonclick()