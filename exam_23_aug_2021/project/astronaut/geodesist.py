from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):

    def __init__(sel, name: str):
        super().__init__(name, 50)