class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = 'Unaffiliated'

    def add_skill(self, skill_name, mana_cost):
        if skill_name not in self.skills.keys():
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        else:
            return "Skill already added"

    def player_info(self):
        to_return = [f"Name: {self.name}", f"Guild: {self.guild}", f"HP: {self.hp}", f"MP: {self.mp}"]
        for key, value in self.skills.items():
            to_return.append(f"==={key} - {value}")
        return '\n'.join(to_return)
