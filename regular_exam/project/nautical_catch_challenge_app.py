from typing import List

from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver

from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type == 'ScubaDiver':
            diver_exist_check = [diver for diver in self.divers if diver_name == diver.name]
            if diver_exist_check:
                return f"{diver_name} is already a participant."
            else:
                diver = ScubaDiver(diver_name)
                self.divers.append(diver)
                return f"{diver_name} is successfully registered for the competition as a {diver_type}."

        elif diver_type == 'FreeDiver':
            diver_exist_check = [diver for diver in self.divers if diver_name == diver.name]
            if diver_exist_check:
                return f"{diver_name} is already a participant."
            else:
                diver = FreeDiver(diver_name)
                self.divers.append(diver)
                return f"{diver_name} is successfully registered for the competition as a {diver_type}."

        else:
            return f"{diver_type} is not allowed in our competition."

    #  ORIG
    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type == 'PredatoryFish':
            fish_exist_check = [fish for fish in self.fish_list if fish_name == fish.name]
            if fish_exist_check:
                return f"{fish_name} is already permitted."
            else:
                fish = PredatoryFish(fish_name, points)
                self.fish_list.append(fish)
                return f"{fish_name} is allowed for chasing as a {fish_type}."

        elif fish_type == 'DeepSeaFish':
            fish_exist_check = [fish for fish in self.fish_list if fish_name == fish.name]
            if fish_exist_check:
                return f"{fish_name} is already permitted."
            else:
                fish = DeepSeaFish(fish_name, points)
                self.fish_list.append(fish)
                return f"{fish_name} is allowed for chasing as a {fish_type}."

        else:
            return f"{fish_type} is forbidden for chasing in our competition."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        # Diver Validation:
        check_diver_existence = [diver for diver in self.divers if diver_name == diver.name]
        if not check_diver_existence:
            return f"{diver_name} is not registered for the competition."
        check_diver_existence = check_diver_existence[0]

        # Fish Validation:
        fish_exist_check = [fish for fish in self.fish_list if fish_name == fish.name]
        if not fish_exist_check:
            return f"The {fish_name} is not allowed to be caught in this competition."
        fish_exist_check = fish_exist_check[0]

        # Health Check:
        if check_diver_existence.has_health_issue or check_diver_existence.oxygen_level <= 0:
            check_diver_existence.has_health_issue = True
            return f"{diver_name} will not be allowed to dive, due to health issues."

        # Oxygen Level Comparison
        time_to_catch_fish = fish_exist_check.time_to_catch
        oxygen_level_diver = check_diver_existence.oxygen_level

        if oxygen_level_diver < time_to_catch_fish:
            check_diver_existence.miss(time_to_catch_fish)
            check_diver_existence.has_health_issue = True
            return f"{diver_name} missed a good {fish_name}."

        elif oxygen_level_diver == time_to_catch_fish:
            if is_lucky:
                check_diver_existence.hit(fish_exist_check)
                return f"{diver_name} hits a {fish_exist_check.points}pt. {fish_name}."
            else:
                check_diver_existence.miss(time_to_catch_fish)
                check_diver_existence.has_health_issue = True
                return f"{diver_name} missed a good {fish_name}."

        elif oxygen_level_diver > time_to_catch_fish:
            check_diver_existence.hit(fish_exist_check)
            return f"{diver_name} hits a {fish_exist_check.points}pt. {fish_name}."

        # Zero Oxygen Level Handling:
        if oxygen_level_diver <= 0:
            check_diver_existence._has_health_issue = True
            return f"{diver_name} will not be allowed to dive, due to health issues."

    # def health_recovery(self):
    #     divers_count = 0
    #     for diver in self.divers:
    #         health_status = diver.has_health_issue
    #         if health_status:
    #             # diver.has_health_issue = False
    #             diver.renew_oxy()
    #             divers_count += 1
    #     return f"Divers recovered: {divers_count}"

    def health_recovery(self):
        divers_count = 0
        for diver in self.divers:
            diver.renew_oxy()
            diver.has_health_issue = False
            divers_count += 1
        return f"Divers recovered: {divers_count}"

    def diver_catch_report(self, diver_name: str):
        find_diver_object = [diver for diver in self.divers if diver_name == diver.name]
        find_diver_object = find_diver_object[0]
        to_return = [f"**{diver_name} Catch Report**"]
        for catches in find_diver_object.catch:
            to_return.append(catches.fish_details())
        return '\n'.join(to_return)

    def competition_statistics(self):
        sorted_divers = sorted([diver for diver in self.divers if not diver.has_health_issue and not diver.oxygen_level == 0],
                               key=lambda x: (-x.competition_points, -len(x.catch), x.name))

        result = [f"**Nautical Catch Challenge Statistics**"]
        [result.append(diver.__str__()) for diver in sorted_divers if not diver.has_health_issue]

        return "\n".join(result)
