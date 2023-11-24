'''
1. Create a snake body
2. Move the snake
3. control the snake
4. Detect collision with food
5. Create a scoreboard
6. Detect collision with the wall
7. Detect collision with the tail
'''

from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) # this will turn off the tracer - Now we will need to use the update method to update the screen.

# Create a snake body
# dimension of turtle object is 20X20


snake = Snake()



screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#Move the snake
game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()


    # move each of the segments
    # for seg in segments:
    #     seg.forward(20)
        # This will update the screen for each segment
        # screen.update()




screen.exitonclick()
