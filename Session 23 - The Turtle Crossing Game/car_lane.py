from turtle import Turtle
from car import Car
from traffic_laness import Traffic_laness

class Car_lane(Turtle):
    def __init__(self, lane_up_y, lane_down_y):
        self.cars = []
        self.lane_up_y = lane_up_y
        self.lane_down_y = lane_down_y
        self.traffic_lane_up = Traffic_laness(self.lane_up_y)
        self.traffic_lane_down = Traffic_laness(self.lane_down_y)
    def add_a_car(self, center):
        self.cars.append(Car(center))
    def move_cars_on_lane(self):
        for i in self.cars:
            i.move_car(40)
    def get_lane_up_y(self):
        return self.lane_up_y
    def get_lane_down_y(self):
        return self.lane_down_y