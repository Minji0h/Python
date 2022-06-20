from tela import Tela
from scoreboard import ScoreBoard
from ball import Ball
screen = Tela()

game_is_true = True

while game_is_true:
    screen.update_screen()


screen.exit_on_click()