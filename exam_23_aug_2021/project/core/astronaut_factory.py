from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist


class AstronautFactory:
    astronaut_types = {
        'Biologist': Biologist,
        'Geodesist': Geodesist,
        'Meteorologist': Meteorologist,
    }

    def create_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type in AstronautFactory.astronaut_types:
            return self.__class__.astronaut_types[astronaut_type](name)
        raise Exception("Astronaut type is not valid!")
