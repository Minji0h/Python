import turtle as t

class Drawing():
    def __init__(self):
        self = t.Screen()
        self.listen()
        self.onkeypress(key="w",fun=move_fowards)
        self.onkeypress(key="s",fun=move_backwards)
        self.onkeypress(key="a",fun=move_counter_clockwise)
        self.onkeypress(key="d",fun=move_clockwise)
        self.onkeypress(key="c",fun=clear)
        self.exitonclick()
def move_fowards():
    loki.forward(10)
def move_backwards():
    loki.backward(10)
def move_counter_clockwise():
    head = loki.heading() + 10
    loki.setheading(head)
def move_clockwise():
    head = loki.heading() - 10
    loki.setheading(head)
def clear():
    loki.clear()
    loki.penup()
    loki.home()
    loki.pendown()
loki = t.Turtle()

screen = Drawing()



