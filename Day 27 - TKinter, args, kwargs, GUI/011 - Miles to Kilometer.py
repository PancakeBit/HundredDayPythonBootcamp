from tkinter import *

window = Tk()
window.config(padx=20, pady=20)
window.minsize(height=115,width=255)
window.title("Miles-Kilometer Converter")

def use_converter():
    num = convertfrom.get()
    if num.isnumeric() == False:
        return
    num = float(num)
    num *= 1.60934
    num = round(num, 2)
    convertto.config(text=num)

convertfrom = Entry(width=10, justify=CENTER)
convertfrom.insert(0, "0")
convertfromlabel = Label(text="Miles")

isequalto = Label(text='Is equal to')
convertto = Label(text="0")
converttolabel = Label(text='Kilometers')

calculate = Button(text='Calculate!', command=use_converter)

convertfrom.grid(column=1, row=0)
convertfromlabel.grid(column=2, row=0)

isequalto.grid(column=0, row=1)
convertto.grid(column=1, row=1)
converttolabel.grid(column=2, row=1)

calculate.grid(column=1, row=2)

window.mainloop()