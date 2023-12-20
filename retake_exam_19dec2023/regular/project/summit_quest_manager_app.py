from typing import List

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.base_climber import BaseClimber
from project.climbers.summit_climber import SummitClimber

from project.peaks.arctic_peak import ArcticPeak
from project.peaks.base_peak import BasePeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    def __init__(self):
        self.climbers: List[BaseClimber] = []
        self.peaks: List[BasePeak] = []

    def register_climber(self, climber_type: str, climber_name: str):
        valid_climbers = ['ArcticClimber', 'SummitClimber']
        if climber_type not in valid_climbers:
            return f"{climber_type} doesn't exist in our register."
        climber_exist = [climber for climber in self.climbers if climber.name == climber_name]
        if climber_exist:
            return f"{climber_name} has been already registered."
        if climber_type == 'ArcticClimber':
            register_climber = ArcticClimber(climber_name)
        else:
            register_climber = SummitClimber(climber_name)
        self.climbers.append(register_climber)
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        valid_peaks = ["ArcticPeak", "SummitPeak"]
        if peak_type not in valid_peaks:
            return f"{peak_type} is an unknown type of peak."
        if peak_type == 'ArcticPeak':
            register_peak = ArcticPeak(peak_name, peak_elevation)
        else:
            register_peak = SummitPeak(peak_name, peak_elevation)
        self.peaks.append(register_peak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    # def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
    #     missing_gear = []
    #     climber_object = [climber for climber in self.climbers if climber.name == climber_name][0]
    #     peak_object = [peak for peak in self.peaks if peak.name == peak_name][0]
    #     required_gear = peak_object.get_recommended_gear()
    #     if peak_object.__class__.__name__ == 'SummitPeak':
    #         for req_gear in required_gear:
    #             if req_gear not in gear:
    #                 missing_gear.append(req_gear)
    #     elif peak_object.__class__.__name__ == 'ArcticPeak':
    #         for req_gear in required_gear:
    #             if req_gear not in gear:
    #                 missing_gear.append(req_gear)
    #     if not missing_gear:
    #         return f"{climber_name} is prepared to climb {peak_name}."
    #     if missing_gear:
    #         climber_object.is_prepared = False
    #         sorted_missing_gear = sorted(missing_gear)
    #         return (f"{climber_name} is not prepared to climb {peak_name}. "
    #                 f"Missing gear: {', '.join(sorted_missing_gear)}.")

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
        missing_gear = []
        climber_object = [climber for climber in self.climbers if climber.name == climber_name][0]
        peak_object = [peak for peak in self.peaks if peak.name == peak_name][0]
        required_gear = set(peak_object.get_recommended_gear())
        gear = set(gear)
        # missing_gear = required_gear - set(gear)
        if peak_object.__class__.__name__ == 'SummitPeak' or peak_object.__class__.__name__ == 'ArcticPeak':
            for req_gear in required_gear:
                if req_gear not in gear:
                    missing_gear.append(req_gear)
        if not missing_gear:
            return f"{climber_name} is prepared to climb {peak_name}."
        climber_object.is_prepared = False
        return (f"{climber_name} is not prepared to climb {peak_name}. "
                f"Missing gear: {', '.join(sorted(missing_gear))}.")

    # def perform_climbing(self, climber_name: str, peak_name: str):
    #     climber_exist = [climber for climber in self.climbers if climber.name == climber_name]
    #     if not climber_exist:
    #         return f"Climber {climber_name} is not registered yet."
    #     peak_exist = [peak for peak in self.peaks if peak.name == peak_name]
    #     if not peak_exist:
    #         return f"Peak {peak_name} is not part of the wish list."
    #     climber_exist = climber_exist[0]
    #     peak_exist = peak_exist[0]
    #     climber_exist.can_climb()
    #
    #     if climber_exist.is_prepared and climber_exist.enough_strength:
    #         climber_exist.climb(peak_exist)
    #         return (f"{climber_name} conquered {peak_name} "
    #                 f"whose difficulty level is {peak_exist.difficulty_level}.")
    #     elif climber_exist.is_prepared is False:
    #         return f"{climber_name} will need to be better prepared next time."
    #     else:
    #         climber_exist.rest()
    #         return (f"{climber_name} needs more strength to climb {peak_name} "
    #                 f"and is therefore taking some rest.")

    def perform_climbing(self, climber_name: str, peak_name: str):
        climber_exist = next((climber for climber in self.climbers if climber.name == climber_name), None)
        peak_exist = next((peak for peak in self.peaks if peak.name == peak_name), None)
        if climber_exist is None:
            return f"Climber {climber_name} is not registered yet."
        if peak_exist is None:
            return f"Peak {peak_name} is not part of the wish list."

        climber_exist.can_climb()

        if climber_exist.is_prepared and climber_exist.can_climb():
            climber_exist.climb(peak_exist)
            return (f"{climber_name} conquered {peak_name} "
                    f"whose difficulty level is {peak_exist.difficulty_level}.")
        elif not climber_exist.is_prepared:
            return f"{climber_name} will need to be better prepared next time."
        else:
            climber_exist.rest()
            return (f"{climber_name} needs more strength to climb {peak_name} "
                    f"and is therefore taking some rest.")

    def get_statistics(self):
        # successful_climbers = [climber for climber in self.climbers if climber.conquered_peaks]
        # total_climbed_peaks = set()
        #
        # for climber_stats in successful_climbers:
        #     total_climbed_peaks.update(climber_stats.conquered_peaks)
        #
        # total_climbed_peaks_num = len(total_climbed_peaks)
        # statistics_result = [f"Total climbed peaks: {total_climbed_peaks_num}", "**Climber's statistics:**"]
        #
        # sorted_climbers = sorted(successful_climbers, key=lambda climber: (-len(climber.conquered_peaks), climber.name))
        #
        # for climber in sorted_climbers:
        #     statistics_result.append(climber.__str__())
        #
        # return "\n".join(statistics_result)
        sorted_climbers = sorted([climber for climber in self.climbers if climber.conquered_peaks],
                                 key=lambda climber: (-len(climber.conquered_peaks), climber.name))

        result = [
            f"Total climbed peaks: {len(self.peaks)}",
            "**Climber's statistics:**"
        ]

        climber_statistics = "\n".join(str(c) for c in sorted_climbers)
        result.append(climber_statistics)

        return '\n'.join(result)
