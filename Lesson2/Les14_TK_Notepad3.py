from tkinter import *

root = Tk()
root.title('Notepad')
root.geometry('800x600+750+300')


main_menu = Menu(root)
root.config(menu=main_menu)

def about_program():
    print("About")

def change_theme(theme):
    t['bg'] = theme_colors[theme]['text_bg']
    t['fg'] = theme_colors[theme]['text_fg']
    t['insertbackground'] = theme_colors[theme]['cursor']
    t['selectbackground'] = theme_colors[theme]['select_bg']

# File
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Открыть')
file_menu.add_command(label='Сохранить')
file_menu.add_separator()
file_menu.add_command(label='Выход')
main_menu.add_cascade(label='Файл', menu=file_menu)

#Theme
theme_menu = Menu(main_menu, tearoff=0)
theme_menu_sub = Menu(theme_menu, tearoff=0)
theme_menu_sub.add_command(label="Light Theme", command=lambda:change_theme('light'))
theme_menu_sub.add_command(label="Dark Theme", command=lambda:change_theme('dark'))
theme_menu.add_cascade(label="Офорление", menu=theme_menu_sub)
theme_menu.add_separator()
theme_menu.add_command(label='О программе', command=about_program)
main_menu.add_cascade(label='Справка', menu=theme_menu)

f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

theme_colors = {
    'dark': {
        'text_bg': '#343d46', 'text_fg': '#fff', 'cursor': '#eda756', 'select_bg': '#4e5a65'

    },
    'light': {
        'text_bg': '#fff', 'text_fg': '#000', 'cursor': '#8000ff', 'select_bg': '@777'
    }
}

t = Text(f_text, bg=theme_colors['dark']['text_bg'], fg=theme_colors['dark']['text_fg'], padx='10',
         pady='10', wrap='word', insertbackground=theme_colors['dark']['cursor'],
         selectbackground=theme_colors['dark']['select_bg'],
         width='5', spacing3='10', font=('Courier New', 11))
t.pack(fill=BOTH, expand=1, side=LEFT,)

scroll = Scrollbar(f_text, command=t.yview,)
scroll.pack(fill=Y, side=LEFT)
t.config(yscrollcommand=scroll.set)



root.mainloop()