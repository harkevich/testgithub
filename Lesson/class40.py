class Person:
    # name = 'John'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f'Name: {self.name}, Age: {self.age}')

class Employee(Person):

    company = 'Google'

    def more_info(self):
        print(f'{self.name}, works in: {self.company}')