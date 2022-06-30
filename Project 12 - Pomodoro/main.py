from msilib.schema import ReserveCost
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    global timer
    reset_button.config(state="disabled")
    start_button.config(state="normal")
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(counter, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marker.config(text="")
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    
    global reps
    reps += 1
    start_button.config(state="disabled")
    reset_button.config(state="normal")

    if reps % 8 == 0:
        title_label.config(text="Break",fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        title_label.config(text="Break",fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        title_label.config(text="Work",fg=GREEN)
        count_down(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    minutes = count//60
    seconds = count%60

    if minutes <= 9:
        minutes = f"0{minutes}"
    if seconds <= 9:
        seconds = f"0{seconds}"

    canvas.itemconfig(counter, text=f"{minutes}:{seconds}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = reps//2
        for _ in range(work_sessions):
            marks += "✔"
        check_marker.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50,bg=YELLOW)

title_label = Label(text="Timer", font=(FONT_NAME,24,"bold"),fg=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)

tomato_image = PhotoImage(file="tomato.png")

canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=False)
canvas.create_image(100,112, image=tomato_image)
canvas.grid(row=1, column=1)

counter = canvas.create_text(100,130,text="00:00", fill="white",font=(FONT_NAME))

start_button = Button(text="Start", command=start_timer, font=(FONT_NAME,20,"bold"),fg=YELLOW, bg=GREEN)
start_button.grid(row=2, column=0)

check_marker = Label(text="", font=(FONT_NAME,24,"bold"),fg=GREEN,bg=YELLOW)
check_marker.grid(row=3,column=1)

reset_button = Button(text="Reset", command=reset_timer, font=(FONT_NAME,20,"bold"),fg=YELLOW, bg=GREEN, state="disabled")
reset_button.grid(row=2, column=2)


window.mainloop()