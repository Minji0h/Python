import random
from turtle import Turtle, speed
import time
PALLET = [(3, 62, 140), (3, 76, 140), (22, 95, 140),
          (155, 209, 242), (242, 242, 240)]
STRETCH_WID = 1
STRETCH_LEN = 2
INIT_X = 310

MIN_Y = -249
MAX_Y = 260

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(PALLET))
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=STRETCH_WID, stretch_len=STRETCH_LEN)
        self.ypos = random.choice(range(MIN_Y, MAX_Y, 40))
        self.xpos = INIT_X
        self.goto(self.xpos, self.ypos)

    def move_car(self):
        self.xpos = self.xpos - 10
        self.goto(self.xpos, self.ypos)

    def still_car_in_screen(self):
        if(self.xcor() <= -300):
            self.xpos = INIT_X
            self.ypos = random.choice(range(MIN_Y, MAX_Y, 40))

