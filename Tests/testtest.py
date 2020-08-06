# # arr = ['even', 4, 'even', 1, 'odd', 'even', 55, 'test', 6, 'even', 10, 3, 'even']
# #
# #
# # def func(a):
# #     arr1 = a.index('odd')
# #     for poz in arr:
# #         if poz == arr1:
# #             print("True")
# #             break
# #     else:
# #         print('False')
# #
# # func(arr)
#
# # ------------------------------------------------------------------------
#
# # arr = ['even', 4, 'even', 7, 'odd', 'even', 55, 'test', 6, 'even', 10, 3, 'even', 0]
# # def func(a):
# #     arr1 = arr.index(a)
# #     arr2 = [poz for poz in arr if poz == arr1]
# #     arr3 = ''.join(map(str, arr2))
# #     arr4 = str(arr1)
# #     if arr3 == arr4:
# #         return ("True")
# #     else:
# #         return ('False')
# # print(func('odd'))
# # # print(func('odd'))
# import os
# import os.path
# #
# #
# # def list_files(startpath):
# #     for root, dirs, files in os.walk(startpath):
# #         level = root.replace(startpath, ' ').count(os.sep)
# #         indent = ' ' * 4 * (level)
# #         print('{}{}/'.format(indent, os.path.basename(root)))
# #     subindent = ' ' * 4 * (level + 1)
# #     for d in dirs:
# #         print('{}{}'.format(subindent, d))
# #     subindent2 = ' ' * 4 * (level + 1)
# #     for f in files:
# #         print('{}/'.format(subindent2,f))
# #
# # print(list_files('D:\\test\\'))
#
# def test(n):
#     for d in os.walk(n):
#         l = d.os.path.split(n)
#         i = ' ' * 4 * l
#         print(i)
#
#
#
# test('D:\\test\\')

# list1list1list1 = [1, 3, 5, 9, 13]
# list2list2list2 = [2, 4, 6, 7, 15]
# def simple_mer2e(list1, list2):
#     i, j = 0, 0
#     res = []
#     while i < len(list1) and j < len(list2):
#         if list1[i] < list2[j]:
#             res.append(list1[i])
#             i += 1
#         else:
#             res.append(list2[j])
#             j += 1
#     res += list1[i:]
#     res += list2[j:]
#     # один из list1[i:] и list2[j:] будет уже пустой, поэтому добавится только нужный остаток
#     return res
# print(simple_merge([1, 3, 5, 9, 13], [14,16, 6, 7, 15]))
#
# a = [1, 3, 5, 9, 13]
# b = [12, 4, 16, 7, 15, 22, 33]
# def iter_merge(list1, list2):
#     result, it1, it2 = [], iter(list1), iter(list2)
#     el1 = next(it1, None)
#     el2 = next(it2, None)
#     while el1 is not None or el2 is not None:
#         if el1 is None or (el2 is not None and el2 < el1):
#             result.append(el2)
#             el2 = next(it2, None)
#         else:
#             result.append(el1)
#             el1 = next(it1, None)
#     return result
# print(iter_merge(a, b))
#-------------------------------------------
# a = [1, 3, 5, 9, 13]
# b = [12, 4, 16, 7, 15, 22, 33]
# def gen_merge_inner(it1, it2):
#     el1 = next(it1, None)
#     el2 = next(it2, None)
#     while el1 is not None or el2 is not None:
#         if el1 is None or (el2 is not None and el2 < el1):
#             yield el2
#             el2 = next(it2, None)
#         else:
#             yield el1
#             el1 = next(it1, None)
#     # print(el1, el2)
# def gen_merge(list1, list2):
#     return list(gen_merge_inner(iter(list1), iter(list2))) # из генератора получаем список
# gen = gen_merge
#
# # print(gen_merge(a,b))
# # print(list(gen_merge_inner(iter(a), iter(b))))
# # print(gen(a,b))
# print(gen_merge(a, b))
#-------------------------------------------
# list1 = [1, 3, 5, 9, 13]
# list2 = [12, 4, 16, 7, 15, 22, 33]
# from heapq import merge
#
# def heapq_merge(list1, list2):
#     return list(merge(list1, list2)) # тоже возвращает генератор
#
#
# print(heapq_merge(list1, list2))
#-------------------------------------------
# from collections import Counter
# list1 = [1, 3, 5, 9, 13]
# list2 = [12, 4, 16, 7, 15, 22, 33]
# def gen_merge_inner(it1, it2):
#     el1 = next(it1, None)
#     el2 = next(it2, None)
#     while el1 is not None or el2 is not None:
#         if el1 is None or (el2 is not None and el2 < el1):
#             yield el2
#             el2 = next(it2, None)
#         else:
#             yield el1
#             el1 = next(it1, None)
# def counter_merge(list1, list2):
#     return list(gen_merge_inner(Counter(list1).elements(), Counter(list2).elements()))
#
# print(counter_merge(list1, list2))

#-------------------------------------------
list1 = [1, 3, 5, 9, 13]
list2 = [12, 4, 16, 7, 15, 22, 33]
def sort_merge(list1, list2):
    return sorted(list1 + list2)
print(sort_merge(list1, list2))