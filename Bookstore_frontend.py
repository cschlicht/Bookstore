from tkinter import *
import Bookstore_backend
window = Tk()
window.title("Bookstore")
#window.geometry("600x330")


def view_command():
    list1.delete(0,END)
    for row in Bookstore_backend.view():
        list1.insert(END, row) 


def search_command():
    list1.delete(0, END)
    for row in Bookstore_backend.search(title_value.get(), author_value.get(), year_value.get(), isbn_value.get()):
        list1.insert(END, row)

def insert_command():
    list1.delete(0,END)
    Bookstore_backend.insert(title_value.get(), author_value.get(), year_value.get(), isbn_value.get())
    list1.insert(END, (title_value.get(), author_value.get(), year_value.get(), isbn_value.get()))

def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        title.delete(0,END)
        author.delete(0,END)
        year.delete(0,END)
        isbn.delete(0,END)

        title.insert(END, selected_tuple[1])
        author.insert(END, selected_tuple[2])
        year.insert(END, selected_tuple[3])
        isbn.insert(END, selected_tuple[4])
    except IndexError:
        pass
def delete_command():
    Bookstore_backend.delete(selected_tuple[0])

def update_command():
    Bookstore_backend.update(selected_tuple[0], title_value.get(), author_value.get(), year_value.get(), isbn_value.get())

def close():
    window.destroy()

b1 = Button(window, text = "View All", width = 12, command = view_command)
b1.grid(row = 2, column = 4)

b1 = Button(window, text = "Search Entry", width = 12, command = search_command)
b1.grid(row = 3, column = 4)

b1 = Button(window, text = "Add Entry", width = 12, command = insert_command)
b1.grid(row = 4, column = 4)

b1 = Button(window, text = "Update Selected", width = 12, command = update_command)
b1.grid(row = 5, column = 4)

b1 = Button(window, text = "Delete Selected", width = 12, command = delete_command)
b1.grid(row = 6, column = 4)

b1 = Button(window, text = "Close", width = 12, command = close)
b1.grid(row = 7, column = 4)

title_value = StringVar()
title =Entry(window, textvariable = title_value)
title.grid(row=0, column= 2)

year_value = StringVar()
year =Entry(window, textvariable = year_value)
year.grid(row=1, column= 2)

author_value = StringVar()
author =Entry(window, textvariable = author_value)
author.grid(row=0, column= 4)

isbn_value = StringVar()
isbn =Entry(window, textvariable = isbn_value)
isbn.grid(row=1, column= 4)

price_value = StringVar()
price=Entry(window, textvariable = isbn_value)
price.grid(row=2, column= 2)


l1 = Label(text = "Title")
l1.grid(row = 0, column = 1)

l2 = Label(text = "Author" )
l2.grid(row = 0, column = 3)

l3 = Label(text = "ISBN" )
l3.grid(row = 1, column = 3)

l4 = Label(text = "Year" )
l4.grid(row = 1, column = 1)

l4 = Label(text = "Price" )
l4.grid(row = 2, column = 1)


list1 = Listbox(window, height= 6, width= 35)
list1.grid(row = 2, column = 1, rowspan = 6, columnspan = 2)
list1.bind('<<ListboxSelect>>', get_selected_row)


sb1=Scrollbar(window)
sb1.grid(row = 4, column = 3, rowspan = 2)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)


window.mainloop()