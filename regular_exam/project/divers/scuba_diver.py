from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):

    def __init__(self, name: str):
        super().__init__(name, 540)

    # ORIG
    # def miss(self, time_to_catch: int):
    #     self.oxygen_level -= 0.30 * time_to_catch
    #     if self.oxygen_level < 0:
    #         self.oxygen_level = 0
    #     else:
    #         self.oxygen_level = round(self.oxygen_level)

    def miss(self, time_to_catch: int):
        self.oxygen_level -= 0.30 * time_to_catch
        if self.oxygen_level < 0:
            self.oxygen_level = 0
        else:
            self.oxygen_level = round(self.oxygen_level)

    def renew_oxy(self):
        self.oxygen_level = 540

    def __str__(self):
        return f'ScubaDiver: [Name: {self.name}, Oxygen level left: {self.oxygen_level}, Fish caught: {len(self.catch)}, Points earned: {self._competition_points}]'