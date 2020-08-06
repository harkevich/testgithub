class Person:
    # name = 'John'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f'Name: {self.name}, Age: {self.age}')

class Employee(Person):

    def __init__(self, name, age, company):
        super().__init__(name, age)
        self.company = company

    def more_info(self):
        print(f'{self.name}, works in: {self.company}')

    def print_info(self):
        super(Employee, self).print_info()
        print(f'Work {self.company}')

    def __str__(self):
        # return f'Name: {self.name}'
        return "Class" + self.__class__.__name__