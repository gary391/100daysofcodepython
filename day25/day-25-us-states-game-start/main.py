from turtle import Screen, Turtle
import pandas
screen = Screen()

turtle = Turtle()
screen.title("U.S. States Games")
# You can load the image as a shape of the turtle
image = "blank_states_img.gif"
screen.addshape(image)
# Once you have added the image to the screen,
# then it is available to the turtle
turtle.shape(image)
total_count = 50
guessed_state = []
# print(f'answer_state: {answer_state}')

'''
1. Convert the guess to Title case
2. Check if the guess is among the 50 states
3. Write correct guesses onto the map 
4. Use a loop allow the user to keep guessing
5. Record the correct guesses in a list 
6. Keep track of the score
'''

data = pandas.read_csv("50_states.csv")
all_states = (data["state"].tolist())

while len(guessed_state) < 50:
    answer_state = screen.textinput(title =f"{len(guessed_state)}/{total_count} States Correct",
                                        prompt="What's another state's name?").title()
    print(answer_state)
    if answer_state == "Exit":
        break
    # If answer_state is one of the states in all the states of the 50 states csv
    if answer_state in all_states: # This can only work if you have a list
        guessed_state.append(answer_state)
        turtle = Turtle()
        turtle.hideturtle()
        turtle.penup()
        # If they got it correct:
            # Create a turtle to write the name of the state at the state's x
            # and y coordinate
        correct_state = data[data["state"] == answer_state]
        turtle.goto(int(correct_state.x), int(correct_state.y))
        turtle.write(correct_state.state.item())

#states to learn.csv
diff = set(all_states) - set(guessed_state)
new_data = pandas.DataFrame(list(diff))
new_data.to_csv("states_to_learn.csv")

# with open ("states_to_learn.csv", "w") as file:
#     file.write(not_guessed_states)





screen.exitonclick()