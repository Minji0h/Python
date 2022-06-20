import colorsys
import random
from turtle import Turtle

COLORS = ['red','orange','yellow','green','blue','purple']

class Ball(Turtle):
    def __init__(self):
        super().__init__(shape = 'circle')
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.color("white")
        self.speed(0)
        self.goto(x=0,y=0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.seth(random.randint(0,360))
    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
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
        self.color(random.choice(COLORS))