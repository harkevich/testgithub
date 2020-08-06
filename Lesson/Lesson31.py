from datetime import date
from datetime import datetime
from datetime import timedelta
import locale
#
# #---------class date
# # today = date.today()
# # print(today)          # 2020-07-13
# # print(today.day)      #13
# # print(today.month)    #7
# # print(today.year)     #2020
# # print(today.weekday()) #0 дни  недели начинаются с 0 понедельник=0, воскресенье=6
#
# #---------class datetime
# # datetime.now = datetime.today
# # now = datetime.now()    #2020-07-13 14:53:28.358231
# # now2 = datetime.today() #2020-07-13 14:53:28.358231
# # print(now)
# # print(now2)
#
# now = datetime.now()
# print(now)              #2020-07-13 14:59:14.618045
# print(now.day)          #13
# print(now.month)        #7
# print(now.year)         #2020
# print(now.weekday())    #0
# print(now.hour)         #14
# print(now.minute)       #59
# print(now.second)       #14
#
# days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
# print(days[now.weekday()])  #пн

# now =datetime.now()
# print(now.strftime('%a'))
# print(now.strftime('%A'))
#
# locale.setlocale(locale.LC_ALL, 'ru_RU')
#
# print(now.strftime('%a'))
# print(now.strftime('%A'))
#
# print(f'Дата: {now.strftime("%A, %d, %B, %Y")}')
# print(f'Время: {now.strftime("%H:%M:%S")}')
#
# print(now.strftime('%c'))
# print(now.strftime('%x'))
# print(now.strftime('%X'))


# #---------class timedelta
locale.setlocale(locale.LC_ALL, 'ru_RU')

now =datetime.now()

print(now.strftime('%c'))

d1 = now + timedelta(days=1, hours=2, minutes=10)

print(d1)
 
print(d1.strftime('%c'))