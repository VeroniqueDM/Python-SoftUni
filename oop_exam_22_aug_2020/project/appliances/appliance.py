from abc import ABC, abstractmethod


class Appliance(ABC):
    @abstractmethod
    def __init__(self, cost):
        self.cost = cost

    def get_monthly_expense(self):
        return 30 * self.cost
