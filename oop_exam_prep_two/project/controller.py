
from project.core.car_factory import CarFactory
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []
        self.car_factory = CarFactory()

    def create_car(self, car_type, model, speed_limit):
        does_exist = any([auto.model == model for auto in self.cars])
        if does_exist:
            raise Exception(f"Car {model} is already created!")
        try:
            car = self.car_factory.create_car(car_type, model, speed_limit)
            self.cars.append(car)
            return f"{car_type} {model} is created."
        except RuntimeError:
            pass

    def create_driver(self, driver_name):
        does_exist = any([driv.name == driver_name for driv in self.drivers])
        if does_exist:
            raise Exception(f"Driver {driver_name} is already created!")
        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name):
        does_exist = any([r.name == race_name for r in self.races])
        if does_exist:
            raise Exception(f"Race {race_name} is already created!")
        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def __find_car_by_type(self,car_type):
        for ind in range(len(self.cars)-1, -1, -1):
            car = self.cars[ind]
            if not car.is_taken and car.__class__.__name__ == car_type:
                return car
        return None

    def __find_driver_by_name(self,driver_name):
        for driv in self.drivers:
            if driv.name == driver_name:
                return driv
        raise Exception(f"Driver {driver_name} could not be found!")

    def __find_race_by_name(self, name):
        for rac in self.races:
            if rac.name == name:
                return rac
        raise Exception(f"Race {name} could not be found!")

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__find_driver_by_name(driver_name)
        car = self.__find_car_by_type(car_type)
        if car is None:
            raise Exception(f"Car {car_type} could not be found!")
        return driver.change_car(car)
        # car.is_taken = True
        # if driver.car:
        #     driver.car.is_taken = False
        #     old_car, driver.car = driver.car, car
        #     return f"Driver {driver_name} changed his car from {old_car.model} to {car.model}."
        # else:
        #     driver.car = car
        #     return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self,race_name: str, driver_name: str):
        race = self.__find_race_by_name(race_name)
        current_driver = self.__find_driver_by_name(driver_name)
        # current_driver = [d for d in self.drivers if d.name == driver_name][0]
        return race.register_driver(current_driver)

    def start_race(self, race_name: str):
        race = self.__find_race_by_name(race_name)
        return race.start()

