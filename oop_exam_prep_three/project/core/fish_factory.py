from project_one.fish.freshwater_fish import FreshwaterFish
from project_one.fish.saltwater_fish import SaltwaterFish


class FishFactory:
    fish_types = {
        'FreshwaterFish': FreshwaterFish,
        'SaltwaterFish': SaltwaterFish,
    }

    def create_fish(self, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type in FishFactory.fish_types:
            return self.fish_types[fish_type](fish_name, fish_species, price)
        return f"There isn't a fish of type {fish_type}."

