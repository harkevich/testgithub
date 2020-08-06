# --------------1 Задача-------------------
#------1 способ----
# arr = ['even', 4, 'even', 7,'odd', 'even', 55, 'test', 6, 'even', 10,  3, 'even', 0]
# arr1 = ['even', 3, 'even', 7,'odd', 'even', 55, 'test', 6, 'even', 10,  3, 'even', 0]
# arr2 = ['even', 3, 'odd', 7, 0]
# def func(a):
#     arr1 = arr.index(a)
#     arr2 = [i for i in arr if i == arr1]
#     arr3 = ''.join(map(str, arr2))
#     arr4 = str(arr1)
#     if arr3 == arr4:
#         return ("True")
#     else:
#         return ('False')
# print(func('odd'))
#------2 способ----
# def func(a):
#     arr1 = a.index('odd')
#     for poz in arr:
#         if poz == arr1:
#             print("True")
#             break
#     else:
#         print('False')
#
# func(arr2)

# #------3 способ ----
# def odd_ball(arr, n):
#     return arr.index(n) in arr
# print(odd_ball(['even', 4, 'even', 7,'odd', 'even', 55, 'test', 6, 'even', 10,  3, 'even', 0], 'odd'))
# print(odd_ball(['even', 3, 'even', 7,'odd', 'even', 55, 'test', 6, 'even', 9,  3, 'even', 0], 'odd'))
# print(odd_ball(['even', 4, 'even', 7,'odd'],'odd'))


# ------------------2 задача -------------------------
# ------1 решение -------
# def find_sum(a):
#     posl = list(range(a + 1))
#     s = sum([chi for chi in posl if chi % 3 == 0 or chi %5==0 ])
#     print(s)
# find_sum(5)

# ------2 решение ------
# def find_sum2(t):
#     posl = list(range(t + 1))
#     a = []
#     b = []
#     # s = aa+bb
#     for chi in posl:
#         if chi % 3 == 0:
#             # print(chi)
#             a.append(chi)
#     for chi2 in posl:
#
#         if chi2 % 5 == 0:
#             # print(chi2)
#             b.append(chi2)
#     aa = sum(a)
#     bb = sum(b)
#     s = aa + bb
#     # print(aa)
#     # print(bb)
#     print(s)
#     # find_sum2(5)
# find_sum2(10)

# ------3 решение ------
#
# def find_sum(n):
#     res = 0
#     for i in range(n + 1):
#         if i % 3 == 0 or i % 5 == 0:
#             res += i
#     return res
# print(find_sum(5))
# print(find_sum(10))

# ------4 решение ------
# def find_sum2(n):
#     return sum(i for i in range(n + 1) if i % 3 == 0 or i % 5 == 0)
#
# print(find_sum2(5))
# print(find_sum2(10))
# -----------------3 Задача
# ------1 решение ------
# names = ['Ryan', 'Kieran', 'John', 'David', 'Paul']
# def get_names():
#     new_names = []
#     for n in names:
#         if len(n) == 4:
#             new_names.append(n)
#     print(new_names)
# get_names()

# ------2 решение ------.
# names = ['Ryan', 'Kieran', 'John', 'David', 'Paul']
# def get_names(names):
#     return [i for i in names if len(i) == 4]
# print(get_names(names))
