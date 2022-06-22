import colorsys
import random
import time
from turtle import Turtle
import turtle

PALLET = [(33, 28, 64), (45, 44, 64), (229, 209, 222),
          (199, 202, 217), (116, 129, 140)]

turtle.colormode(255)


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape='circle')
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        color = random.choice(PALLET)
        self.color(color)
        self.speed(0)
        self.goto(x=0, y=0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.seth(random.randint(0, 360))

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        time.sleep(self.move_speed)
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.ball_change_color()

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
        self.ball_change_color()

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

    def ball_change_color(self):
        self.color(random.choice(PALLET))
