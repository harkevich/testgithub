from tkinter import *
import time


root = Tk()
root.title('clock')
root.geometry('800x600+750+300')
def tick():
    watch.after(200, tick)
    watch['text'] = time.strftime("%H:%M:%S")
watch = Label(root, font="Arial 70")
watch.pack()
tick()
root.mainloop()