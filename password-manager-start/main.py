from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for x in range(nr_letters)] + [random.choice(symbols) for x in
                                                                           range(nr_symbols)] + [random.choice(numbers)
                                                                                                 for x in
                                                                                                 range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    if len(password_input.get()) > 0:
        password_input.delete(0, END)
        password_input.insert(END, password)
        pyperclip.copy(password)
    else:
        password_input.insert(END, password)
        pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

# website_input = website_input.get()
#
def save_password():
    new_data = {website_input.get(): {"email": email_input.get(),
                                      "password": password_input.get(),
                                      }
                }
    if len(website_input.get()) == 0 or len(password_input.get()) == 0 or len(email_input.get()) == 0:
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        try:
            messagebox.showinfo(title=f"{website_input.get()} Info", message=f"Email: {data[website_input.get()]['email']} "
                                                                             f"\nPassword: {data[website_input.get()]['password']}")
        except KeyError:
            messagebox.showinfo(title="Error", message="This account does not exist")




# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=21)
website_input.grid(column=1, row=1, columnspan=1, sticky="we")
website_input.focus()

search_button = Button(text="Search", command=search_password)
search_button.grid(column=2, row=1, sticky="we")

# Email

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, sticky="we")

email_input = Entry(width=35)
email_input.insert(END, "test@gmail.com")
email_input.grid(column=1, row=2, columnspan=2, sticky="we")

# Password

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="we")

password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky="we")

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3, sticky="we")

# Add

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="we")

window.mainloop()
