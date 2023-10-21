import tkinter

window = tkinter.Tk()
window.title("Simple")
window.minsize(500,500)

def btnclick():
    btn1.config(text=input.get())

btn1 = tkinter.Button(text="Click Me!", command=btnclick)
input = tkinter.Entry(width=10)

input.pack()
btn1.pack()

window.mainloop()