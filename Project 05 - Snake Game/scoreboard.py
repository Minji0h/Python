from turtle import Turtle, color
ALIGN = "center"
FONT = ("Arial", 20, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.update_score()
        
    def update_score(self):
        self.score+=1
        self.clear()
        self.write(f"{self.score}", align=ALIGN, font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align=ALIGN, font=FONT)
    