from turtle import Screen, Turtle
import pandas
screen = Screen()

turtle = Turtle()
screen.title("U.S. States Games")
# You can load the image as a shape of the turtle
image = "blank_states_img.gif"
# you can load an image as a new shape,
# which can be any image file.
screen.addshape(image)
# Once you have added the image to the screen,
# then it is available to the turtle
turtle.shape(image)
total_count = 50
guessed_state = []


"""
1. Convert the guess to Title case.
2. Check if the guess is among the 50 states.
3. Write correct guesses onto the map.
4. Use a loop (while) to allow the user to keep guessing.
5. Record the correct guesses in a list.
6. Keep track of the score.
"""

data = pandas.read_csv("50_states.csv")

# Returns a list of states.
list_of_states = data["state"].tolist()

# Check if the guess is among the 50 states.
while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f" {len(guessed_state)}/{total_count} States Correct",
                                    prompt="What's another state's name?".title())
    print(answer_state)
    if answer_state == "Exit":
        break
    # in key word will only work if the series is converted to a list.
    if answer_state in list_of_states:
        guessed_state.append(answer_state)
        turtle = Turtle()
        turtle.hideturtle()
        turtle.penup()
        data_s = data[data["state"] == answer_state]

        # Write the correct guess on to the map.

        turtle.goto(int(data_s.x), int(data_s.y))
        # This will allow the name of the state. +
        # turtle.write(data_s.state.item())
        turtle.write(answer_state)

diff_list = set(list_of_states) - set(guessed_state)


df = pandas.DataFrame(diff_list)
print(df.to_csv('out-1.csv'))






screen.exitonclick()