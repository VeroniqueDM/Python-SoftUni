from abc import ABC, abstractmethod

from project.core.Validator import Validator


class Astronaut(ABC):
    OXYGEN_DECREASE = 10

    @abstractmethod
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_string_is_empty_or_whitespace(value, "Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def breathe(self):
        self.oxygen -= self.OXYGEN_DECREASE

    def increase_oxygen(self, amount):
        self.oxygen += amount

    def astronaut_info(self):
        backpack_items = ', '.join(self.backpack) if len(self.backpack)>0 else 'none'
        res = f'Name: {self.name}\nOxygen: {self.oxygen}\nBackpack items: {backpack_items}'
        return res

