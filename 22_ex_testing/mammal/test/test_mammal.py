from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Gery", "Gadze", "boli me glavata")

    def testInit(self):
        """tests correct initialization"""
        self.assertEqual("Gery", self.mammal.name)
        self.assertEqual("Gadze", self.mammal.type)
        self.assertEqual("boli me glavata", self.mammal.sound)

    def testSound(self):
        """test for making a sound"""
        self.assertEqual(f"{self.mammal.name} makes {self.mammal.sound}", self.mammal.make_sound())

    def testKingdom(self):
        self.assertEqual('animals', self.mammal.get_kingdom())

    def testInfo(self):
        """test get info"""
        self.assertEqual(f"{self.mammal.name} is of type {self.mammal.type}", self.mammal.info())


if __name__ == '__main__':
    main()
