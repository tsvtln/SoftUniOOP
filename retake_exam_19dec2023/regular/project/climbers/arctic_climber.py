from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    def __init__(self, name: str):
        super().__init__(name, 200)

    def can_climb(self):
        if self.strength >= 100:
            return True
        else:
            return False

    def climb(self, peak: BasePeak):
        # if self.is_prepared and self.enough_strength:
        if peak.difficulty_level == 'Extreme':
            self.strength -= 20 * 2
        else:
            self.strength -= 20 * 1.5
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
