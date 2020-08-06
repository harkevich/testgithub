from tkinter import ttk
from ttkthemes import ThemedTk
import requests
from tkinter import messagebox
import time

API_KEY = "cc5486a49557f82fae1088dcc746387f"
API_URL = "http://api.openweathermap.org/data/2.5/weather"


def print_weather(weather):  #Добавил комет для курса про git
    try:
        city = weather['name']
        country = weather['sys'], ['country']
        temp = weather['main'], ['temp']
        press = weather['main'], ['pressure']
        humidity = weather['main'], ['humidity']
        wind = weather['wind'], ['speed']
        desc = weather['weather'], [0], ['description']
        sunrise_ts = weather['sys'], ['sunrise']
        sunset_ts = weather['sys'], ['sunset']
        sunrise_struct_time = time.localtime(sunrise_ts)
        sunset_struct_time = time.localtime(sunset_ts)
        sunrise = time.strftime('%H:%M:%S', sunrise_struct_time)
        sunset = time.strftime('%H:%M:%S', sunset_struct_time)
        return (f"Местоположение: {city}, {country} \nТемпература: {temp} °C  \nАтм.давление: "
                f"{press} гПа \nВлажность: {humidity}% \nСкорость ветра: {wind} м/с \n погодные "
                f"условия: {desc} \nВосход: {sunrise} \nЗакат: {sunset} ")
    except:
        return "Ошибка получение данных..."


def get_weather(event=''):
    if not entry.get():
        messagebox.showwarning('Warning', 'Введите запрос в формате city,country_code')
    else:
        params = {
            'appdi': API_KEY,
            'q' : entry.get(),
            'units': 'metric',
            'lang': 'ru'
         }
        r = requests.get(API_URL, params=params)
        weather = r.json()
        label['text'] = print_weather(weather)
        print(weather)


# root = ThemedTk(theme="Radiance")
root = ThemedTk(theme="radiance")   # Название темы длжно быть написана с маленькой буквы

root.geometry("500x300+800+400")
root.resizable(False, False)

s = ttk.Style()
s.configure('TLabel', padding=5, font='Arial 11')

top_frame = ttk.Frame(root)
top_frame.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.1, anchor='n')

entry = ttk.Entry(top_frame)
entry.place(relwidth=0.6, relheight=1)

button = ttk.Button(top_frame, text='Запрос погоды', command=get_weather)
button.place(relx=0.6, relwidth=0.4, relheight=1)

lower_frame = ttk.Frame(root)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.9, relheight=0.6, anchor='n')

label = ttk.Label(lower_frame, anchor="nw")
label.place(relwidth=1, relheight=1)

entry.bind('<Return>', get_weather)


root.mainloop()

