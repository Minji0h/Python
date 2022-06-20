import time
import turtle as t
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

WIDHT = 800
HEIGHT = 600
COLOR = "black"
TITLE = "Pig Pong Game"

class Tela(t.Turtle):
    def __init__(self):
        super().__init__()
        self.screen = t.Screen()
        self.screen.setup(width=WIDHT,height=HEIGHT)
        self.screen.bgcolor(COLOR)
        self.screen.title(TITLE)
        self.screen.tracer(0)
        self.inicia_paddles()
        self.inicia_teclas()
        self.inicia_scoreboard()
        self.ball = Ball()
        
        
    def inicia_paddles(self):
        self.paddle_right = Paddle((350,0))
        self.paddle_left = Paddle((-350,0))

    def inicia_teclas(self):
        self.screen.listen()
        self.screen.onkeypress(key="w",fun=self.paddle_left.to_up)
        self.screen.onkeypress(key="Up",fun=self.paddle_right.to_up)
        self.screen.onkeypress(key="s",fun=self.paddle_left.to_down)
        self.screen.onkeypress(key="Down",fun=self.paddle_right.to_down)
    
    def inicia_scoreboard(self):
        self.score_r = ScoreBoard((100, 200))
        self.score_l = ScoreBoard((-100, 200))

    def valida_bola_em_tela(self):
        if self.ball.ycor() > 280 or self.ball.ycor() < -280:
            self.ball.bounce_y()
        if self.ball.distance(self.paddle_right) < 50 and self.ball.xcor() > 320 or self.ball.distance(self.paddle_left) < 50 and self.ball.xcor() < -320:
            self.ball.bounce_x()

    #Detect R paddle misses
        if self.ball.xcor() > 380:
            self.ball.reset_position()
            self.score_l.increment_score()

        #Detect L paddle misses:
        if self.ball.xcor() < -380:
            self.ball.reset_position()
            self.score_r.increment_score()

    def exit_on_click(self):
        self.screen.exitonclick()
    def update_screen(self):
        time.sleep(0.1)
        self.valida_bola_em_tela()
        self.screen.update()
        self.ball.move_ball()
