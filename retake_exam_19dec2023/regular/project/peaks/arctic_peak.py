from project.peaks.base_peak import BasePeak


class ArcticPeak(BasePeak):
    def __init__(self, name: str, elevation: int):
        super().__init__(name, elevation)
        # self.difficulty_level = self.calculate_difficulty_level()

    @property
    def difficulty_level(self):
        value = self.calculate_difficulty_level()
        return value

    def get_recommended_gear(self):
        rg = ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]
        return rg

    def calculate_difficulty_level(self):
        if self.elevation > 3000:
            return 'Extreme'
        elif 2000 <= self.elevation <= 3000:
            return 'Advanced'

