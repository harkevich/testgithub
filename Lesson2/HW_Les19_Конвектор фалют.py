from tkinter import *
from tkinter import ttk
import urllib.request
import json
from tkinter import messagebox

root = Tk()
root.title('Конвертор валют')
root.geometry('800x600+750+300')
root. resizable(False, False)

SMART_AMOUNT = 1000

def exchenge():
    pass

header_frame = Frame(root)
header_frame.pack(fill=X)



req = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
# req_read = req.content  # Преабразуем в список

req_json = req.json()

# print(req_json, type(req_json))

i = []
for val in req_json:
    print(val.keys())
    # if i in val:
    #     print(i)

#
# label = Label(root, bg='red')
# label.pack(fill=X, ipady=250)
#
# e = Entry(root, justify=CENTER)
# e.pack(fill=X, expand=1, padx=10, pady=10)
#
# btn = Button(root, text='Расчитать')
# btn.pack(padx=10, pady=10)


# root.mainloop()