import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars=[]
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        toss=random.randint(1,6)
        if toss == 1:
            new_car=Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.color(random.choice(COLORS))
            random_y=random.randint(-250,250)
            new_car.goto(300,random_y)

            self.all_cars.append(new_car)

    def move_Cars(self):
        for car in self.all_cars:
            car.forward(-1*(self.car_speed))

    def car_speed_up(self):
        self.car_speed +=STARTING_MOVE_DISTANCE




