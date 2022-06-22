from road import Road
from screen import screen

roads = []
for i in range(5):
    lines_up = screen.window_width()/5*-i
    lines_down = screen.window_width()/5*-i
    roads.append(Road(lines_up,lines_down))
screen.exitonclick()