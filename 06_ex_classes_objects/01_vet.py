class Vet:
    animals = list()  # for all vets
    space = 5  # total capacity

    def __init__(self, name: str):
        self.name = name
        self.animals = list()

    def register_animal(self, animal_name):
        if self.space != 0:
            self.animals.append(animal_name)
            Vet.animals.append(animal_name)
            Vet.space -= 1
            return f"{animal_name} registered in the clinic"
        return "Not enough space"

    def unregister_animal(self, animal_name):
        if animal_name in self.animals:
            self.animals.remove(animal_name)
            Vet.animals.remove(animal_name)
            Vet.space += 1
            return f"{animal_name} unregistered successfully"
        return f"{animal_name} not in the clinic"

    def info(self):
        return f"{self.name} has {len(self.animals)} animals. {Vet.space} space left in clinic"


'''tests'''
#
# peter = Vet("Peter")
# george = Vet("George")
# print(peter.register_animal("Tom"))
# print(george.register_animal("Cory"))
# print(peter.register_animal("Fishy"))
# print(peter.register_animal("Bobby"))
# print(george.register_animal("Kay"))
# print(george.unregister_animal("Cory"))
# print(peter.register_animal("Silky"))
# print(peter.unregister_animal("Molly"))
# print(peter.unregister_animal("Tom"))
# print(peter.info())
# print(george.info())

# import unittest
#
#
#     def test_register_successfull(self):
#         vet = Vet("Bob")
#         Vet.animals = []
#         Vet.space = 5
#         vet2 = Vet("Peter")
#         res = vet.register_animal("Doggy")
#         self.assertEqual(res, "Doggy registered in the clinic")
#         self.assertEqual(vet.animals, ["Doggy"])
#         self.assertEqual(vet.animals, ["Doggy"])
#         self.assertEqual(vet2.animals, [])
#
# if __name__ == "__main__":
#     unittest.main()