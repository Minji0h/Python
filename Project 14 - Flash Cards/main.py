from tkinter import *
from tkinter import messagebox
from turtle import color
import pandas
import random
## Constants
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
DATA_FILE = "data\\words_to_learn.csv" 


## Globals

current_card = {}
##   Load data

try:
    with open(DATA_FILE, 'r') as data_file:
        data = pandas.read_csv(data_file)
        to_learn = data.to_dict(orient="records")
except FileNotFoundError:
    with open("data\\french_words.csv", 'r') as data_file:
        data = pandas.read_csv(data_file)
        to_learn = data.to_dict(orient="records")
else:
    messagebox.showerror(title="ERROR", message="No data file found!")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas_background.itemconfig(image_background, image=card_front_image)
    canvas_background.itemconfig(label_title, text="Frech", fill="black")
    canvas_background.itemconfig(label_word, text=f"{current_card['French']}", fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    global current_card
    canvas_background.itemconfig(image_background, image=card_back_image)
    canvas_background.itemconfig(label_title, text="English", fill="white")
    canvas_background.itemconfig(label_word, text=f"{current_card['English']}", fill="white")

def know_word():
    global current_card, to_learn
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv(DATA_FILE,index=False)
    next_card()

#Initialize the windows
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40,bg=BACKGROUND_COLOR)

#Create the images
card_back_image = PhotoImage(file="images\card_back.png")
card_front_image = PhotoImage(file="images\card_front.png")
right_image = PhotoImage(file="images\\right.png")
wrong_image = PhotoImage(file="images\wrong.png")

#Create the canvas backgroung
canvas_background = Canvas(width=800, height=526, highlightthickness=False, bg=BACKGROUND_COLOR)
image_background = canvas_background.create_image(410, 270, image=card_front_image)
label_title = canvas_background.create_text(400, 150, text='Title',font=(FONT_NAME, 40, 'italic'))
label_word =  canvas_background.create_text(400,263, text="Word", font=(FONT_NAME, 60,'bold'))
canvas_background.grid(row=0, column=0, columnspan=5, rowspan=3)


#Create the buttons
right_button = Button(image=right_image,highlightthickness=False,borderwidth=0, command=know_word)
right_button.grid(row=4, column=1, padx=20, pady=20)
wrong_button = Button(image=wrong_image, highlightthickness=False,borderwidth=0, command=next_card)
wrong_button.grid(row=4, column=3, padx=20, pady=20)



flip_timer = window.after(3000, func=flip_card)
next_card()



window.mainloop()