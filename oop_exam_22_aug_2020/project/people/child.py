class Child:
    def __init__(self, food_cost, *attrs):
        # self.food_cost = food_cost
        # self.toys_cost = sum(attrs)
        self.cost = food_cost + sum(attrs)
