from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):

    def __init__(self, name: str):
        super().__init__(name, 120.0)

    def miss(self, time_to_catch: int):
        self.oxygen_level -= 0.60 * time_to_catch
        if self.oxygen_level < 0:
            self.oxygen_level = 0
        else:
            self.oxygen_level = round(self.oxygen_level)

    def renew_oxy(self):
        self.oxygen_level = 120.0

    def __str__(self):
        return f'FreeDiver: [Name: {self.name}, Oxygen level left: {self.oxygen_level}, Fish caught: {len(self.catch)}, Points earned: {self._competition_points}]'
