name = 'John'

age = 30
print("My name is " + name + '. ' 'I\'m ' + str(age))
print('My name is %(name)s. I\'m %(age)d' %{'name' : name, 'age' : age})
print('My name is %s. I\'m %d' %(name, age))

# -----------print("Title: %s,")

# ----------Format---------

print('My {1} name is {0}. I\'m {1}'.format(name, age))

print(f'My name is {name}. I\'m {age}')

print(f'My {5 + 2} name is {name}. I\'m {age + 5 - 6}')

print(f'y = {3000 * 456}')