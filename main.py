import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

car_manager=CarManager()
scoreboard=Scoreboard()
player=Player()



screen.onkeypress(player.go_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.score_board()
    car_manager.create_car()
    car_manager.move_Cars()


    #Level up part
    if player.level_up():
        player.stating_point()
        car_manager.car_speed_up()
        scoreboard.update_score()


    #colission with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on=False
            scoreboard.gameOver()



screen.exitonclick()