"""
Reeborg was exploring a dark maze and the battery in its flashlight ran out.

Write a program using an if/elif/else statement so Reeborg can find the exit. 

The secret is to have Reeborg follow along the right edge of the maze, 
turning right if it can, going straight ahead if it can’t turn right,
or turning left as a last resort.

What you need to know
The functions move() and turn_left().
Either the test 
                front_is_clear()
                wall_in_front()
                right_is_clear()
                wall_on_right()
                at_goal().
How to use a while loop and if/elif/else statements.
It might be useful to know how to use the negation of a test (not in Python).

"""
def turn_around():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while (not at_goal()):

    # Check if right is clear 
    if(right_is_clear()):
        turn_right()
        move()
    elif (front_is_clear()):
        move()
    elif(wall_in_front()):
        turn_right()
    elif(wall_on_right()):
        turn_left()

        