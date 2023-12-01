import unittest
from project.hero import Hero


class TestHero(unittest.TestCase):
    def setUp(self):
        self.test_hero = Hero(
            'Gery',
            60,
            100.00,
            5.00
        )
        self.enemy_hero = Hero(
            'Johny',
            60,
            100.00,
            5.00
        )

    def test_init(self):
        self.assertEqual('Gery', self.test_hero.username)
        self.assertEqual(60, self.test_hero.level)
        self.assertEqual(100.00, self.test_hero.health)
        self.assertEqual(5.00, self.test_hero.damage)
        self.assertEqual('Johny', self.enemy_hero.username)
        self.assertEqual(60, self.enemy_hero.level)
        self.assertEqual(100.00, self.enemy_hero.health)
        self.assertEqual(5.00, self.enemy_hero.damage)
        self.assertIsInstance(self.test_hero.username, str)
        self.assertIsInstance(self.test_hero.level, int)
        self.assertIsInstance(self.test_hero.health, float)
        self.assertIsInstance(self.test_hero.damage, float)
        self.assertIsInstance(self.enemy_hero.username, str)
        self.assertIsInstance(self.enemy_hero.level, int)
        self.assertIsInstance(self.enemy_hero.health, float)
        self.assertIsInstance(self.enemy_hero.damage, float)

    def test_fight_self(self):
        with self.assertRaises(Exception) as ex:
            self.test_hero.battle(self.test_hero)
        self.assertEqual('You cannot fight yourself', str(ex.exception))

    def test_fight_zero_hp_hero(self):
        self.test_hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.test_hero.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_fight_zero_hp_enemy(self):
        self.enemy_hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.test_hero.battle(self.enemy_hero)
        self.assertEqual(f"You cannot fight {self.enemy_hero.username}. He needs to rest", str(ve.exception))

    def test_damage(self):
        self.test_hero.health = 305
        self.enemy_hero.health = 305
        expected_health_hero = 5
        expected_health_enemy = 10

        self.test_hero.battle(self.enemy_hero)
        self.assertEqual(expected_health_hero, self.test_hero.health)
        self.assertEqual(expected_health_enemy, self.enemy_hero.health)

    def test_draw(self):
        self.test_hero.health = 295
        self.enemy_hero.health = 295
        fight = self.test_hero.battle(self.enemy_hero)
        self.assertEqual('Draw', fight)

    def test_hero_win(self):
        self.test_hero.health = 305
        self.enemy_hero.health = 295
        expected_level = self.test_hero.level + 1
        expected_health = (self.test_hero.health + 5) - 300
        expected_damage = self.test_hero.damage + 5
        fight = self.test_hero.battle(self.enemy_hero)
        self.assertEqual('You win', fight)
        self.assertEqual(expected_level, self.test_hero.level)
        self.assertEqual(expected_health, self.test_hero.health)
        self.assertEqual(expected_damage, self.test_hero.damage)

    def test_enemy_win(self):
        self.test_hero.health = 295
        self.enemy_hero.health = 305
        expected_level = self.enemy_hero.level + 1
        expected_health = (self.enemy_hero.health + 5) - 300
        expected_damage = self.enemy_hero.damage + 5
        fight = self.test_hero.battle(self.enemy_hero)
        self.assertEqual('You lose', fight)
        self.assertEqual(expected_level, self.enemy_hero.level)
        self.assertEqual(expected_health, self.enemy_hero.health)
        self.assertEqual(expected_damage, self.enemy_hero.damage)

    def test_str(self):
        obj = self.test_hero
        expected_string = f"Hero {self.test_hero.username}: {self.test_hero.level} lvl\n" \
                          f"Health: {self.test_hero.health}\n" \
                          f"Damage: {self.test_hero.damage}\n"
        self.assertEqual(str(obj), expected_string)


if __name__ == '__main__':
    unittest.main()
