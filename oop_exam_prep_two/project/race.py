
from project.core.validators import Validator


class Race:
    def __init__(self, name):
        self.name = name
        self.drivers = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_string_shorter_than_value(value, 1, "Name cannot be an empty string!")
        self.__name = value


    def register_driver(self, driver):
        if driver.car is None:
            raise Exception(f"Driver {driver.name} could not participate in the race!")
        if any([dr.name == driver.name for dr in self.drivers]):
            return f"Driver {driver.name} is already added in {self.name} race."

        self.drivers.append(driver)
        return f"Driver {driver.name} added in {self.name} race."

    def start(self):
        if len(self.drivers) < 3:
            raise Exception(f"Race {self.name} cannot start with less than 3 participants!")
        top_three = sorted(self.drivers, key=lambda dr: dr.car.speed_limit, reverse=True)[:3]
        res = ''
        for driv in top_three:
            driv.number_of_wins += 1
            res += f"Driver {driv.name} wins the {self.name} race with a speed of {driv.car.speed_limit}.\n"
        return res.strip()
