from project.core.validator import Validator


class Player:
    STAMINA_MAX_VALUE = 100
    STAMINA_MIN_VALUE = 0

    def __init__(self, name: str, age: int, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina


    @property
    def need_sustenance(self):
        if self.stamina == self.STAMINA_MAX_VALUE:
            return False
        return True

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        Validator.raise_if_value_not_in_range(value,self.STAMINA_MIN_VALUE, self.STAMINA_MAX_VALUE, "Stamina not valid!")
        self.__stamina = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_string_is_empty(value, "Name not valid!")
        Validator.check_if_name_is_unique(value, f"Name {value} is already used!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validator.raise_if_value_less_than_minimum(value, 12, "The player cannot be under 12 years old!")
        self.__age = value

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"
