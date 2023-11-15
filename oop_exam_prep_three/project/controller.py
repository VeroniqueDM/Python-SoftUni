from project_one.core.aquarium_factory import AquariumFactory
from project_one.core.decoration_factory import DecorationFactory
from project_one.core.fish_factory import FishFactory
from project_one.decoration.decoration_repository import DecorationRepository


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []
        self.aquarium_factory = AquariumFactory()
        self.decoration_factory = DecorationFactory()
        self.fish_factory = FishFactory()

    def __find_aquarium_by_name(self, name):
        for aquarium in self.aquariums:
            if aquarium.name == name:
                return aquarium

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        aquarium = self.aquarium_factory.create_aquarium(aquarium_type, aquarium_name)
        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        decoration = self.decoration_factory.create_decoration(decoration_type)
        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if decoration is None:
            return f"There isn't a decoration of type {decoration_type}."
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        aquarium.add_decoration(decoration)
        self.decorations_repository.remove(decoration)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        fish = self.fish_factory.create_fish(fish_type, fish_name, fish_species, price)
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        if aquarium:
            return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str):
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        if aquarium:
            aquarium.feed()
            return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        if aquarium:
            # value = sum([dec.price for dec in aquarium.decorations]) + sum([fish.price for fish in aquarium.fish])
            value = aquarium.calculate_value()
            return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        res = ''
        for aquarium in self.aquariums:
            res += str(aquarium) + '\n'
        return res.strip()
