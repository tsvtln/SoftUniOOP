from project.dough import Dough
from typing import Type

from project.topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Type[Dough], max_number_of_toppings: int, toppings: dict):
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings = toppings
    
    @property
    def name(self):
        return self.__dough
    
    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("The name cannot be an empty string")
        self.__dough = value
        
    @property
    def dough(self):
        return self.__dough
    
    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")

    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value):
        if value <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")
        self.__max_number_of_toppings = value

    def add_topping(self, topping: Type[Topping]):
        if len(self.toppings) + 1 == self.__max_number_of_toppings:
            raise ValueError("Not enough space for another topping")
        topping_details = {top for top in self.toppings if topping == self.toppings}
        topping_name = next(iter(topping_details.keys()))

    def calculate_total_weight(self):
        pass