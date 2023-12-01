import unittest

from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle(15.00, 420.00)

    def testInit(self):
        self.assertEqual(15.00, self.vehicle.fuel)
        self.assertEqual(420.00, self.vehicle.horse_power)
        self.assertEqual(15.00, self.vehicle.capacity)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)
        self.assertIsInstance(self.vehicle.fuel, float)
        self.assertIsInstance(self.vehicle.capacity, float)
        self.assertIsInstance(self.vehicle.horse_power, float)
        self.assertIsInstance(self.vehicle.fuel_consumption, float)

    def testDrivingGood(self):
        expected_fuel_left = self.vehicle.fuel - (self.vehicle.fuel_consumption * 5)
        self.vehicle.drive(kilometers=5)
        self.assertEqual(expected_fuel_left, self.vehicle.fuel)

    def testDrivingBad(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(kilometers=100)
        self.assertEqual(str(ex.exception), 'Not enough fuel')

    def testDrivingExactFuel(self):
        self.vehicle.drive(kilometers=12)
        self.assertEqual(0, self.vehicle.fuel)

    def testRefuelGood(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel(fuel=5)
        self.assertEqual(5, self.vehicle.fuel)

    def testRefuelBad(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(500)
        self.assertEqual(str(ex.exception), 'Too much fuel')

    def testRefuelMaxCapacity(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel(fuel=self.vehicle.capacity)
        self.assertEqual(self.vehicle.capacity, self.vehicle.fuel)

    def test__str(self):
        obj = self.vehicle
        expected_string = f"The vehicle has {self.vehicle.horse_power} " \
                          f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        self.assertEqual(str(obj), expected_string)


if __name__ == '__main__':
    unittest.main()
