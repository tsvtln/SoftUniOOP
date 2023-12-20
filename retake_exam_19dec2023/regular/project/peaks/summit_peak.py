from project.peaks.base_peak import BasePeak


class SummitPeak(BasePeak):
    def __init__(self, name: str, elevation: int):
        super().__init__(name, elevation)
        # self._difficulty_level = self.difficulty_level

    @property
    def difficulty_level(self):
        value = self.calculate_difficulty_level()
        return value

    def get_recommended_gear(self):
        re = ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]
        return re

    def calculate_difficulty_level(self):
        if self.elevation > 2500:
            return 'Extreme'
        elif 1500 <= self.elevation <= 2500:
            return 'Advanced'


