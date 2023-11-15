from project_one.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    def __init__(self, name, species,  price):
        super().__init__(name, species, 5,  price)

    def eat(self):
        self.size += 2

    @property
    def aquarium_type(self):
        return 'SaltwaterAquarium'
