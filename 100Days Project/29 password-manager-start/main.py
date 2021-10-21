from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get().title()
    email = email_entry.get()
    username = username_entry.get().title()
    password = password_entry.get()
    new_data = {
        email: {
            website: {
                "username": username,
                "password": password,
            }
        }
    }

    if len(website) == 0 or len(password) == 0 or len(username) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: "
                                                              f"\nEmail: {email} "
                                                              f"\nUsername: {username}"
                                                              f"\nPassword: {password} "
                                                              f"\nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", mode="r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:

                with open("data.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                # Updating old data with new data
                if email in data:
                    data[email].update(new_data[email])

                else:
                    data.update(new_data)

                with open("data.json", mode="w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)

            finally:
                website_entry.delete(0, END)
                username_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- Search --------------------------------- #

def search():
    website = website_entry.get().title()
    email = email_entry.get()

    if len(website) == 0 or len(email) == 0:
        messagebox.showinfo(title="Sorry", message="Search function request input email and website.")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            messagebox.showinfo(title="Sorry", message="This user message has not been saved.")

        else:
            if email in data and website in data[email]:
                user_message = data[email][website]
                text = f"Email: {email}" \
                       f"\nUsername: {user_message['username']}" \
                       f"\nPassword: {user_message['password']}"
                pyperclip.copy(user_message['password'])
                messagebox.showinfo(title=website, message=text)

            else:
                messagebox.showinfo(title="Sorry", message="This user message has not been saved.")


# ---------------------------- UI SETUP ------------------------------- #

# window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=30)

# canvas
canvas = Canvas(width=330, heigh=100)
logo_img = PhotoImage(file="kksecuritymedium.png")
canvas.create_image(165, 50, image=logo_img)
canvas.grid(column=0, row=0, columnspan=3)

# labels
website_label = Label(text="Website name:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email account:")
email_label.grid(column=0, row=2)

username_label = Label(text="Username:")
username_label.grid(column=0, row=3)

password_label = Label(text="Password:")
password_label.grid(column=0, row=4)

# entries
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=40)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "tan040724101445@gmail.com")

username_entry = Entry(width=40)
username_entry.grid(column=1, row=3, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=4)

# button
search_button = Button(text="Search", width=14, highlightthickness=0, command=search)
search_button.grid(column=2, row=1)

generate_button = Button(text="Generate Password", highlightthickness=0, command=generate_password)
generate_button.grid(column=2, row=4)

add_button = Button(text="Add", width=34, highlightthickness=0, command=save_password)
add_button.grid(column=1, row=5, columnspan=2)

window.mainloop()
