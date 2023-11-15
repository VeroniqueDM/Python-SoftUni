# import math
#
#
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def calculate_distance(self, point):
#         return math.sqrt((point.x - self.x)**2 + (point.y - self.y)**2)
#
#     @staticmethod
#     def calculate_static_distance(point_1, point_2):
#         return math.sqrt((point_1.x - point_2.x)**2 + (point_1.y - point_2.y)**2)
#
# p = Point(5,6)
# p2 = Point(3,4)
# p.calculate_distance(p2)
### -----------------------------------

class Person:
    min_age = 0
    max_age = 150

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def __validate_age(value):
        if value < Person.min_age or \
           value > Person.max_age:
            raise ValueError()

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value


class Employee(Person):
    min_age = 16
    max_age = 150

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def __validate_age(value):
        if value < Employee.min_age or \
           value > Employee.max_age:
            raise ValueError()

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value


###----------------------------------
