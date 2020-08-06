# ---------------- Создание словарей ----------------
# d = {}
# d1 = dict()
#
# print(type(d))
# print(type(d1))
# print(d)
# print(d1)
# # product1 = {          # Можно создать и так. Просто для удобства чтения всего словаря
# #     'title' : 'Sony',
# #     'price': 100
# # }
# product1 = {'title' : 'Sony', 'price': 100}
# product2 = dict(title= "iPhone", price=220)
# print(product1)
# print(product2)
# ----------------Преобразавание из списка в словарь----------------
# users = [
#     ['bob@gmail.com', 'Bob'],
#     ['kary@gmail.com', 'Katy'],
#     ['John@gmail.com', 'John'],
# ]
# d_users = dict(users)
# print(users)
# print(d_users)
#
#
# ---------------- Преобразавание из кортежа в словарь----------------
# users_t = (
#     ('bob@gmail.com', 'Bob'),
#     ('kary@gmail.com', 'Katy'),
#     ('John@gmail.com', 'John'),
# )
# d_users_t = dict(users_t)
# print(users_t)
# print(d_users_t)
#
# product3 = dict.fromkeys(['price1', 'price2','price3'],50)
# print(product3)
#
# ---------------- гениратор словарей----------------
# nums = {i: i + 1 for i in range(1, 10)}
# print(nums)
#
# product3 = {'title' : 'Sony', 'price': 100}
# product4 = dict(title= "iPhone", price=220)
#
# print(product3['title'])
#
# print(nums[1]) # есть словарь состоит из цифр(int) то при вывоже не нужно указавать ''
#
#
#
# # ----------------выводит то что в скобках----------------
# # 1 случай если нет такого в словаре то при выводе print(product3['title'])  выдаст ошибку
# # 2 случай если нет такого в словаре то при выводе print(product3.get('title'))  выведет NONE можно указать что выводить print(product3.get('title'),"ТАКОГО КЛЮЧА НЕТ")
# print(product3['title'])
# print(product3.get('title2', "ТАКОГО КЛЮЧА НЕТ"))

#---------------- Передрать словарь ----------------
# product1 = {'title' : 'Sony', 'price': 100}
# product2 = dict(title= "iPhone", price=220)
# for key in product1:
#     print(product1[key])
#     print(f'{key}: {product1[key]}')
#
# # print(product1.items())
# for key, value in product1.items():\
#     print(key , value)


#---------------- Список словарь ----------------
products = [
    {'title' : 'Sony', 'price': 100},
    {'title' : 'iPhone', 'price': 200},
    {'title' : 'Samsung', 'price': 50}
]
print(products)
for pro in products:
    print(pro['title'], pro['price'])