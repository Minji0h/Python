import random
import turtle as t

t.colormode(255)
loki = t.Turtle()
loki.hideturtle()
loki.speed(10)
loki.pensize(2)

def create_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        loki.color(create_color())
        loki.circle(100)
        loki.setheading(loki.heading() + size_of_gap)

draw_spirograph(10)


screen = t.Screen()
screen.exitonclick()