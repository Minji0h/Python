import turtle
import pandas

## Global Variables 
BACKGROUND = "blank_states_img.gif"
DATA = "50_states.csv"



## Initialize Screen
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(BACKGROUND)
turtle.shape(BACKGROUND)

correts = []

##Initialize Data
data = pandas.read_csv(DATA)
states = data.state.to_list()
while states != []:
    
    answer = screen.textinput(title=f"{len(correts)}/50 States Correct",prompt="What's another state's name?").title()
    if(answer == "Exit"):
        data_dict = {
            "state":states
        }
        df = pandas.DataFrame(data_dict)
        df.to_csv("states_to_learn.csv")
        break  
    
    if(answer in states):
        states.remove(answer)
        print(states)
        state_data = data[data.state == answer.title()]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x),int(state_data.y))
        t.write(f"{state_data.state.item()}")
        correts.append(answer.title())
        
turtle.mainloop()