# def get_sum(a, b, c=0, d=9):
#     print(a, b, c, d)
#     return a + b + c + d
#
#
# print(get_sum(1,3,d=6))


# def get_sum(*args):   # - *args пазиционные аргументы (Любое кол-во переменных будет преабразован в кортеж)

# def get_sum(**kwargs):# - **kwags (ключевые слова) именнованные аргументы(Любое кол-во переменных будет преабразован в словарь)
# def get_sum2(*args):
#     print(sum(args))
#
# get_sum2(1, 5, 9 ,8)

# def func(**kwargs):
#     print(kwargs)
#
# func(a=1, c=20, d=6)

def f(a, x, *args, **kwargs):
    print(a)
    print(x)
    print(args)
    print(kwargs)
f(1, 2, 3, 4, b='test', c='hi')