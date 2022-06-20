

from turtle import Turtle

UP = 90
DOWN = 270
FORWARD = 20
STRETCH_WID = 5
STRETCH_LEN = 1

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=STRETCH_WID, stretch_len=STRETCH_LEN)

    def to_up(self):
        new_x = self.xcor()
        new_y = self.ycor()+10
        self.goto(new_x,new_y)

    def to_down(self):
        new_x = self.xcor()
        new_y = self.ycor()-10
        self.goto(new_x,new_y)