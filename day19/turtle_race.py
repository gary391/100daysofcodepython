from turtle import Turtle, Screen
import random

screen = Screen()


# Screen size
screen.setup(width=500, height=400)

#Text Input for inputing text
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will the race? Enter a color: ")
color = ["red", "orange", "blue", "green", "purple", "yellow"]
all_turtle = []

is_race_on = False
x_position = -240
y_position = -60
for position in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color[position])
    # Starting line
    turtle_position = position * 30
    new_turtle.goto(x=x_position, y=y_position + turtle_position)
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won. The winning turtle is {winning_color}")
            else:
                print(f"You've lost. The winning turtle is {winning_color}")
            is_race_on = False
        turtle.forward(random.randint(0, 10))

screen.exitonclick()