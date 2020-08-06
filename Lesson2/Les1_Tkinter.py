# import tkinter
from tkinter import *


root = Tk()
root.title('Мое первое GUI приложение')
root.iconbitmap("icon1.ico")
root.geometry('800x600+750+300')
root.resizable(False, False) # Запрет на изменения размера окна
# root.config(bg="green") #Можно указать как название цвета так и код цвета
root['bg'] = 'red'



root.mainloop()