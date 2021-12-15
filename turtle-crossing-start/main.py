import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
level = Scoreboard()

cars = CarManager()
cars.generate_car()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(cars.increase_speed, "Down")
loop = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    loop += 1
    if loop % 6 == 0:
        cars.generate_car()
    cars.move()
    # cars.clear_cars()
    for i in cars.cars:
        if player.distance(i) < 15:
            level.game_over()
            game_is_on = False
    if player.ycor() > 280:
        level.add_score()
        cars.increase_speed()
        player.reset()


screen.exitonclick()