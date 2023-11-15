from project.animals.animal import Bird


class Owl(Bird):
    ALLOWED_FOOD = ['Meat']
    GAINED_WEIGHT = 0.25

    def make_sound(self):
        return 'Hoot Hoot'


class Hen(Bird):
    ALLOWED_FOOD = ['Meat', 'Vegetable', 'Fruit', 'Seed']
    GAINED_WEIGHT = 0.35

    def make_sound(self):
        return 'Cluck'
