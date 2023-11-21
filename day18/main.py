import random
# module name is turtle and thing that you want from the module i.e. Turtle
from turtle import Turtle, Screen

timmy_the_turtle = Turtle() # Turtle class- We are creating a object of the class Turtle
# timmy_the_turtle.shape("turtle")

# timmy_the_turtle.forward(150)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(150)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(150)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(150)
# timmy_the_turtle.right(90)

# for _ in range(4):
#     timmy_the_turtle.forward(150)
#     timmy_the_turtle.right(90)
# Draw dashed lines
# for _ in range(10):
    # timmy_the_turtle.pencolor("black")
    # timmy_the_turtle.forward(10)
    # timmy_the_turtle.pencolor("white")
    # timmy_the_turtle.forward(10)
    # timmy_the_turtle.pendown()
    # timmy_the_turtle.forward(10)
    # timmy_the_turtle.penup()
    # timmy_the_turtle.forward(10)

# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon

"""
3 = triangle = 360/3 = 120
4 = sqaure = 360/4 = 90
5 = pentagon = 360/5 = 72
6 = hexagon = 360/6 = 60
8 = octagon = 360/8 = 45
9 = nonagon = 360/9 = 40
10 = decagon = 360/10 = 36
"""
shape_sides = [3,4,5,6,8,9,10]
colors = ["red","green","blue","orange","purple","pink","yellow"]

for sides in shape_sides:
    angle = 360/sides
    print(sides)
    color = random.choice(colors)
    print(color)
    for _ in range(sides):
        if sides == 3:
            timmy_the_turtle.pencolor(color)
            timmy_the_turtle.right(angle)
            timmy_the_turtle.forward(100)
        elif sides == 4:
            timmy_the_turtle.pencolor(color)
            timmy_the_turtle.right(angle)
            timmy_the_turtle.forward(100)
        elif sides == 5:
            timmy_the_turtle.pencolor(color)
            timmy_the_turtle.right(angle)
            timmy_the_turtle.forward(100)
        elif sides == 6:
            timmy_the_turtle.pencolor(color)
            timmy_the_turtle.right(angle)
            timmy_the_turtle.forward(100)
        elif sides == 8:
            timmy_the_turtle.pencolor(color)
            timmy_the_turtle.right(angle)
            timmy_the_turtle.forward(100)
        elif sides == 9:
            timmy_the_turtle.pencolor(color)
            timmy_the_turtle.right(angle)
            timmy_the_turtle.forward(100)
        elif sides == 10:
            timmy_the_turtle.pencolor(color)
            timmy_the_turtle.right(angle)
            timmy_the_turtle.forward(100)

# Only exist
screen = Screen()
screen.exitonclick()