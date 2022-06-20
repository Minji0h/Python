from turtle import Turtle
class Crosswalk(Turtle):
    def __init__(self, lane_up, lane_down) -> None:
        super().__init__()
        self.lane_up = lane_up
        self.lane_down = lane_down
