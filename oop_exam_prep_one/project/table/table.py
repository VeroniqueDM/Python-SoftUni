from abc import ABC, abstractmethod

from project.baked_food.baked_food import BakedFood
from project.core.validator import Validator
from project.drink.drink import Drink


class Table(ABC):

    def __init__(self, table_number, capacity):
        self.is_reserved = False
        self.number_of_people = 0
        self.drink_orders = []
        self.food_orders = []
        self.capacity = capacity
        self.table_number = table_number

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        Validator.raise_if_number_not_in_range(
            value, self.min_table_number,
            self.max_table_number, self.error_message)
        self.__table_number = value

    @property
    @abstractmethod
    def min_table_number(self):
        pass

    @property
    @abstractmethod
    def max_table_number(self):
        pass

    @property
    @abstractmethod
    def error_message(self):
        pass

    @property
    def capacity(self):
        return self.__capacity
    
    @capacity.setter
    def capacity(self, value):
        Validator.raise_if_value_zero_or_negative(value, "Capacity has to be greater than 0!")
        self.__capacity = value

    def reserve(self, number_of_people):
        self.is_reserved = True
        self.number_of_people = number_of_people

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        bill = 0
        for food in self.food_orders:
            bill += food.price
        for drink in self.drink_orders:
            bill += drink.price
        return bill

    def clear(self):
        self.food_orders = []
        self.drink_orders = []
        self.is_reserved = False
        self.number_of_people = 0

    def free_table_info(self):
        if not self.is_reserved:
            res = f"Table: {self.table_number}\nType: {self.__class__.__name__}\nCapacity: {self.capacity}"
            return res
