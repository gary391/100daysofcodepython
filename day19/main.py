# Event Listeners


from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# In order to start listening for event we will have to use
# listen function of the screen. We will have to bind a function
# that will be triggered when a particular key is pressed on the keyboard.

# In order to bind a key stroke to an event in our code, we will have to
# use a onkeyrelease

"""
Function as Inputs 
Passing function as an argument to another function
Here we don't need to use parenthesis 

w=forward
s=backward
a=counter clockwise
d=clockwise
c=clear drawing 
"""


def move_forwards():
    tim.forward(10)


def move_backward():
    tim.backward(10)

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def counter_clockwise():
    tim.left(10)
#
def clockwise():
    tim.right(10)



screen.listen()
# Using positional arguments
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_drawing)


screen.exitonclick()

