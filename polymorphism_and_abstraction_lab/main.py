from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

# class Triangle(Shape):
#     def __init__(self, h, side):
#         self.h = h
#         self.side = side
#
#     def calculate_area(self):
#         return 'Calculating Triangle Area'
#

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def calculate_area(self):
        return pi * (self.r**2)

    def calculate_perimeter(self):
        return 2*pi*self.r

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return 2* (self.height + self.width)

# class Square(Shape):
#     def __init__(self, a , b):
#         self.a = a
#         self.b = b
#
#     def calculate_area(self):
#         return 'Calculating Square Area'

#
# shapes = [Triangle(5,2), Circle(5), Triangle(2,6), Triangle(8,9)]
#
# for shape in shapes:
#     print(shape.calculate_area())

circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())
rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
