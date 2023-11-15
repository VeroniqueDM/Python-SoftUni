class Zoo:

    def __init__(self,  name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self,animal, price):
        if self.__animal_capacity > len(self.animals):
            if self.__budget < price:
                return "Not enough budget"
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity>len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker.name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salary = 0
        for worker in self.workers:
            total_salary += worker.salary
        if total_salary <= self.__budget:
            self.__budget -= total_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_care = 0
        for animal in self.animals:
            total_care += animal.money_for_care
        if total_care <= self.__budget:
            self.__budget -= total_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):

        lions_list = []
        tigers_list = []
        cheetahs_list = []

        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions_list.append(repr(animal))
            elif animal.__class__.__name__ == "Tiger":
                tigers_list.append(repr(animal))
            else:
                cheetahs_list.append(repr(animal))
        res = f"You have {len(self.animals)} animals\n" + \
              f"----- {len(lions_list)} Lions:\n" + "\n".join(lions_list) + \
              f'\n----- {len(tigers_list)} Tigers:\n' + "\n".join(tigers_list) + \
              f'\n----- {len(cheetahs_list)} Cheetahs:\n' + "\n".join(cheetahs_list)
        return res
    def workers_status(self):
        vets_list = []
        caretakers_list = []
        keepers_list = []
        for worker in self.workers:
            if worker.__class__.__name__ == "Caretaker":
                caretakers_list.append(repr(worker))
            elif worker.__class__.__name__ == "Vet":
                vets_list.append(repr(worker))
            else:
                keepers_list.append(repr(worker))
        res = f"You have {len(self.workers)} workers\n" + \
              f"----- {len(keepers_list)} Keepers:\n" + "\n".join(keepers_list) + \
              f'\n----- {len(caretakers_list)} Caretakers:\n' + "\n".join(caretakers_list) + \
              f'\n----- {len(vets_list)} Vets:\n' + "\n".join(vets_list)
        return res




