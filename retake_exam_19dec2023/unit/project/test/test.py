import unittest

from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(unittest.TestCase):

    def setUp(self):
        self.robot = ClimbingRobot('Mountain', 'Legs', 100, 512)

    def test_valid_category(self):
        self.assertEqual(self.robot.category, 'Mountain')
        self.assertEqual(self.robot.part_type, 'Legs')
        self.assertEqual(self.robot.capacity, 100)
        self.assertEqual(self.robot.memory, 512)

    def test_invalid_category(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = 'InvalidCategory'
        self.assertEqual(str(ve.exception), "Category should be one of ['Mountain', 'Alpine', 'Indoor', 'Bouldering']")

    def test_valid_installation(self):
        software = {'name': 'ClimbingApp', 'capacity_consumption': 50, 'memory_consumption': 128}
        result = self.robot.install_software(software)
        self.assertIn('successfully installed', result)

    def test_invalid_installation_capacity(self):
        software = {'name': 'HeavyApp', 'capacity_consumption': 150, 'memory_consumption': 128}
        result = self.robot.install_software(software)
        self.assertIn('cannot be installed', result)

    def test_invalid_installation_memory(self):
        software = {'name': 'MemoryHog', 'capacity_consumption': 50, 'memory_consumption': 600}
        result = self.robot.install_software(software)
        self.assertIn('cannot be installed', result)

    def test_get_used_capacity(self):
        software = {'name': 'App1', 'capacity_consumption': 30, 'memory_consumption': 64}
        self.robot.install_software(software)
        self.assertEqual(self.robot.get_used_capacity(), 30)

    def test_get_available_capacity(self):
        software = {'name': 'App2', 'capacity_consumption': 20, 'memory_consumption': 32}
        self.robot.install_software(software)
        self.assertEqual(self.robot.get_available_capacity(), 80)

    def test_get_used_memory(self):
        software = {'name': 'App3', 'capacity_consumption': 40, 'memory_consumption': 128}
        self.robot.install_software(software)
        self.assertEqual(self.robot.get_used_memory(), 128)

    def test_get_available_memory(self):
        software = {'name': 'App4', 'capacity_consumption': 10, 'memory_consumption': 32}
        self.robot.install_software(software)
        self.assertEqual(self.robot.get_available_memory(), 480)

    def test_edge_case_installation(self):
        software = {'name': 'EdgeApp', 'capacity_consumption': 100, 'memory_consumption': 512}
        result = self.robot.install_software(software)
        self.assertIn('successfully installed', result)


if __name__ == '__main__':
    unittest.main()
