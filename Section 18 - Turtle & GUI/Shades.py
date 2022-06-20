from turtle import *
tim = Turtle()
def draw_dashed_shapes(loki,qtd_size):
    for i in range(qtd_size):
        for i in range(10):
            loki.forward(10)
            if(loki.isdown() == True):
                loki.penup()
            else:
                loki.pendown()
        loki.left(360/qtd_size)
def draw_shapes(loki, qtd_size):
    for i in range(qtd_size):
        loki.forward(1)
        loki.right(360/qtd_size)
screen = Screen()
screen.exitonclick()