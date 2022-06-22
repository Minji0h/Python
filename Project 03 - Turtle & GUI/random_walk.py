import random
import turtle as t

directions = ['left', 'right']
angles = [0, 90, 180, 270]
loki = t.Turtle()
loki.pensize(10)
loki.hideturtle()
loki.speed(10)
t.colormode(255)

def walk(turtle, color, direction, angle, size):
    if(direction == 'left'):
        turtle.left(angle)
    else:
        turtle.right(angle)
    turtle.pencolor(color)
    turtle.forward(size)
    

def random_walk(turtle):
    color = create_color()
    direction = random.choice(directions)
    angle = random.choice(angles)
    size = random.randrange(20,100,20)
    walk(turtle, color, direction, angle, size)

def create_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

for i in range(200):
    random_walk(loki)

screen = t.Screen()
screen.exitonclick()