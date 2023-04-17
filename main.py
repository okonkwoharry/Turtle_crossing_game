import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280
MOVE_INCREMENT = 0
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
scoreboard = Scoreboard()
list_of_car = []

n_of_loop = 0
required_loop = 6
screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    n_of_loop += 1
    time.sleep(0.1)
    screen.update()
    if n_of_loop >= required_loop:
        new_car = CarManager()
        list_of_car.append(new_car)
        n_of_loop = 0
    for car in list_of_car:
        car.move(MOVE_INCREMENT)
        # detect when player collides with a car
        if player.distance(car) < 30:
            game_is_on = False
            scoreboard.game_over()
        if player.ycor() > FINISH_LINE_Y:
            scoreboard.update_level()
            player.reset_position()
            MOVE_INCREMENT += 10
            required_loop -= 1.2


screen.exitonclick()
