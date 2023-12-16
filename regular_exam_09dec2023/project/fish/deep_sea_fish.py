from project.fish.base_fish import BaseFish


class DeepSeaFish(BaseFish):

    def __init__(self, name: str, points: float):
        super().__init__(name, points, 180)

    def fish_details(self):
        return (f"DeepSeaFish: "
                f"{self.name} [Points: {self.points}, Time to Catch: "
                f"{self.time_to_catch} seconds]")
