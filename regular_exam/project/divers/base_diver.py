from abc import ABC, abstractmethod
from typing import List

from project.fish.base_fish import BaseFish


class BaseDiver(ABC):
    def __init__(self, name: str, oxygen_level: float):
        self.name = name
        self.oxygen_level = oxygen_level
        self.catch: List[BaseFish] = []
        self.competition_points: float = 0
        self.has_health_issue: bool = False

    # @property
    # def has_health_issue(self):
    #     return self._has_health_issue
    #
    # @has_health_issue.setter
    # def has_health_issue(self, value):
    #     self._has_health_issue = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Diver name cannot be null or empty!")
        self.__name = value

    @property
    def oxygen_level(self):
        return self.__oxygen_level

    @oxygen_level.setter
    def oxygen_level(self, value):
    #    if value < 0:
     #       raise ValueError("Cannot create diver with negative oxygen level!")
        self.__oxygen_level = value

    @property
    def competition_points(self):
        return self._competition_points

    @competition_points.setter
    def competition_points(self, value):
        self._competition_points = value

    @abstractmethod
    def miss(self, time_to_catch: int):
        pass

    @abstractmethod
    def renew_oxy(self):
        pass


    def hit(self, fish: BaseFish):
        time_to_catch_this_fish = fish.time_to_catch
        if self.oxygen_level - time_to_catch_this_fish < 0:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= time_to_catch_this_fish
            self.catch.append(fish)
            self._competition_points += round(fish.points, 1)

    def update_health_status(self):
        if self._has_health_issue is False:
            self._has_health_issue = True
        else:
            self._has_health_issue = False

    @abstractmethod
    def __str__(self):
        pass
        # return f'{self.__class__.__name__}: [Name: {self.name}, Oxygen level left: {self.oxygen_level}, Fish caught:
        # {len(self.catch)}, Points earned: {self._competition_points}]'

