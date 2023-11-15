from project_one.aquarium.freshwater_aquarium import FreshwaterAquarium
from project_one.aquarium.saltwater_aquarium import SaltwaterAquarium


class AquariumFactory:
    aquarium_types={
        'SaltwaterAquarium': SaltwaterAquarium,
        'FreshwaterAquarium': FreshwaterAquarium,
    }

    def create_aquarium(self, aquarium_type, name):
        if aquarium_type in AquariumFactory.aquarium_types:
            return self.aquarium_types[aquarium_type](name)
        return "Invalid aquarium type."


