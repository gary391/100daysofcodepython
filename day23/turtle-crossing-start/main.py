import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

all_cars = []
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

# for _ in range(100):
#     all_cars.append(CarManager())

print(all_cars)
score_count = 0
game_is_on = True
while game_is_on:
    scoreboard.score_display(score_count)
    time.sleep(0.1)
    screen.update()
    # Here we are calling the create car method each time the update screen which is happening at 0.1 seconds
    # similarly we are calling the car move method for the same frequency
    car_manager.create_car()
    car_manager.car_move()

    # Detect collision with the car.
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect collision with the top wall.
    if player.ycor() > 290:
        scoreboard.score_clear()
        score_count = score_count + 1
        player.reset()
        car_manager.increase_car_speed()
screen.exitonclick()