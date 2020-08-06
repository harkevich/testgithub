# def hello():
#     return 'Hello, I am func "hello'
#
#
# def super_func(func):
#     print('Hello, I am func "super_hello')
#     print(func())
#
# super_func(hello)
#-----------------------------------------------------
#
# def hello():
#     return 'Hello, I am func "hello'
#
# test = hello
#
# print(test())

#-----------------------------------------------------

# def my_decarator(func):
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')
#     return func_wrapper
# def func_test():
#     print('Hello, I am func "func_test')
#
#
# # test = my_decarator(func_test)
# # test()

#-----------------------------------------------------

# def my_decarator(func):
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')
#     return func_wrapper
#
# @my_decarator
# def func_test():
#     print('Hello, I am func "func_test')
#
#
# func_test()
#
#-----------------------------------------------------

def make_title(fn):
    def wraped():
        title = fn()
        title = title.capitalize()
        title = title.replace(',', ' ')
        return title
    return wraped
@make_title
def hi():
    return 'hello, world!'

print(hi())



