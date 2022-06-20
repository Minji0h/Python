import turtle as t

screen = t.Screen()
screen.setup(width=660,height=600)
screen.bgcolor("black")
screen.title("My Snack Game")

class snack():
    def __init__(self):
        self.body = []
        self.body.append(body_segment(0,0))
        self.body.append(body_segment(-20,0))
        self.body.append(body_segment(-40,0))
    def move_snack(self):
        for segment in self.body:
            segment.move_segment()
    def grow(self):
        return 0
def body_segment(pos_x, pos_y):
    new_segment = t.Turtle(shape="square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(x=pos_x, y=pos_y)
    return new_segment
    def move_segment(self):
        self.forward(10)
    def get_pos_x(self):
        return self.pos_x
    def get_pos_y(self):
        return self.pos_y

##cobrinha = snack()
teste = body_segment(0,0)
teste.move_segment()
teste.move_segment()
teste.move_segment()
teste.move_segment()
screen.exitonclick()

