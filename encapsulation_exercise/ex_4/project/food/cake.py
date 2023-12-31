from project.food.dessert import Dessert



class Cake(Dessert):
    GRAMS = 250
    CALORIES = 1000
    PRICE = 5

    def __init__(self, name):
        super().__init__(name, Cake.PRICE, Cake.GRAMS, Cake.CALORIES)

class Tiramisu(Dessert):
    def __init__(self, name, price, grams, calories):
        super().__init__(name, price, grams, calories)