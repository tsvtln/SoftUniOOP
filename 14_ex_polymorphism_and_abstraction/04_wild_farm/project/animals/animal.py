from abc import ABC, abstractmethod
from typing import List

from project.food import Food


class Animal(ABC):
    ALLOWED_FOOD: List[str] = []
    GAINED_WEIGHT: float = 0

    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food: Food):
        if type(food).__name__ not in self.ALLOWED_FOOD:
            return f"{type(self).__name__} does not eat {type(food).__name__}!"
        self.weight += food.quantity * self.GAINED_WEIGHT
        self.food_eaten += food.quantity


class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f'{type(self).__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]'
