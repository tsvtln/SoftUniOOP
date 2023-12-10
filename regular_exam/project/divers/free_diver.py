from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):

    def __init__(self, name: str):
        super().__init__(name, 120.0)

    # def miss(self, time_to_catch: int):
    #     # self.oxygen_level -= time_to_catch * 0.60
    #     reduction_amount = round(time_to_catch * 0.60)
    #     self.oxygen_level = max(0, self.oxygen_level - reduction_amount)
    #     if self.oxygen_level == 0:
    #         self.has_health_issue = True
    def miss(self, time_to_catch: int):
        time_to_catch = round(time_to_catch * 0.6)
        if self.oxygen_level < time_to_catch:
            self.oxygen_level = 0
            return
        self.oxygen_level -= time_to_catch

    def renew_oxy(self):
        self.oxygen_level = 120.0

    def __str__(self):
        return f'FreeDiver: [Name: {self.name}, Oxygen level left: {int(self.oxygen_level)}, Fish caught: {len(self.catch)}, Points earned: {self._competition_points}]'
