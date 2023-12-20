from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    def __init__(self, name: str):
        super().__init__(name, 150)

    def can_climb(self):
        if self.strength >= 75:
            return True
        else:
            return False

    def climb(self, peak: BasePeak):
        # self.can_climb()
        # if self.is_prepared and self.enough_strength:
        #     if peak.difficulty_level == 'Advanced':
        #         self.strength -= 30 * 1.3
        #     else:
        #         self.strength -= 30 * 2.5
        #     self.conquered_peaks.append(peak)
        # if self.is_prepared and self.enough_strength:
        if peak.difficulty_level == 'Advanced':
            self.strength -= 30 * 1.3
        else:
            self.strength -= 30 * 2.5
        self.conquered_peaks.append(peak.name)

    # def __str__(self):
    #     type_of_climber = self.__class__.__name__
    #     climber_name = self.name
    #     left_strength = self.strength
    #     sorted_conquered_peaks = sorted(self.conquered_peaks, key=lambda pk: pk.name)
    #     conquered = ', '.join(peak.name for peak in sorted_conquered_peaks)
    #
    #     return (f"{type_of_climber}: /// "
    #             f"Climber name: {climber_name} * "
    #             f"Left strength: {left_strength:.1f} * "
    #             f"Conquered peaks: {conquered} ///")

    # def rest(self):
    #     self.strength += 15
