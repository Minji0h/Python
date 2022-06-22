from turtle import Turtle, color
ALIGN = "center"
COLOR = "white"
FONT = ("Courier", 80, "normal")

class ScoreBoard(Turtle):
    def __init__(self,position):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color(COLOR)
        self.goto(position)
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"{self.score}", align=ALIGN, font=FONT)

    def increment_score(self):
        self.score+=1
        self.update_score()
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align=ALIGN, font=FONT)
    