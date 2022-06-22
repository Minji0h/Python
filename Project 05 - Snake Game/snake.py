from pickle import FALSE
import random
import turtle as t
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
PALLET = [(33,28,64),(45,44,64),(229,209,222),(199,202,217),(116,129,140)]
t.colormode(255)

class snake():
    def __init__(self):
        self.snake = []
        self.color = random.choice(PALLET) 
        self.add_segment((0, 0))
        self.add_segment((-20, 0))
        self.add_segment((-40, 0))
        self.head = self.snake[0]
        
        

    def add_segment(self, pos):
        segment = t.Turtle(shape="square")
        segment.color(self.color)
        segment.penup()
        segment.goto(pos)
        segment.speed(0)
        self.snake.append(segment)

    def new_segment(self):
        self.add_segment(self.snake[-1].position())

    def move_snake(self):
        for seg in range(len(self.snake)-1, 0, -1):
            new_x = self.snake[seg-1].xcor()
            new_y = self.snake[seg-1].ycor()
            new_heading = self.snake[seg-1].heading()
            self.go_heading = new_heading
            self.snake[seg].goto(x=new_x, y=new_y)
        self.head.forward(20)
        
    def valida_batida(self):
        for i in self.snake[1:]:
            if(self.head.distance(i)<=10):
                return True
        return False

    def to_right(self):
        if(self.head.heading() != LEFT):
            self.head.setheading(RIGHT)

    def to_up(self):
        if(self.head.heading() != DOWN):
            self.head.setheading(UP)

    def to_left(self):
        if(self.head.heading() != RIGHT):
            self.head.setheading(LEFT)

    def to_down(self):
        if(self.head.heading() != UP):
            self.head.setheading(DOWN)
