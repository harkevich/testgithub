# -----------------Untry-----------------
from tkinter import *

root = Tk()
root.geometry('800x600+750+300')

def add_str():
    e.insert(END, 'Hello')

def del_str():
    e.delete(0, END)

def get_str():
    l_text['text'] = e.get()

l = Label(root, text="Поле ввода")
l.pack()

e = Entry(root, show='*')
# e.insert(0, 'Hello')
# # e.insert(5, ' world')
# e.insert(END, ' world')
e.pack()
#
btn_add = Button(root, text='ADD', command=add_str).pack()
btn_del = Button(root, text='Del', command=del_str).pack()
btn_get = Button(root, text='Get', command=get_str).pack()

l_text = Label(root)
l_text.pack()

root.mainloop()
