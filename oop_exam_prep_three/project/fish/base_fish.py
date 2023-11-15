from abc import ABC, abstractmethod
from project_one.core.validator import Validator


class BaseFish(ABC):
    def __init__(self, name, species, size, price: float):
        self.price = price
        self.size = size
        self.species = species
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_empty_string(value, "Fish name cannot be an empty string.")
        self.__name = value

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        Validator.raise_if_empty_string(value, "Fish species cannot be an empty string.")
        self.__species = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        Validator.raise_if_value_less_or_equal_than_zero(value, "Price cannot be equal to or below zero.")
        self.__price = value

    @abstractmethod
    def eat(self):
        self.size += 5

    @property
    @abstractmethod
    def aquarium_type(self):
        pass
