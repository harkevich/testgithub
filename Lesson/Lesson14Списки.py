l = [1, 2, 3, 'hello', ['test', 10], 'world', True, 5.2]
#
# l2 = list('hello')
# l3 = list((1, 2, 3))
#
#l4 = [i for i in 'hello']
# l5 = [i for i in 'hello world']
l6 = [i for i in 'hello world' if i != ' ']
# l7 = [i for i in 'hello world' if i != ' ' and i != 'e']
# l8 = [i for i in 'hello world!?' if not [' ', 'a', 'e', 'o', 'u', '!']]
#
#
print(l6)
#
#
# print(l, l2, l3, l4, l5, l6, l7, l8, sep=("\n"))


# print(list(range(11)), sep='\n')

# l9 = list(range(5, 11))
# print(l9)

# for i in range (1, 3):
#     print(f'Внешний цикл #{i}')
#     for j in range(1, 3):
#         print(f'\tВнутоенний цикл #{j}')