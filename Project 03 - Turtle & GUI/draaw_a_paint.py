import colorgram
import random
import turtle as t

t.colormode(255)
def new_pallet():
    pallet = colorgram.extract('teste.jpg', 6)
    return pallet 

def radom_color(pallet):
    color = random.choice(pallet)
    rgb = color.rgb
    r = rgb.r
    g = rgb.g
    b = rgb.b
    rgb = (r,g,b)
    return (r,g,b)


def draw_circle(loki):
    loki.begin_fill()
    loki.pendown()
    loki.circle(10)
    loki.penup()
    loki.forward(30)
    loki.end_fill()

def set_new_position(loki, x, y,side):
    if(side%2==0):
        loki.setposition(y-30,x+30)
        loki.setheading(180)
    else:
        loki.setposition(y+30,x+30)
        loki.setheading(0)


def draw_a_paint(loki):
    pallet = new_pallet()
    for i in range(10):
        for j in range(10):
            color = radom_color(pallet)
            loki.color(color,color)
            loki.dot(30, color)
            loki.forward(30)
        y = loki.position()[0]
        x = loki.position()[1]
        set_new_position(loki, x, y, i)

loki = t.Turtle()
loki.hideturtle()
loki.speed("fastest")
loki.penup()

draw_a_paint(loki)
screen = t.Screen()
screen.exitonclick()
