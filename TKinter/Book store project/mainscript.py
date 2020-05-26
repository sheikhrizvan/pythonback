from tkinter import *
import backend



def get_selected_row(event):
    global selected_row
    index = lb.curselection()[0]
    selected_row = lb.get(index)

    e1.delete(0,END)
    e1.insert(END,selected_row[1])

    e2.delete(0,END)
    e2.insert(END,selected_row[2])

    e3.delete(0,END)
    e3.insert(END,selected_row[3])

    e4.delete(0,END)
    e4.insert(END,selected_row[4])


def delete_command():
    backend.delete(selected_row[0])
    view_command()


def view_command():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    lb.delete(0, END)
    for row in backend.view():
        lb.insert(END, row)


def search_command():
    lb.delete(0,END)
    ttl = title_text.get()
    atr = author_text.get()
    yr = year_text.get()
    ibn = isbn_text.get()
    for row in backend.search(title=ttl, year=yr, author=atr, isbn=ibn):
        lb.insert(END, row)

def add_command():
    lb.delete(0,END)
    ttl = title_text.get()
    atr = author_text.get()
    yr = year_text.get()
    ibn = isbn_text.get()
    backend.insert(ttl,yr,atr,ibn)
    for row in backend.search(title=ttl, author=atr, year=yr, isbn=ibn):
        lb.insert(END, row)
    
def update_command():
    ttl = title_text.get()
    atr = author_text.get()
    yr = year_text.get()
    ibn = isbn_text.get()
    backend.update(id=selected_row[0],title=ttl, author=atr, isbn=ibn, year=yr)
    view_command()


  
# GUI part 
window = Tk()
window.wm_title("Book Store")


# Input fields

l1 = Label(window, text="Title")
l1.grid(row=0,column=0)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0,column=1)

l2 = Label(window, text="Author")
l2.grid(row=0,column=2)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0,column=3)

l3 = Label(window, text="Year")
l3.grid(row=1,column=0)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1,column=1)

l4 = Label(window, text="ISBN")
l4.grid(row=1,column=2)

isbn_text=StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1,column=3)


# ListBox and Buttons area

lb = Listbox(window, height=8, width=40)
lb.grid(row=2,column=0,rowspan=6, columnspan=2)

lb.bind('<<ListboxSelect>>',get_selected_row)

sb1 = Scrollbar(window)
sb1.grid(row=3, column=2, rowspan=5)

lb.configure(yscrollcommand=sb1.set)
sb1.configure(command=lb.yview)

b1 = Button(window, text="View All", width=12, command=view_command)
b1.grid(row=3,column=3)

b2 = Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=4,column=3)

b3 = Button(window, text="Add Entry", width=12, command=add_command)
b3.grid(row=5,column=3)

b4 = Button(window, text="Update Entry", width=12, command=update_command)
b4.grid(row=6,column=3)

b5 = Button(window, text="Delete Entry", width=12, command=delete_command)
b5.grid(row=7,column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=8,column=3)








window.mainloop()

