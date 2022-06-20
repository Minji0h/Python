import random
import turtle as t



screen = t.Screen()
screen.setup(width=500,height=400)

colors = ['red','orange','yellow','green','blue','purple']



class Game():
    def __init__(self):
        self.user_bet = int(screen.numinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: \n 1- Red \n 2- Orange \n 3- Yellow \n 4 - Green \n 5 - Blue \n 6 - Purple"))
        while self.user_bet not in range(6):
            self.user_bet = int(screen.numinput(title="Make your bet",prompt="Color don't existe! Which turtle will win the race? Enter a color:"))
        self.user_bet = colors[self.user_bet]
        self.runner = []
        self.is_race_on = True
    def inicia_game(self):
        x_position = -230
        y_position = 100
        for i in range(6):
            self.runner.append(t.Turtle(shape="turtle"))
            self.runner[i].penup()
            self.runner[i].color(colors[i])
            self.runner[i].goto(x=x_position, y=y_position)
            y_position-=30
    def race(self):
        while self.is_race_on:
            for runner in self.runner:
                if(runner.xcor() > 230):
                    winner = runner.pencolor()
                    self.is_race_on = False
                    if (winner == self.user_bet):
                        print(f"You won! The {winner} turtle is the winner!")
                    else:
                        print(f"You lose! The {winner} turtle is the winner!")
                distance = random.randint(0,10)
                runner.forward(distance)


game = Game()
game.inicia_game()
game.race()
screen.exitonclick()