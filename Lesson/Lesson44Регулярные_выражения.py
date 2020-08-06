#
# s = 'Это просто строка текста. А это ещё одна строка текстаю'
#
# pattern  = 'строка'
#
# print(s.find(pattern))
# print(pattern in s)
#-----------------------------------------------------
# import re
# s = 'Это просто строка текста. А это ещё одна строка текстаю'
#
# pattern  = 'строка'
#
# if re.search(pattern, s):
#     print('Matched')
# else:
#     print('No_Matched')
#-----------------------------------------------------
# import re
# s = 'Это просто строка текста. А это ещё одна строка текстаю'
#
# pattern = 'строка'
#
# if re.search(pattern, s):
#     print('Matched')
# else:
#     print('No_Matched')
#
# match = re.search(pattern, s)
#
# print(match)
#-----------------------------------------------------
# import re
# s = 'Это просто строка текста. А это ещё одна строка текстаю'
#
# pattern = 'строка'
# pattern2 = 'Это'
# pattern3 = 'это'
#
# print(re.match(pattern, s))
# print(re.match(pattern2, s)) # регистро зависимый метод поиска. Находит только первое совподение
# print(re.match(pattern3, s))
#-----------------------------------------------------

# import re
# s = 'Это просто строка текста. А это ещё одна строка текстаю'
#
# pattern = 'строка'
#
# print(re.findall(pattern, s)) # Находит все совподения в списке
#-----------------------------------------------------

# import re
# s = 'Это просто строка текста. А это ещё одна строка текстаю.'
#
# pattern = 'строка'
#
# print(re.split('.', s))# Разделяет строку по заданному заблону
# print(re.split('\.', s))
# print(re.split(r'\.', s))
# print(re.split(r'\.', s, 1)) # 1 указывает на одно разделение строки

# #-----------------------------------------------------
#
# import re
# s = '''Это просто строка текста.
# А это ещё одна строка текстаю.
# А это строка с цифрами: 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10
# А это сторока с разными символами: "!", "@", "-", "&", "?", "_"
# a\\b\tc
# test string
# '''
#
# pattern = r'\w' #получает все симловы кроме специальных
# pattern2 = r'\w+' # получает слова + цифры кроме специальных
# print(re.findall(pattern, s))
# print(re.findall(pattern2, s))
#-----------------------------------------------------
#
# import re
# s = '''Это просто строка текста.
# А это ещё одна строка текстаю.
# А это строка с цифрами: 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10
# А это сторока с разными символами: "!", "@", "-", "&", "?", "_"
# a\\b\tc
# test string
# '''
#
# pattern = r'[]'
#
# print(re.findall(pattern, s))

# Функция для валидации email

import re
s = "mail@mail.com"


def validate_email(email):
    # return re.match(r'^.+@\w+\.[a-z]{2,6}$', email, re.IGNORECASE)
    # return re.match(r'^.+@(\w+\.){0,2}[a-z]{2,6}$', email, re.IGNORECASE)
    return bool(re.match(r'^.+@(\w+\.){0,2}[a-z]{2,6}$', email, re.IGNORECASE))

print(validate_email("mail@mail.com"))
print(validate_email("ivanov@mail"))
print(validate_email("mail@mail.com.ru"))