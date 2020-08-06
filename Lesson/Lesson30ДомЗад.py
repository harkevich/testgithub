import random
print('Давай поиграем в игру! Угадай число.')
# p = random.randint(1, 100)
# c = 0
# c += 1
while True:
    p = random.randint(1, 100)
    c = 0
    while True:
        p2 = int(input('Введи число: '))
        c += 1
        if p2 == p:
            print("Поздравляем Вы угадали")
            print('Вы отгадали за ', c, 'попыток')
            break
        elif p2 > p:
            print('Ваше число Больше загаданного числа')
        elif p2 < p:
            print('Ваше число Меньше загаданного')
    print('Хотитее сыграть сново? нажмите y/n')
    i = str(input('Сделай свой выбор: '))
    if i == 'y':
        print('Играем заново')
    elif i == 'n':
        print('Спасибо за игру')
        break