# import os
# # import random as r
# # import random
# from random import randint, shuffle     # доступны только два метода randint и shuffle
# from random import *    # доступ все модули из random
#
#
# print(os.getcwd())
# # print(random.randint(1 , 100))
# print(randint(1, 100))
# l = [1, 2, 3, 4, 5]
# shuffle(l)
# print(l)
#

#
# import libs
#
# print(libs.get_count('hello', 'd'))
# print(libs.get_len('hello'))

import libs as l
print(l.get_count('hello', 'd'))
print(l.get_len('hello'))
