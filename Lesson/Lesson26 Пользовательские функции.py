#-------- пример с 19 урока
# s = 'Hello word'
# if '' in s:
#     s = s.upper()
# else:
#     s = s.lower()
# print(s)

# def (определять) вызов функции
def hello():
    print('Hello')
hello()
hello()
hello()
hello()

def hello2(name, word): # параметор может быть любой (тут параметор называетname)

    print('Hello, ' + name + '. Say ' + word)

hello2('John','hi')
hello2('Katy', 'hello')


def get_sum(a, b):
    print(a + b)
x = 2
y = 5
get_sum(1, 3)
get_sum(x, y)

def get_sum2(a, b):
    return a + b

print(get_sum2(1, 2))

def hi():
    print('Hi')

hi()
print(hi())