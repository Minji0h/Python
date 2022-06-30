import tkinter

##Initialize Window
window = tkinter.Tk()
window.title("Mile to kilometer converter")
window.config(padx=20,pady=20)
##window.minsize(width=200, height=300)

##Função para converter o valor
def converter_value():
    mile = int(miles_input.get())
    kilometer = round(mile * 1.60934,2)
    result.config(text=f"{kilometer}")


miles_input = tkinter.Entry(width=7)
miles_input.grid(column=1,row=0)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2,row=0)

is_equal_label = tkinter.Label(text="Is equal to")
is_equal_label.grid(column=0,row=1)

result = tkinter.Label(text="0")
result.grid(column=1,row=1)

label3 = tkinter.Label(text="Km")
label3.grid(column=2,row=1)

button = tkinter.Button(text="Calculate", command=converter_value)
button.grid(column=1,row=3)




window.mainloop()