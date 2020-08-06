class Person:
    # name = 'John'
    def __init__(self, name):
        # print('hi')
        self.name = name
        self.__age = 20
    def print_info(self):
        print(f'Name: {self.name}, Age: {self.__age}')

    # def get_age(self):
    #     return self.__age
    #
    # def set_age(self, value):
    #     # self.__age = value
    #     if value in range(1, 101):
    #         self.__age
    #     else:
    #         print('Wrong age')
    @property
    def age(self):
        return self.__age