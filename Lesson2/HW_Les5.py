#------------------Включил в себя 6, 7, 8 урок------------------
#-----------------------------------------Радуга----------------------
#--------------------------------------Первый способ------------------
# from tkinter import *
#
# root = Tk()
# root.title ('Радуга')
# root.geometry('300x220+750+300')
#
# def krasny():
#     cvet.delete(0, END)
#     kod.delete(0, END)
#     cvet.insert(END, 'Красный')
#     kod.insert(END, '#ff0000')
# def orandjevy():
#     cvet.delete(0, END)
#     kod.delete(0, END)
#     cvet.insert(END, 'Оранжевый')
#     kod.insert(END, '#ff7d00')
# def djolty():
#     cvet.delete(0, END)
#     kod.delete(0, END)
#     cvet.insert(END, 'Желтый')
#     kod.insert(END, '#ffff00')
# def zeleny():
#     cvet.delete(0, END)
#     kod.delete(0, END)
#     cvet.insert(END, 'Зеленый')
#     kod.insert(END, '#00ff00')
# def goludoi():
#     cvet.delete(0, END)
#     kod.delete(0, END)
#     cvet.insert(END, 'Голубой')
#     kod.insert(END, '#007dff')
# def siniy():
#     cvet.delete(0, END)
#     kod.delete(0, END)
#     cvet.insert(END, 'Синий')
#     kod.insert(END, '#0000ff')
# def violetovyi():
#     cvet.delete(0, END)
#     kod.delete(0, END)
#     cvet.insert(END, 'Фиолетовый')
#     kod.insert(END, '#7d00ff')
# cvet = Entry(root)
# cvet.pack()
# kod = Entry(root)
# kod.pack()
#
# btn_krasny = Button(root, bg='#ff0000', command=krasny)
# btn_krasny.pack(fill=X)
#
# btn_orandjevy = Button(root, bg='#ff7d00', command=orandjevy)
# btn_orandjevy.pack(fill=X)
#
# btn_djolty = Button(root, bg='#ffff00', command=djolty)
# btn_djolty.pack(fill=X)
#
# btn_zeleny = Button(root, bg='#00ff00', command=zeleny)
# btn_zeleny.pack(fill=X)
#
# btn_goludoi = Button(root, bg='#007dff', command=goludoi)
# btn_goludoi.pack(fill=X)
#
# btn_siniy = Button(root, bg='#0000ff', command=siniy)
# btn_siniy.pack(fill=X)
#
# btn_violetovyi = Button(root, bg='#7d00ff', command=violetovyi)
# btn_violetovyi.pack(fill=X)
#
# root.mainloop()



#-------------------------------------Второй способ---------------------------
# from tkinter import *
#
# root = Tk()
# root.title('Радуга')
# root.geometry('300x220+750+300')
#
#
# cvet = Entry(root)
# cvet.pack()
# kod = Entry(root)
# kod.pack()
#
# def krasny():
#     cvet.delete(0, END)
#     kod.delete(0, END)
#     cvet.insert(END, 'Красный')
#     kod.insert(END, '#ff0000')
# def orandjevy():
#     cvet.delete(0, END)
#     kod.delete(0, END)
#     cvet.insert(END, 'Оранжевый')
#     kod.insert(END, '#ff7d00')
# def djolty():
#     cvet.delete(0, END)
#     kod.delete(0, END)
#     cvet.insert(END, 'Желтый')
#     kod.insert(END, '#ffff00')
# def zeleny():
#     cvet.delete(0, END)
#     kod.delete(0, END)
#     cvet.insert(END, 'Зеленый')
#     kod.insert(END, '#00ff00')
# def goludoi():
#     cvet.delete(0, END)
#     kod.delete(0, END)
#     cvet.insert(END, 'Голубой')
#     kod.insert(END, '#007dff')
# def siniy():
#     cvet.delete(0, END)
#     kod.delete(0, END)
#     cvet.insert(END, 'Синий')
#     kod.insert(END, '#0000ff')
# def violetovyi():
#     cvet.delete(0, END)
#     kod.delete(0, END)
#     cvet.insert(END, 'Фиолетовый')
#     kod.insert(END, '#7d00ff')
#
# btn_cvet = {
# Button(root, bg='#ff0000', command=krasny).pack(fill=X),
# Button(root, bg='#ff7d00', command=orandjevy).pack(fill=X),
# Button(root, bg='#ffff00', command=djolty).pack(fill=X),
# Button(root, bg='#00ff00', command=zeleny).pack(fill=X),
# Button(root, bg='#007dff', command=goludoi).pack(fill=X),
# Button(root, bg='#0000ff', command=siniy).pack(fill=X),
# Button(root, bg='#7d00ff', command=violetovyi).pack(fill=X)
# }
#
#
# root.mainloop()

#-------------------------------------Третий способ---------------------------

#
# from tkinter import *
#
# root = Tk()
# root.title('Радуга')
# root.geometry('300x220+750+300')
# def get_color(text_color, hex_color):
#     l['text']= text_color
#     e.delete(0, END)
#     e.insert(END, hex_color)
# l = Label(root)
# e = Entry(root, width=30, justify=CENTER)
# l.pack()
# e.pack()
# btn_cvet = {
# Button(root, bg='#ff0000', command=lambda: get_color('Красный', '#ff0000')).pack(fill=X),
# Button(root, bg='#ff7d00', command=lambda: get_color('Оранжевый', '#ff7d00')).pack(fill=X),
# Button(root, bg='#ffff00', command=lambda: get_color('Желтый', '#ffff00')).pack(fill=X),
# Button(root, bg='#00ff00', command=lambda: get_color('Зеленый', '#00ff00')).pack(fill=X),
# Button(root, bg='#007dff', command=lambda: get_color('Голубой', '#007dff')).pack(fill=X),
# Button(root, bg='#0000ff', command=lambda: get_color('Синий', '#0000ff')).pack(fill=X),
# Button(root, bg='#7d00ff', command=lambda: get_color('Фиолетовый', '#7d00ff')).pack(fill=X)
# }
#
# root.mainloop()

#-------------------------------------Четвертый способ---------------------------

# from tkinter import *
#
# root = Tk()
# root.title('Радуга')
# root.geometry('300x220+750+300')
#
#
# def get_color(text_color, hex_color):
#     l['text']= text_color
#     e.delete(0, END)
#     e.insert(0, hex_color)
#
#
# l = Label(root)
# e = Entry(root, width=30, justify=CENTER)
# l.pack()
# e.pack()
#
# colors = {
#     '#ff0000': 'Красный',
#     '#ff7d00': 'Оранжевый',
#     '#ffff00': 'Желтый',
#     '#00ff00': 'Зеленый',
#     '#007dff': 'Голубой',
#     '#0000ff': 'Синий',
#     '#7d00ff': 'Фиолетовый',
# }
#
# for k, v in colors.items():
#     Button(root, bg=k, command=lambda text_color=v,hex_color=k: get_color(text_color,
#                                                                           hex_color)).pack(fill=X)
#
# root.mainloop()


#-------------------------------------Пятый способ---------------------------
from tkinter import *

root = Tk()
root.title('Радуга')
root.geometry('300x220+750+300')
l = Label(root)
e = Entry(root, width=30, justify=CENTER)
l.pack()
e.pack()
colors = {
    '#ff0000': 'Красный',
    '#ff7d00': 'Оранжевый',
    '#ffff00': 'Желтый',
    '#00ff00': 'Зеленый',
    '#007dff': 'Голубой',
    '#0000ff': 'Синий',
    '#7d00ff': 'Фиолетовый',
}
class MyButtons():
    def __init__(self, master, text_color, hex_color):
        self.text_color = text_color
        self.hex_color = hex_color
        self.button = Button(root, bg=hex_color, command=self.get_color)
        self.button.pack(fill=X)
    def get_color(self):
        l['text'] = self.text_color
        e.delete(0, END)
        e.insert(0, self.hex_color)

for k, v in colors.items():
    MyButtons(root, v, k)

root.mainloop()