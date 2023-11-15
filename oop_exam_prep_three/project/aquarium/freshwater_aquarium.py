
from project_one.aquarium.base_aquarium import BaseAquarium
from project_one.decoration.ornament import Ornament
from project_one.decoration.plant import Plant
from project_one.fish.freshwater_fish import FreshwaterFish


class FreshwaterAquarium(BaseAquarium):

    def __init__(self, name):
        super().__init__(name, 50)


# aquarium =  FreshwaterAquarium('Aquarium 1')
# fish = FreshwaterFish('Name', 'species', 5 )
# fish2 = FreshwaterFish('Aa', 'species', 5 )
# fish3 = FreshwaterFish('bb', 'species', 5 )
# decoration = Plant()
# decoration2 = Ornament()
# aquarium.add_fish(fish)
# aquarium.add_fish(fish2)
# aquarium.add_fish(fish3)
# aquarium.add_decoration(decoration)
# aquarium.add_decoration(decoration2)
# print(aquarium.calculate_value())