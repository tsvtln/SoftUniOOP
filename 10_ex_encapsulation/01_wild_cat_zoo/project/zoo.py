from project.worker import Worker


class Zoo:
    animals = []
    workers = []

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

    def add_animal(self, animal, price):
        if price <= self.__budget and len(self.animals) < self.__animal_capacity:
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {type(animal).__name__} added to the zoo"
        elif price > self.__budget:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        worker = [worker for worker in self.workers if worker_name == worker.name]
        if not worker:
            return f"There is no {worker_name} in the zoo"
        worker = worker[0]
        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        salary_total = 0
        for worker in self.workers:
            salary_total += worker.salary
        if salary_total <= self.__budget:
            self.__budget -= salary_total
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        animals_care_total = 0
        for animal in self.animals:
            animals_care_total += animal.money_for_care
        if animals_care_total <= self.__budget:
            self.__budget -= animals_care_total
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        to_print = [f"You have {len(self.animals)} animals"]
        lions = []
        cheetahs = []
        tigers = []
        for animal_type in self.animals:
            if 'Lion' == type(animal_type).__name__:
                lions.append(animal_type)
            elif 'Cheetah' == type(animal_type).__name__:
                cheetahs.append(animal_type)
            else:
                tigers.append(animal_type)
        to_print.append(f"----- {len(lions)} Lions:")
        for lion_stats in lions:
            to_print.append(lion_stats.__repr__())
        to_print.append(f"----- {len(tigers)} Tigers:")
        for tiger_stats in tigers:
            to_print.append(tiger_stats.__repr__())
        to_print.append(f"----- {len(cheetahs)} Cheetahs:")
        for cheetah_stats in cheetahs:
            to_print.append(cheetah_stats.__repr__())

        return '\n'.join(to_print)

    def workers_status(self):
        to_print = [f"You have {len(self.workers)} workers"]
        keepers = []
        caretakers = []
        vets = []
        for worker_type in self.workers:
            if 'Keeper' == type(worker_type).__name__:
                keepers.append(worker_type)
            elif 'Caretaker' == type(worker_type).__name__:
                caretakers.append(worker_type)
            else:
                vets.append(worker_type)
        to_print.append(f"----- {len(keepers)} Keepers:")
        for keeper_stats in keepers:
            to_print.append(keeper_stats.__repr__())
        to_print.append(f"----- {len(caretakers)} Caretakers:")
        for caretakers_stats in caretakers:
            to_print.append(caretakers_stats.__repr__())
        to_print.append(f"----- {len(vets)} Vets:")
        for vets_stats in vets:
            to_print.append(vets_stats.__repr__())
        return '\n'.join(to_print)