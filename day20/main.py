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
from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) # this will turn off the tracer - Now we will need to use the update method to update the screen.

# Create a snake body
# dimension of turtle object is 20X20


snake = Snake()
food = Food()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#Move the snake
game_is_on = True
score_count = 0
while game_is_on:
    scoreboard.score_display(score_count)
    screen.update()
    time.sleep(0.1)
    snake.move()


    # Detect collision of food with the snake
    # for this you can use distance method of the turtle
    if snake.head.distance(food) < 15:
        print(" Oh! Yaa delicious")
        # Create a score board using the turtle write
        scoreboard.score_clear()
        score_count = score_count + 1
        snake.extend()
        food.refresh()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()


    # Detect collision with tail
    # snake.head = snake.segments[-1]
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()
    # if the head collides with any segment in the tail:
        # trigger game_over




screen.exitonclick()
