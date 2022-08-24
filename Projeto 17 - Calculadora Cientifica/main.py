import numbers
from tkinter import *
window = Tk() 
window.title('Calculadora')
window.config(padx=20, pady=20) 

numbers_input = Label(width=50, height=5 , borderwidth=1, text="abacate", relief="solid")
numbers_input.grid(row=0, column=0, columnspan=3)


button_number1 = Button(text="1", width=6, height=3)
button_number2 = Button(text="2", width=6, height=3)
button_number3 = Button(text="3", width=6, height=3)
button_number1.grid(row=2, column=0)
button_number2.grid(row=2, column=1)
button_number3.grid(row=2, column=2)

button_number4 = Button(text="4", width=6, height=3)
button_number5 = Button(text="5", width=6, height=3)
button_number6 = Button(text="6", width=6, height=3)
button_number4.grid(row=3, column=0)
button_number5.grid(row=3, column=1)
button_number6.grid(row=3, column=2)

button_number7 = Button(text="7", width=6, height=3)
button_number8 = Button(text="8", width=6, height=3)
button_number9 = Button(text="9", width=6, height=3)
button_number7.grid(row=4, column=0)
button_number8.grid(row=4, column=1)
button_number9.grid(row=4, column=2)





window.mainloop()