from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import os
from datetime import datetime

def choose_dir():
    dir_path = filedialog.askdirectory()
    e_path.delete(0, END)
    e_path.insert(0, dir_path)

def f_start():
    cur_path = e_path.get()
    if cur_path:
        for folder, subfolder, files in os.walk(cur_path):
            for file in files:
                path = os.path.join(folder, file)  # полный пууть к файлу
                mtime = os.path.getmtime(path)  # Время создание файла в секундах
                date = datetime.fromtimestamp(mtime)  # Перевод секунд в дд.мм.гг
                date = date.strftime("%Y.%m.%d")
                date_folder = os.path.join(cur_path, date) # Полный путь к папке
                if not os.path.exists(date_folder):
                    os.mkdir(date_folder)
                os.rename(path, os.path.join(date_folder, file))
        messagebox.showinfo("Success", 'Сортировка выполнена успешна')
        e_path.delete(0, END)
    else:
        messagebox.showinfo("Warning", 'Выберете папку с фотографиями')
root = Tk()
root.title('PhotoSort')
root.geometry('500x150')
s = ttk.Style()
s.configure('my.TButton', font=('Helvetica', 15))
frame = Frame(root, bg='#56adff', bd=5)
frame.pack(pady=10, padx=10, fill=X)


e_path = ttk.Entry(frame)
e_path.pack(side=LEFT, ipady=2, expand=True, fill=X)

btn_dialog = ttk.Button(frame, text='Выбрать папку', command=choose_dir)
btn_dialog.pack(side=LEFT, padx=5)

btn_start = ttk.Button(root, text='START', style='my.TButton', command=f_start)
btn_start.pack(fill=X, padx=10)




root.mainloop()