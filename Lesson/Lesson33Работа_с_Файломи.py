#----------Чтение файла---------------
# f = open('file.txt', encoding='UTF-8')
# text = f.read()
# text2 =text.tell()
# # text2 = f.read(8)
# # print(f.encoding) # узнать в какой кодировки файл
# f.close()
# print(text, text2)
#---------запись в файл----------------
# f = open('file.txt', 'a', encoding='UTF-8')
# f.write('Новая строка55\n') #не забывай \n для переносо строки в файле который записываешь
# f.close()

#---------запись в файл с помощью writelines----------------
# lines = ['Новая строка1', 'Новая строка2', 'Новая строка3']
# f = open('file.txt', 'a', encoding='UTF-8')
# for i in lines:
#     f.write(i + '\n')
# f.writelines(lines)
# f.writelines(f'{i}\n' for i in lines )
# f.close()
#----------Чтение файла---------------
# f = open('file.txt', 'r', encoding='UTF-8')
# f1 = f.read()
# print(f1)
# ----------------------
# with open('file.txt', 'r+') as f:  # Открываем на чтение и запись.
#     f.write('0123456789')

# ----------------readline(читает построчно) and readlines-----------------------
# with open('file.txt', encoding='utf-8') as f:
#     my_lines = f.readline()
#     my_lines2 = f.readlines()
#
# print(my_lines, my_lines2)

with open('file.txt', 'a') as f:
    f.write('0123456789')
    f.tell()  # 10
    f.write('abcdef')
    f.tell()
f2 = f.encoding
print(f2)