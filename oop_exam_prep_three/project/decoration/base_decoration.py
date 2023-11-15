from abc import ABC, abstractmethod


class BaseDecoration(ABC):
    @abstractmethod
    def __init__(self, comfort, price: float):
        self.price = price
        self.comfort = comfort
    #
    # def __str__(self):
    #     return f'This is {self.__class__.__name__}'
