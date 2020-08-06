from tkinter import *

root = Tk()
root.title('Notepad')
root.geometry('800x600+750+300')


main_menu = Menu(root)
root.config(menu=main_menu)

# main_menu.add_command(label='File')
# main_menu.add_command(label='About')

def about_program():
    print("About")


# File
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Открыть')
file_menu.add_command(label='Сохранить')
file_menu.add_separator()
file_menu.add_command(label='Выход')
main_menu.add_cascade(label='Файл', menu=file_menu)

#About
help_menu = Menu(main_menu, tearoff=0)
help_menu_sub = Menu(help_menu, tearoff=0)
help_menu_sub.add_command(label="Онлайн")
help_menu_sub.add_command(label="Оффлайн")
help_menu.add_cascade(label="Помощь", menu=help_menu_sub)
help_menu.add_separator()
help_menu.add_command(label='О программе', command=about_program)

main_menu.add_cascade(label='Справка', menu=help_menu)


# f_menu = Frame(root, bg='#1F252A', height=40)
# f_menu.pack(fill=X)
f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)






t = Text(f_text, bg='#343d46', fg='#c6dec1',padx='10', pady='10', wrap='word',
         insertbackground='#eda756', selectbackground='#4e5a65', width='5', spacing3='10')
t.pack(fill=BOTH, expand=1, side=LEFT,)

scroll = Scrollbar(f_text, command=t.yview,)
scroll.pack(fill=Y, side=LEFT)
t.config(yscrollcommand=scroll.set)



root.mainloop()