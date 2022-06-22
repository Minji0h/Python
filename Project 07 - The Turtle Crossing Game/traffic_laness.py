import time
from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")
class Traffic_laness(Turtle):
    def __init__(self, setY):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.setheading(180)
        self.setx(screen.window_width()/2)
        self.sety(setY)
        self.draw_traffic_laness()
    def draw_traffic_laness(self):
        while self.xcor() > -screen.window_width()/2:
            self.forward(20)
            if(self.isdown() == True):
                self.penup()
            else:
                self.pendown()
    def clear(self) -> None:
        return super().clear()
    def ycor(self) -> float:
        return super().xcor()