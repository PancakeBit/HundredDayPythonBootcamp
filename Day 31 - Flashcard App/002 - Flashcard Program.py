from tkinter import *
from tkinter import messagebox
import pandas
from random import choice

#Global Variables
BLUE = "#B1DDC6"
LANG_FONT = ('Arial', 30, 'italic')
TEXT_FONT = ('Arial', 60, 'bold')
FOREIGN = 'Japanese'
TRANSLATED = 'English'
try:
    WORDS = pandas.read_csv('data/jpFrequent.csv')
except FileNotFoundError:
    messagebox.showinfo(title="File not Found", message="You do not yet have a database CSV file, please acquire one first")
    exit()
words_dict = {}
foreign = ""
timer = None

# Would much rather ^Foreign and Translated variables be read from the dataframe, but it would
# take up too much memory i think. Definitely doable, but not worth the trouble
# of accounting for the edge cases should the csv not have a header and such

# Giving up on checking for the mistakes file, would require too much code rewriting
# i still hate pandas

# TODO: If a user marks an item as a mistake, save that mistake to a csv and load it FIRST on the next session
# i.e. When a user mistakes 'I' and 'when', they get added to a csv.
# When the user opens the program they must get 'I' and 'when' correct before
# going back to the original file

# def checkForMistakes():
#     try:
#         print("checking")
#         words = pandas.read_csv('data/words_to_learn.csv')
#         mistakes = {item.Japanese: item.English for (index, item) in words.iterrows()}
#         print(mistakes)
#         return mistakes
#     except FileNotFoundError:
#         print("error")
#         return {}

def display():
    #set the card to the front
    canvas.itemconfig(card, image=mainimage)
    global words_dict
    global timer
    global foreign
    # If the dictionary is empty, repopulate
    # also if data isn't compatible this will not work
    if len(words_dict)==0:
        try:
            words_dict = {item.Japanese:item.English for (index, item) in WORDS.iterrows()}
        except AttributeError as err:
            messagebox.showinfo(title=str(err), message="CSV File not properly formatted, please fix")
            exit()
    foreign = choice(list(words_dict.keys()))

    canvas.itemconfig(language, text=FOREIGN)
    canvas.itemconfig(text, text=foreign)

    timer = mainwindow.after(1000, showtranslated, foreign)

def showtranslated(foreign):
    canvas.itemconfig(card, image=backimage)
    canvas.itemconfig(language, text=TRANSLATED)
    canvas.itemconfig(text, text=words_dict[foreign])

def correct():
    global timer
    mainwindow.after_cancel(timer)
    # Pop the correct item out of the dictionary
    # Because the user got it correct they don't need it anymore this session
    words_dict.pop(foreign)
    print(words_dict)
    display()

def wrong():
    global timer
    mainwindow.after_cancel(timer)
    # mistake = {foreign:words_dict[foreign]}
    # dataframe = pandas.DataFrame([mistake])
    # dataframe.to_csv('data/words_to_learn.csv', mode='w', index=False)
    display()

def firstbuttonpress():
    # First, check if there exists a learn.csv
    global words_dict
    # words_dict = checkForMistakes()

    check.config(command=correct)
    x.config(command=wrong)
    display()

mainwindow = Tk()
mainwindow.title("Flashy - Card")
mainwindow.config(bg=BLUE, padx=50, pady=20)

# Create card
mainimage = PhotoImage(file='images/card_front.png')
backimage = PhotoImage(file='images/card_back.png')
# UI for the flash card
image_width = mainimage.width()
image_height = mainimage.height()
canvas = Canvas(width=image_width, height=image_height, bg=BLUE, highlightthickness=0)
card = canvas.create_image((image_width / 2), (image_height / 2), image=mainimage)
language = canvas.create_text(image_width / 2, (image_height / 2)-140, text='To Begin the test', font=LANG_FONT)
text = canvas.create_text(image_width / 2, image_height / 2, text='Press Either \nButton Below', font=TEXT_FONT)
canvas.grid(column=0, row=0, columnspan=2)
ch = PhotoImage(file='images/right.png')
ex = PhotoImage(file='images/wrong.png')

check = Button(image=ch, bd=0, highlightthickness=0, command=firstbuttonpress)
x = Button(image=ex, bd=0, highlightthickness=0, command=firstbuttonpress)

# Button Frame grid
check.grid(column=0, row=1)
x.grid(column=1, row=1)

mainwindow.mainloop()