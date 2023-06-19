from tkinter import *
from tkinter import messagebox
import random
import json
import pyperclip


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    PASSWORD_LENGTH = 8

    nr_symbols = random.randint(2, 3)
    nr_numbers = random.randint(2, 3)
    nr_letters = PASSWORD_LENGTH - nr_symbols - nr_numbers

    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_letters = [random.choice(letters) for _ in range(nr_letters)]

    password_list = password_symbols + password_numbers + password_letters

    random.shuffle(password_list)

    password = "".join(password_list)
    # pyperclip.copy(password)

    password_entry.delete(0, END)
    password_entry.insert(0, password)


def add_info():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if website != "" and email != "" and password != "":
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered:\nEmail: {email}\nPassword: "
                                               f"{password}\n\nDo you want to save?")
        if is_ok:
            try:
                with open("Password Manager.json", "r") as txt:
                    data = json.load(txt)
                    data.update(new_data)

            except FileNotFoundError:
                pass

            finally:
                with open("Password Manager.json", "w") as txt:
                    json.dump(data, txt, indent=4)

                # txt.write(f"{website} | {email} | {password}\n")

            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        messagebox.showerror(title="Error", message="Please fill the empty fields!")


def search():
    website = website_entry.get()
    try:
        with open("Password Manager.json", "r") as txt:
            data = json.load(txt)
    except FileNotFoundError:
        messagebox.showinfo(title=website, message="No data file found!")
    else:
        is_found = False

        for item in data:
            if item == website:
                db_website = data[item]
                email = db_website["email"]
                password = db_website['password']
                is_found = messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
                break

        if not is_found:
            messagebox.showinfo(title=website, message=f"No data for {website} has been found!")


window = Tk()
window.title("Password Manager")
window.configure(padx=50, pady=50)

lock_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

website_search = Button(text="Search", width=13, command=search)
website_search.grid(row=1, column=2)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

password_button = Button(text="Generate Password", width=13, command=generate_password)
password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=add_info)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()