import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()
screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
# to create multiple cars and move them
    car.create_car()
    car.move_cars()

# to detect collision of my turtle with cars
    for any_car in car.all_cars:
        if any_car.distance(player) <= 20:
            game_is_on = False
            score.game_over()

# to detect when turtle reaches the top
    if player.is_at_finish_line():
        player.go_to_start()
        car.level_up()
        score.increase_level()

screen.exitonclick()