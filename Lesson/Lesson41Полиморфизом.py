from class41 import Person, Employee

person = Person('Katy', 30)
# person.age = 35
person.print_info()


employee = Employee('Nick', 30, 'Google')
employee.print_info()
employee.more_info()
print(employee)