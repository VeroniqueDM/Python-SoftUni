class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_info(self):
        return f"{self.first_name} {self.last_name} {self.age} years old."

person_one = Person("Ivan", "Ivanov", 25)
person_two = Person("Anna", "Kirova", 20)

print(person_one.first_name)
print(person_two.first_name)