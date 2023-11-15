from project.animal import Animal


class Cat(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def __repr__(self):
        return (f"This is {self.name}. {self.name} is a {self.age} "
                f"year old {self.gender} {type(self).__name__}")

    def make_sound(self):
        return f"Meow meow!"
