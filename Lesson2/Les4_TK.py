#-----------------Label-----------------
from tkinter import *


root = Tk()
root.geometry('800x600+750+300')



#
# l = Label(root, text="Текст в строке1\nСтрока2\nСтрока3\nСтрока4\nСтрока5",
#           bg="red", fg="#fff", font=("Comic Sans MS", 15, 'bold'),
#           justify=LEFT, width=50, height=10, anchor=E)
# l.pack()

image = PhotoImage(file="12.png") # картинки можно только в формате png
l_logo = Label(root, image=image)
l_logo.pack()



root.mainloop()