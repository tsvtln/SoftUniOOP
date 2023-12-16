from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):

    def __init__(self, name: str):
        super().__init__(name, 540)

    def miss(self, time_to_catch: int):
        # self.oxygen_level -= 0.30 * time_to_catch
        # if self.oxygen_level < 0:
        #     self.oxygen_level = 0
        #     self.has_health_issue = True
        # else:
        #     self.oxygen_level = round(self.oxygen_level)
        # reduction_amount = round(time_to_catch * 0.30)
        # self.oxygen_level = max(0, self.oxygen_level - reduction_amount)
        # if self.oxygen_level == 0:
        #     self.has_health_issue = True
        time_to_catch = round(time_to_catch * 0.3)
        if self.oxygen_level < time_to_catch:
            self.oxygen_level = 0
            return
        self.oxygen_level -= time_to_catch

    def renew_oxy(self):
        self.oxygen_level = 540

    def __str__(self):
        return f'ScubaDiver: [Name: {self.name}, Oxygen level left: {int(self.oxygen_level)}, Fish caught: {len(self.catch)}, Points earned: {self._competition_points}]'