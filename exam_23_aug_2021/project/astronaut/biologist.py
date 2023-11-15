from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    OXYGEN_DECREASE = 5

    def __init__(sel, name: str):
        super().__init__(name, 70)