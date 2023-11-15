
from project.astronaut.astronaut_repository import AstronautRepository
from project.core.astronaut_factory import AstronautFactory
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.astronaut_factory = AstronautFactory()
        self.completed_missions = 0
        self.failed_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        astronaut = self.astronaut_factory.create_astronaut(astronaut_type, name)
        if self.astronaut_repository.find_by_name(name):
            return f"{astronaut.name} is already added."
        self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {astronaut.name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."
        planet = Planet(name)
        for item in items.split(', '):
            planet.items.append(item)
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        if self.astronaut_repository.find_by_name(name) is None:
            raise Exception(f"Astronaut {name} doesn't exist!")
        astronaut = self.astronaut_repository.find_by_name(name)
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        if self.planet_repository.find_by_name(planet_name) is None:
            raise Exception("Invalid planet name!")
        planet = self.planet_repository.find_by_name(planet_name)
        astronauts_list = self.find_astronauts_for_mission()
        return self.collect_items(planet, astronauts_list)

    def collect_items(self, planet, astronauts):
        astr_in_open_space = 0
        for astronaut in astronauts:
            astr_in_open_space +=1
            while astronaut.oxygen > 0 and len(planet.items)>0:
                last_item = planet.items.pop()
                astronaut.backpack.append(last_item)
                astronaut.breathe()
            if len(planet.items) == 0:
                self.completed_missions +=1
                self.planet_repository.planets.remove(planet)
                return f"Planet: {planet.name} was explored. {astr_in_open_space} astronauts participated in collecting items."
        if len(planet.items) == 0:
            self.completed_missions += 1
            self.planet_repository.planets.remove(planet)
            return f"Planet: {planet.name} was explored. {astr_in_open_space} astronauts participated in collecting items."
        self.failed_missions +=1
        return "Mission is not completed."

    def find_astronauts_for_mission(self):
        top_astronauts = []
        sorted_astronauts = sorted(self.astronaut_repository.astronauts, key=lambda x: x.oxygen, reverse=True)
        for astronaut in sorted_astronauts:
            if astronaut.oxygen > 30:
                top_astronauts.append(astronaut)
            if len(top_astronauts) == 5:
                return top_astronauts
        if len(top_astronauts) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")
        return top_astronauts


    def report(self):
        res = f"{self.completed_missions} successful missions!\n{self.failed_missions}" \
              f" missions were not completed!\nAstronauts' info:\n"

        for astronaut in self.astronaut_repository.astronauts:
            res += astronaut.astronaut_info() + '\n'

        return res.strip()
