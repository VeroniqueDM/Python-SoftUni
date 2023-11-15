from project.core.drink_factory import DrinkFactory
from project.core.food_factory import FoodFactory
from project.core.table_factory import TableFactory
from project.core.validator import Validator


class Bakery:
    def __init__(self, name):
        self.total_income = 0
        self.tables_repository = []
        self.drinks_menu = []
        self.food_menu = []
        self.name = name
        self.food_factory = FoodFactory()
        self.drink_factory = DrinkFactory()
        self.table_factory = TableFactory()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_string_is_empty_or_whitespace(value, "Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type, name, price):
        food = self.food_factory.create_food(food_type, name, price)
        for item in self.food_menu:
            if food.name == item.name:
                raise Exception(f"{food_type} {name} is already in the menu!")
        self.food_menu.append(food)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name, portion, brand):
        drink = self.drink_factory.create_drink(drink_type, name, portion, brand)
        for item in self.drinks_menu:
            if drink.name == item.name:
                raise Exception(f"{drink_type} {name} is already in the menu!")

        self.drinks_menu.append(drink)
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type, table_number, capacity):
        table = self.table_factory.create_table(table_type, table_number, capacity)
        for item in self.tables_repository:
            if item.table_number == table.table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")

        self.tables_repository.append(table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people):
        for table in self.tables_repository:
            if table.is_reserved:
                continue
            if table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number, *args):
        unavailable_food = []
        table = self.find_table_by_number(table_number)
        if table:
            for arg in args:
                food = self.find_food_by_name(arg)
                if food:
                    table.order_food(food)
                else:
                    unavailable_food.append(arg)
            foods = [str(food) for food in table.food_orders]
            order_food = f"Table {table_number} ordered:\n" + '\n'.join(foods)
            unordered_food = f"{self.name} does not have in the menu:\n" + '\n'.join(unavailable_food)
            res = order_food + "\n" + unordered_food
            return res
        else:
            return f"Could not find table {table_number}"

    def find_food_by_name(self, name):
        for food in self.food_menu:
            if name == food.name:
                return food

    def find_drink_by_name(self, name):
        for drink in self.drinks_menu:
            if name == drink.name:
                return drink

    def find_table_by_number(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table

    def order_drink(self, table_number, *args):
        unavailable_drinks = []
        table = self.find_table_by_number(table_number)
        if table:
            for name in args:
                drink = self.find_drink_by_name(name)
                if drink:
                    table.order_drink(drink)
                else:
                    unavailable_drinks.append(name)
            drinks = [str(drink) for drink in table.drink_orders]
            order_drinks = f"Table {table_number} ordered:\n" + '\n'.join(drinks)
            unordered_drinks = f"{self.name} does not have in the menu:\n" + '\n'.join(unavailable_drinks)
            res = order_drinks + "\n" + unordered_drinks
            return res
        else:
            return f"Could not find table {table_number}"

    def leave_table(self, table_number):
        table = self.find_table_by_number(table_number)
        bill = table.get_bill()
        self.total_income += bill
        table.clear()
        return f"Table: {table_number}\nBill: {bill:.2f}"


    def get_free_tables_info(self):
        tables = []
        for table in self.tables_repository:
            if not table.is_reserved:
                tables.append(table.free_table_info())
        return '\n'.join(tables)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
