# from tkinter import *
#
# root = Tk()
# root.title('Метод_Bind')
# root.geometry('800x600+750+300')
#
# def f_event(event,key):
#     print(event, key)
#
# e = Entry(root, justify=CENTER, font="Arial 15")
# e.pack(fill=X, expand=1, padx=10, ipady=10)
# e.bind('<Button-1>', lambda event, key="Left click": f_event(event, key))
# e.bind('<Button-2>', lambda event, key="Middle click": f_event(event, key))
# e.bind('<Button-3>', lambda event, key="Right click": f_event(event, key))
#
#
# root.mainloop()

#-------------------------------------------------------------------------------------------
from tkinter import *

root = Tk()
root.title('Метод_Bind')
# root.geometry('800x600+750+300')
colors = {
    '#ff0000': 'Красный',
    '#ff7d00': 'Оранжевый',
    '#ffff00': 'Желтый',
    '#00ff00': 'Зеленый',
    '#007dff': 'Голубой',
    '#0000ff': 'Синий',
    '#7d00ff': 'Фиолетовый',
}

label = Label(root)
label.pack()
e = Entry(root, width=20, justify=CENTER)
e.pack(fill=X, expand=1, padx=10, pady=10)
# e.bind('<Button-1>', lambda event, key="Left click": f_event(event, key))
# e.bind('<Button-2>', lambda event, key="Middle click": f_event(event, key))
# e.bind('<Button-3>', lambda event, key="Right click": f_event(event, key))
e.pack()


class MyButtons():

    def __init__(self, master, text_color, hex_color):
        self.text_color = text_color
        self.hex_color = hex_color
        self.button = Button(root, bg=hex_color, command=self.get_color)
        self.button.bind('<Button-1>', lambda event, key="Left click": self.f_event(event, key))
        self.button.bind('<Button-3>', lambda event, key="Right click": self.f_event(event, key))
        self.button.pack(fill=X)

    def get_color(self):
        label['text'] = self.text_color
        e.delete(0, END)
        e.insert(0, self.hex_color)

    def f_event(self, event, key):
        if key == "Left click":
            label['bg'] = self.hex_color
        elif key == "Right click":
            e.delete(0, END)
            label['bg'] = '#fff'

for hex_color, text_color in colors.items():
    MyButtons(root, text_color, hex_color)




root.mainloop()

