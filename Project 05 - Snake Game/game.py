import time
import turtle as t
from food import Food
from scoreboard import ScoreBoard
import snake as s

screen = t.Screen()

snake = s.snake()
food = Food()
game_is_on = True

screen.setup(width=660,height=600)
screen.bgcolor("black")
screen.title("My Snack Game")
screen.tracer(0)
screen.onkeypress(key="a",fun=snake.to_left)
screen.onkeypress(key="Left",fun=snake.to_left)
screen.onkeypress(key="d",fun=snake.to_right)
screen.onkeypress(key="Right",fun=snake.to_right)
screen.onkeypress(key="w",fun=snake.to_up)
screen.onkeypress(key="Up",fun=snake.to_up)
screen.onkeypress(key="s",fun=snake.to_down)
screen.onkeypress(key="Down",fun=snake.to_down)
screen.listen()
scoreBoard = ScoreBoard()
while game_is_on == True:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    if(snake.head.distance(food)<20):
        food.new_position()
        time.sleep(0.1)
        snake.new_segment()
        scoreBoard.update_score()
    if(snake.head.xcor()>290) or (snake.head.ycor()>290) or (snake.head.xcor() <-290) or (snake.head.ycor() <-290):
        screen.update()
        game_is_on = False
        scoreBoard.game_over()
    if snake.valida_batida() == True:
        screen.update()
        game_is_on = False
        scoreBoard.game_over()
    
screen.exitonclick()
