from turtle import Turtle
from car_lane import Car_lane
from crosswalk import Crosswalk


class Road(Turtle):
    def __init__(self,laness_up, laness_down):
        super().__init__()