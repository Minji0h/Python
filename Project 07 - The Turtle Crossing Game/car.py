import time
from turtle import Turtle

PALLET = []
STRETCH_WID = 2
STRETCH_LEN = 4

WIDTH = 500

class Car(Turtle):
    def __init__(self, HEIGHT) -> None:
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=STRETCH_WID, stretch_len=STRETCH_LEN)
        self.color("purple")
        self.setposition(WIDTH,HEIGHT)

    def move_car(self, distance):
        time.sleep(0.1)
        new_x = self.xcor() - distance
        new_y = self.ycor()
        self.goto(new_x, new_y)

