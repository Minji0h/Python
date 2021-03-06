import json
from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- Search Pass ---------------------------------------#

def search_pass():
    website = website_input.get()

    if(website == ""):
        messagebox.showerror(
            title="ERROR", message="Please, fill in the Website field.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except:
            messagebox.showerror(title="ERROR", message="No data file found!")
        finally:
            try:
                register_data = data[website]
            except:
                messagebox.showerror(
                    title="ERROR", message="Register not found. \nPlease review the information.")
            finally:
                messagebox.showinfo(
                    title=website, message=f"These are the details: \nEmail: {register_data['email']}\nPassword: {register_data['password']}\n It's ok to save?")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def pass_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if(email == "" or website == "" or password == ""):
        messagebox.showerror(
            title="ERROR", message="Please, Fill out all the fields. ")
    else:
        ansnwer = messagebox.askokcancel(
            title=website, message=f"These are the details: \nEmail: {email}\nPassword: {password}\n It's ok to save?")
        if(ansnwer):
            try:
                with open("data.json", "r") as password_data_file:
                    data = json.load(password_data_file)
                    data.update(new_data)
                with open("data.json", "w") as password_data_file:
                    json.dump(data, password_data_file, indent=4)
            except:
                with open("data.json", "a") as password_data_file:
                    json.dump(new_data, password_data_file, indent=4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)
                website_input.focus()
                messagebox.showinfo(title="Save the password! ",
                                    message="Password save with sucess!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

# Gride Row 0
logo_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=False)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=0, columnspan=3)

# Gride Row 1
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)
website_input = Entry(width=20)
website_input.focus()
website_input.grid(row=1, column=1)
search_button = Button(text="Search", command=search_pass, width=14)
search_button.grid(row=1, column=2)

# Gride Row 2
email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)
email_input = Entry(width=38)
email_input.insert(END, "brabsma@gmail.com")
email_input.grid(row=2, column=1, columnspan=2)

# Gride Row 3
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)
password_input = Entry(width=20)
password_input.grid(row=3, column=1)
generate_button = Button(text="Generate password",
                         command=pass_generator, width=14)
generate_button.grid(row=3, column=2)

# Gride Row 3
add_button = Button(text="Add", width=32, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
