from tkinter import *


window = Tk()


def km_to_miles():
    t1.insert(END, "")
    a = int(e1_value.get())*1.6
    t1.insert(END, str(a))


b1 = Button(window, text = "Covert to Miles", command = km_to_miles)
# b1.pack()
b1.grid(row=0, column=1)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=0)

t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)


window.mainloop()
