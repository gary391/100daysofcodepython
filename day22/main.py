"""
1. Create the screen
2. Create and move a paddle
3. Create another paddle
4. Create the ball and make it move
5. Detect collision with wall and bounce_y
6. Detect collision with paddle
7. Detect when paddle misses
8. Keep score

"""

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scroeboard import Scoreboard
import time




screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  # this will turn off the tracer - Now we will need to use the update method to update the screen.

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up,  "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
score_count_l = 0
score_count_r = 0

while game_is_on:
    scoreboard.score_display(score_count_l, score_count_r)
    time.sleep(ball.ball_speed)
    screen.update()
    # when we disable the animation we will need a way to update the screen manually
    # Adding the update in a while loop can help

    ball.move()


    # Detect collision with top and bottom wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        print(" Oh! Yaa Bouncing ball!!")
        ball.bounce_y()

    # Detect collision with right and left paddle.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        print("Made a contact")
        ball.bounce_x()



    # Detect R paddle misses
    if ball.xcor() > 350:
        scoreboard.score_clear()
        score_count_l = score_count_l + 1
        ball.reset()

    # Detect L paddle misses
    if ball.xcor() < -350:
        scoreboard.score_clear()
        score_count_r = score_count_r + 1
        ball.reset()




screen.exitonclick()
