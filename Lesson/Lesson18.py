# x = [1, 2, 3]
# x [0:3] = [2, 4, 6]
# print(x, id(x))
#---------------------1 ЗАДАЧА
# x = [1, 2, 3]
# y = x.copy()
# y[:3] = [2, 4, 6]
# print(x, id(x))
# print(y, id(y))
#
#
# i= [1, 2, 3]
# i2 = [x * 2 for x in i]
# print(i, id(i))
# print(i2, id(i2))

#---------------------2 ЗАДАЧА
#
# i= [1, 2, 3]
# res = 0
# for num in i:
#     res += num ** 2
# print(res)


#---------------------3 ЗАДАЧА

# w = 0.5
# t1 = 3
# t2 = 6.7
# t3 = 11.8
#
# #print(f'time1: {t1 * w},time2: {t2 * w},time3: {t3 * w}')
# print(int(t1 * w))
# print(int(t2 * w))
# print(int(t3 * w))

#---------------------4 ЗАДАЧА
s = 'Hello world!'
if ' ' in s:
    print(s.upper())
else:
    print(s.lower())
# s2 = s.lower() #  Преобразование строки к нижнему регистру
# s3 = s.upper() #  Преобразование строки к верхнему регистру
# print(s, s2, s3, sep=('\n'))