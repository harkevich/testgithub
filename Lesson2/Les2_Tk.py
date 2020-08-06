from tkinter import *

# from tkinter import ttk


root = Tk()
root.geometry('800x600+750+300')


def cliked():
    print('Cliked')


# btn = Button(root, bg='red', text='Кнопка', command=cliked, width=15)
# btn = Button(root, bg='red', text='Кнопка', command=cliked, font='Arial 20')
# width=15 - размер кнопки
# command=cliked - вызывает какую то функцию команду
# font='Arial 20' - шрифт кнопки + размер шрифта
btn = Button(root, text='Кнопка',)
# btn.configure(width=20, height=5)
# btn["font"] = 'Arial 15'
btn.pack()

# btn2 = ttk.Button(root, text='Кнопка') # Оформление кнопки пот операционную системую Нужен доп модульfrom tkinter import ttk
# btn2.pack()


root.mainloop()
