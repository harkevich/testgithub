# tuple
# t1 = (1, 2, 3)
# l1 = [1, 2, 3]
# t1 = 1, 2, 3
# t1 = tuple((1, 2, 3))
# t1 = ()
# t1 = (1,)

#t1 = tuple('hello')

#t1[1] = 3 нельзя добавить в котреж
#############################
# print(t1.__sizeof__()) } узнать сколько занимает места в оперативной памяти
# print(l1.__sizeof__()) }
##############################
# t1 = tuple('hello')
# t2 = tuple(' world!')
# t3 = t1 + t2
#
# print(t3)
# print(len(t3))
# print(t3.count(''))
# print(t3.index("o"))
#
# if "a" in t3:           # такого симвала в переменной t3 нет
#     print(t3.index('a'))
# else:
#     print("no")
#
# for i in t3:
#     if i == ' ':
#         continue
#     print(i, end=(' '))


t1 = (1, 2, 3,)
x = t1[0]
y = t1[1]
z = t1[2]
print(x, y, z)

x, y, z, = t1
print(x, y, z)

x = 1
y = 2
print(x, y)
x, y = y, x
print(x, y)