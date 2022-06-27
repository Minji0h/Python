import turtle
from player import Player
from turtle import Screen
from car_manager import Car_manager
from scoreboard import ScoreBoard


turtle.colormode(255)


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

scoreboard = ScoreBoard()
car_manager = Car_manager()
player = Player()

screen.onkeypress(key="Up",fun=player.to_up)
GAME_IS_ON = True

while GAME_IS_ON:
    if(player.validate_win()):
        scoreboard.update_score()
        car_manager.next_level()
    car_manager.manager_cars()
    if(car_manager.validate_crash(player)):
        scoreboard.game_over()
        car_manager.clear_cars()
        GAME_IS_ON = False
    screen.update()

screen.exitonclick()
