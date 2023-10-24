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
repcounter = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global repcounter
    repcounter = 0
    checks.config(text='')
    window.after_cancel(timer)
    label_timer.config(text='Timer', fg=GREEN)
    img.itemconfig(clock, text='00:00')


# ---------------------------- TIMER MECHANISM ------------------------------- #

# incredibly unnecesary function but it makes the code easier to read
def changetext(text, color):
    label_timer.config(text=text, fg=color)


def startcountdown():
    global repcounter
    repcounter += 1

    if repcounter == 8:
        repcounter = 0
        checks.config(text='')
        changetext("Break", "red")
        countdown(LONG_BREAK_MIN * 60)
    elif repcounter % 2 == 0:
        changetext("Break", PINK)
        countdown(SHORT_BREAK_MIN * 60)
    else:
        changetext("Work", GREEN)
        countdown(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(counter=5):
    minutes = int(counter / 60)
    seconds = counter % 60
    if minutes < 10:
        minutes = f"0{minutes}"
    if counter < 10:
        seconds = f"0{seconds}"
    if seconds == 0:
        seconds = "00"
    display = f"{minutes}:{seconds}"
    img.itemconfig(clock, text=display)
    if counter != 0:
        counter -= 1
        global timer
        timer = window.after(1000, countdown, counter)
    elif counter == 0:
        global repcounter
        print(repcounter % 2)
        if repcounter == 8:
            checks.config(text="Long Break Time!")
        elif repcounter % 2 == 1:
            check = '️'
            for i in range(0, repcounter, 2):
                check += '✔️'
            checks.config(text=check)
        startcountdown()


# ---------------------------- UI SETUP ------------------------------- #

# Main Window
window = Tk()
window.title("Pomodorororo")
window.config(padx=100, pady=50, bg=YELLOW)

# 'Timer' title
label_timer = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))

# Image and countdown text
img = Canvas(width=210, height=234, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file='tomato.png')
img.create_image(103, 122, image=image)
clock = img.create_text(105, 140, text='00:00', font=(FONT_NAME, 35, "bold"))

# Buttons start and reset, label for check marks
start = Button(text="Start", command=startcountdown)
reset = Button(text="Reset", command=reset)
checks = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 16, 'normal'))

label_timer.grid(column=1, row=0)
img.grid(column=1, row=1)
start.grid(column=0, row=2)
checks.grid(column=1, row=2)
reset.grid(column=2, row=2)

window.mainloop()
