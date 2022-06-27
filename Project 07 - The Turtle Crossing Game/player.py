from turtle import Turtle
import turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("white")
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.speed(0)
        self.score = 0
    
    def to_up(self):
        new_x = self.xcor()
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(new_x,new_y)
    
    def validate_win(self):
        if(self.ycor() >= 280):
            self.goto(STARTING_POSITION)
            self.score+=1
            return True
        else:
            return False

