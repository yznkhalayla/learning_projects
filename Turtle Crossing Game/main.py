import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()

screen.listen()
screen.onkey(key='Up', fun=player.move_turtle_forward)
screen.onkey(key='Down', fun=player.move_turtle_backward)

car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    car_manager.create_car()

    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        car_manager.increase_speed()
        player.go_to_start()
        scoreboard.level_up(car_manager.level)

    screen.update()

screen.exitonclick()
