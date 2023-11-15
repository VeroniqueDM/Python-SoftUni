from abc import ABC, abstractmethod

from project_one.core.validator import Validator


class BaseAquarium(ABC):

    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_empty_string(value, "Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum(d.comfort for d in self.decorations)

    def calculate_value(self):
        price_fish = sum([fish.price for fish in self.fish])
        price_dec = sum([dec.price for dec in self.decorations])

        return price_fish + price_dec
        # return sum([dec.price for dec in self.decorations]) + sum([fish.price for fish in self.fish])

    def add_fish(self, fish):
        if len(self.fish) >= self.capacity:
            return "Not enough capacity."
        if not self.__class__.__name__ == fish.aquarium_type:
            return "Water not suitable."
        self.fish.append(fish)
        return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        if len(self.fish) > 0:
            fish = ' '.join([fish.name for fish in self.fish])
        else:
            fish = 'none'

        comfort = self.calculate_comfort()
        res = f"{self.name}:\nFish: {fish}\nDecorations: {len(self.decorations)}\nComfort: {comfort}"
        return res
