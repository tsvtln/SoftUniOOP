from abc import ABC, abstractmethod
from typing import List

from project.peaks.base_peak import BasePeak


class BaseClimber(ABC):
    def __init__(self, name: str, strength: float):
        self.name = name
        self.strength = strength
        self.conquered_peaks: List[BasePeak] = []
        self.is_prepared: bool = True
        # self.enough_strength: bool = True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Climber name cannot be null or empty!")
        self.__name = value

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, value):
        if value <= 0:
            raise ValueError("A climber cannot have negative strength or strength equal to 0!")
        self.__strength = value

    @abstractmethod
    def can_climb(self):
        pass

    @abstractmethod
    def climb(self, peak: BasePeak):
        pass

    def rest(self):
        self.strength += 15

    def __str__(self):
        # type_of_climber = type(self).__name__
        # climber_name = self.name
        # left_strength = self.strength
        # sorted_conquered_peaks = sorted(self.conquered_peaks, key=lambda pk: pk.name)
        # conquered = ', '.join(peak.name for peak in sorted_conquered_peaks)
        #
        # return (f"{type_of_climber}: /// "
        #         f"Climber name: {climber_name} * "
        #         f"Left strength: {left_strength:.1f} * "
        #         f"Conquered peaks: {conquered} ///")

        conquered_peaks = sorted(self.conquered_peaks)
        return f"{type(self).__name__}: /// Climber name: {self.name} * Left strength: {self.strength:.1f} * Conquered " \
               f"peaks: {', '.join(conquered_peaks)} ///"

        # type_of_climber = type(self).__name__
        # climber_name = self.name
        # left_strength = self.strength
        # sorted_conquered_peaks = sorted(self.conquered_peaks, key=lambda peak: peak.name)
        # conquered = ', '.join(peak.name for peak in sorted_conquered_peaks)
        #
        # return (
        #     f"{type_of_climber}: /// "
        #     f"Climber name: {climber_name} * "
        #     f"Left strength: {left_strength:.1f} * "
        #     f"Conquered peaks: {conquered} ///"
        # )
