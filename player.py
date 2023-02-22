from scoreboard import Scoreboard

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle
from car_manager import CarManager

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.pu()
        self.setheading(90)
        self.stating_point()


    def go_up(self):
        if self.ycor() < FINISH_LINE_Y:
            self.forward(MOVE_DISTANCE)


    def stating_point(self):
        self.goto(STARTING_POSITION)


    def level_up(self):
        if self.ycor()>=FINISH_LINE_Y:
            return True
        else: return False