import colorgram


# Extract all colors from an image.

# def extract_color(image, color_count):
#     colors = colorgram.extract(image, color_count)
#     # first_color = colors[0]
#     # rgb = first_color.rgb
#     color_palette = []
#     for color in colors:
#         rgb = color.rgb
#         color_palette.append((rgb.r, rgb.g, rgb.b))
#     return color_palette
# print(extract_color('damien-hirst-spot-painting-for-sale.jpg', 60))

import random
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)

timmy_the_turtle = Turtle()

timmy_the_turtle.speed("fastest") # fastest
timmy_the_turtle.penup()
timmy_the_turtle.hideturtle()
color_list = [(213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31), (115, 155, 171), (124, 79, 99), (122, 175, 156), (229, 236, 239), (226, 198, 131), (192, 87, 108), (11, 50, 64), (55, 38, 19), (45, 168, 126), (47, 127, 123), (200, 121, 143), (168, 21, 29), (228, 92, 77), (244, 162, 160), (38, 32, 35), (2, 25, 24), (78, 147, 171), (170, 23, 18), (19, 79, 90), (101, 126, 158), (235, 166, 171), (177, 204, 185), (49, 62, 84), (164, 203, 208), (183, 190, 204), (83, 70, 40), (11, 112, 106)]
"""
Req:
10*10 rows of spot
each dot is 20 in size
spaced apart 50 paces


"""

screen = Screen()
screen.setup (width=1000, height=1000)

timmy_the_turtle.setheading(225)
timmy_the_turtle.forward(300)
timmy_the_turtle.setheading(0)
number_of_dots = 100



for dot_count in range(1, number_of_dots+1):
    n_color = random.choice(color_list)
    timmy_the_turtle.dot(20, n_color)
    timmy_the_turtle.fd(50)
    # timmy_the_turtle.setx(0)
    # timmy_the_turtle.sety(y_coordinate * 50)
    if dot_count % 10 == 0:
        timmy_the_turtle.setheading(90)
        timmy_the_turtle.forward(50)
        timmy_the_turtle.setheading(180)
        timmy_the_turtle.forward(500)
        timmy_the_turtle.setheading(0)
screen.exitonclick()
