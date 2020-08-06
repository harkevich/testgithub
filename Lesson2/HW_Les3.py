#--------------Кнопки--------------
from tkinter import *

root = Tk()
root.title ('Counter')
root.geometry('800x600+750+300')

a = 10
b = 5

c = 0
def Plus():
    global c
    # c = a + b
    btn_plus['text'] = a + b


def Minus():
    global c
    btn_minus['text'] = a - b

def deled():
    global c
    btn_deled['text'] = int(a / b)

def umnazenie():
    global c
    btn_umnazenie['text'] = a * b

btn_plus = Button(root, text="Plus", command=Plus, width=15)
btn_plus.pack()

btn_minus = Button(root, text="Minus", command=Minus, width=15)
btn_minus.pack()

btn_deled = Button(root, text="deled", command=deled, width=15)
btn_deled.pack()

btn_umnazenie = Button(root, text="umnazenie", command=umnazenie, width=15)
btn_umnazenie.pack()

root.mainloop()
