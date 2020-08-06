# ---------------------- 14 урок ДомЗад Таблица умнажения
# print('\t\t\t\tТаблица умнажения ')
# for i in range (1, 10):
#     print('Унажение на ', i)
#     for j in range(2,10):
#         print(f'{j} * {i} = {i * j}', end="\t")
#     print(" ")
# else:
#     print('DONE')
# # year = 1
# # while year <= 20:
# #     print(year, end=" ")
# #     year += 1
# # print(l9)
# #
# # print(f'2 * 1 = {2 * 1 }')
# # print(f'2 * 1 = {2 * 1 }')
# # for j in range(1, 11):
# #     print(f'\tВнутоенний цикл #{j}')

# -------------20 урок ДомЗад
# ----- Задача1
# 1 решение
# words = ['мадам', 'топот', 'test', 'madam', 'world']
# words2 = []
# for word in words:
#     if word == word[::-1]:
#         words2.append(word)
# print(words2)
# # 2 решение
# pal = [word for word in words if word == word[::-1]]
# print(pal)

# ----- Задача2
# my_str = ['Око за око','А роза упала на лапу Азора','Около Миши молоко']
# words2 = []
# for word in my_str:
#     word_r = word.replace(' ', '')
#     word_r = word_r.lower()
#     if word_r == word_r [::-1]:
#         words2.append(word)
# print(words2)
# -------------24 урок ДомЗад

# print('Давай поиграем в игру! Угадай число.')
# p = 50
# c = 0
# while True:
#     p2 = int(input('Введи число: '))
#     c += 1
#     if p2 == p:
#         print("Поздравляем Вы угадали")
#         break
#     elif p2 > p:
#         print('Ваше число Больше загаданного числа')
#     elif p2 < p:
#         print('Ваше число Меньше загаданного')
#
#
#
# print('Вы отгадали за ', c, 'попыток')
#

# -------------------26 ДомЗад
# ----------Таблица умнажения через пользовательскую функцию
# print('\t\t\t\tТаблица умнажения ')
#
#
def tabl(a, b):
    for i in range(a, b):
        # print('Унажение на ', i)
        for j in range(a, b):
            print(f'{j} * {i} = {i * j}', end="\t")
        print(" ")
    else:
        print('DONE')
tabl(2, 5) # не забывай указать

# ------------------Сколько выпьет воды пример из 18 урока
# def water(a, b, f):
#     w = 0.5
#     t1 = a
#     t2 = b
#     t3 = f
#     print(f'time1: {t1 * w},time2: {t2 * w},time3: {t3 * w}')
#     print(int(t1 * w))
#     print(int(t2 * w))
#     print(int(t3 * w))
# water(5, 9, 15.5)
#------------------Проверка на провел (если есть пробел то писать прописными буквами есди нет то все с маленькой )det
def set_register(s):
    #s = reg
    if ' ' in s:
        print(s.upper())
    else:
        print(s.lower())
set_register('МенязовутИван')