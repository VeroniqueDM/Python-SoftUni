class Zoo:
    # __animals = 0
    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []



    def add_animal(self, species, animal_name):
      #  Zoo.__animals += 1
        if species == "mammal":
            self.mammals.append(animal_name)
        elif species == "fish":
            self.fishes.append(animal_name)
        elif species == "bird":
            self.birds.append(animal_name)
        total_animals = len(self.mammals) + len(self.fishes) + len(self.birds)

    def get_info(self,species):
        if species == "mammal":
            return f"""Mammals in {self.name}: {", ".join(self.mammals)}
Total animals: {total_animals}"""
        elif species == "fish":
            return f"""Fishes in {self.name}: {", ".join(self.fishes)}
Total animals: {total_animals}"""
        elif species == "bird":
            return f"""Birds in {self.name}: {", ".join(self.birds)}
Total animals: {total_animals}"""






name_zoo = input()
zoo = Zoo(name_zoo)
total_animals = int(input())

for i in range(total_animals):
    command = input().split()
    species_curr_animal = command[0]
    name_curr_animal = command[1]
    zoo.add_animal(species_curr_animal, name_curr_animal)
species_info = input()
species_info_requested = zoo.get_info(species_info)
print(species_info_requested)
