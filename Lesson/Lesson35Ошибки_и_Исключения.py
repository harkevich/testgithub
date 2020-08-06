print('Hello')
# print(100 / 0)
# print(1 + '2')
# print(int('test'))

# try:
#     num = 100 / 0
# except ZeroDivisionError:
#     num = 0
# except TypeError:
#     num = 1


while True:
    try:
        num =int(input('Enter your number: '))
        print(f'100 / {num} = {100/num}')
        break
    except ZeroDivisionError:
        print('The number must be greater than zero')
    except ValueError:
        print('Must be a number')

print(type)
print(type)
print(type)