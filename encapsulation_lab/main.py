# class CreditCard:
#     def __init__(self, number, exp_date, cvv, name, pin):
#         self.number = number
#         self.exp_date = exp_date
#         self.cvv = cvv
#         self.name = name
#         self.__pin = pin
#
#     def get_info(self):
#         return self.__pin
#
# card = CreditCard(4564566565, "2022-02", 456, "Test Name", 4565)
# # print(card.__pin)
# print(card._CreditCard__pin)

class Person:
    def __init__(self, age=0):
        self.age = age


    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        if age < 18: self.__age = 18
        else: self.__age = age


p = Person(5)
print(5)