#--------- Коментируйте функции

#
# def get_sum(a, b):
#     """
#     Сумирует аргументы a и b.
#
#     :param a: Первый оперант
#     :type a:int
#
#     :param b: Второй оперант
#     :type b:int
#
#     :return: return type int
#     """
#     return a + b
#
# print(get_sum(1, 2))

#----------------------
# a = 5 # global
# def f():
#     a = 10 # local
#     a += 1
#     print(a)
# print(a)
# f()
# print(a)
#-----------------------
# a = 5
# def f1():
#     global a
#     a += 1
# print(a)
# f1()
# print(a)
#---------------------
l = [1, '2', 3]

def f3(l):
    return [i * 2 for i in l]

print(f3(l))

#----------------------

l = [1, '2', 3]
def f4(l):
    def get_mult(x):
        return x * 2
    return [get_mult(i) for i in l]
print(f4(l))

#-----------------------------


l = [1, '2', 3]
def f5(l):
    def get_mult(x):
        if isinstance(x, int):
            return x *2
    return [get_mult(i) for i in l if get_mult(i)]
print(f5(l))


#-----------------------------



l = [1, '2', 3]
def f6(l):
    def get_mult(x):
        return x *2
    return list(map(get_mult, l))
print(f6(l))


