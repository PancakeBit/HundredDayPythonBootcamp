from tkinter import *
from os import path
from pyperclip import copy
from tkinter import messagebox
import json

# IMPORTANT - should also add some way to update passwords,
# as of now it's possible to have multiple website/username with different passwords
# This can lead to redundancy within the file, but should work within the code
# It will just take the latest added password as the current password
# When it displays that website/username

# Using JSON instead of Pandas for data retrieval


FONT = ("Courier Prime",12)

def search():
    try:
        with open('database.json', 'r') as database:
            database = json.load(database)
    except FileNotFoundError:
        messagebox.showinfo(title="File Not Found", message="You have not added data yet\nPlease 'Add' your info'")
        return
    else:
        if len(website_entry.get()) == 0:
            return
    # If the file exists, continue
    # Make database file into dictionary
    # This one can't be put into a dictionary comprehension
    web = website_entry.get().strip()
    ema = email_entry.get().strip()

    # Attempt to get password
    try:
        pas = database[web][ema]
    # If KeyError is encountered it means that that website/email combo does not exist
    except KeyError:
        messagebox.showinfo(title="Data Not Found", message="That Website/Username is not within the database, please double check your spelling\n\nNote: This is CASE SENSITIVE")
    else:
        messagebox.showinfo(title=f"{web}", message=f"Email/Username: {ema}\nPassword: {pas}\n\nPassword copied to clipboard!")
        copy(pas)

def password_generator():
    # Password Generator Project from day 5, modified by instructor
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    rletters = [random.choice(letters) for _ in range(nr_letters)]
    rnumbers = [random.choice(numbers) for _ in range(nr_numbers)]
    rsymbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = rletters + rnumbers + rsymbols
    random.shuffle(password_list)

    password = ''.join(password_list)
    pass_entry.delete(0, END)
    pass_entry.insert(0, password)
    copy(password)

def write_to_database():
    # BEGIN DATA WRITE TO FILE
    # ---- There's probably a better way of doing this, but this is what I'm thinking of
    # ---- will keep thinking of better solution
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = pass_entry.get().strip()

    store = {website: {email : password}}

    if not path.exists('database.json'):
        # if the path DOES NOT exist, then just write the given data
        with open('database.json', 'w') as database:
            json.dump(store, database, indent=4)
    else:
        # if the path DOES exist, read through the data and check if the data has been given before
        # if the data is unique, write it to the file
        # if the data is NOT unique, do nothing because it's already in the file
        with open('database.json', 'r') as database:
            data = json.load(database)
        try:
            data[website].update({email:password})
        except KeyError:
            data.update(store)
        with open('database.json', 'w') as database:
            json.dump(data, database, indent=4)
def addclick():
    # if Website or Password is left blank, show message and return
    # username is optional?
    if len(website_entry.get()) == 0 or len(pass_entry.get()) == 0:
        messagebox.showinfo(title="Blank Lines", message="Please do not leave Website or Password Blank")
        return

    # if user answers no to the question, return
    confirm = messagebox.askokcancel(title=website_entry.get(), message='Is it OK to save?\nPlease double check your Username/Password')
    if not confirm:
        return

    write_to_database()

    website_entry.delete(0, END)
    #email_entry.delete(0, END) !!!!!! I don't like the email being erased, i'll keep it in
    pass_entry.delete(0, END)

mainwindow = Tk()
#mainwindow.geometry(f"{WIDTH}x{HEIGHT}")
mainwindow.config(padx=20, pady=20)
mainwindow.title("Password Manager")

# Logo image
canvas = Canvas(width=200, height=200)
img = PhotoImage(file='logo.png')
canvas.create_image((img.width() / 2), (img.height() / 2), image=img)
canvas.grid(column=0, row=0, columnspan=5)

# Website Row
website_label = Label(text = "Website: ", font = FONT)
website_entry = Entry(width = 21)
website_entry.focus()
search_button = Button(text="Search", command=search)

website_label.grid(column=0, row=1,sticky='e')
website_entry.grid(column=1, row=1)
search_button.grid(column=2, row=1, sticky='nsew')

# Email Row
# Read for the most used email in emaildata (using mode in the email column)
most_frequent_email = ''

email_label = Label(text = "Email/Username: ", font = FONT)
email_entry = Entry(width = 35)
email_label.grid(column=0, row=2, sticky='e')
email_entry.insert(0, most_frequent_email)
email_entry.grid(column=1, row=2, columnspan=2)

# Password Row and Button
pass_label = Label(text = "Password: ", font = FONT)
pass_entry = Entry(width=21)
generate = Button(text="Generate", command=password_generator)
pass_label.grid(column=0, row=3, sticky='e')
pass_entry.grid(column=1, row=3, sticky='nsew')
generate.grid(column=2, row=3)

# Add Button
add = Button(text="Add", width=30, command=addclick)
add.grid(column=1, row=4, columnspan=2)

mainwindow.mainloop()
