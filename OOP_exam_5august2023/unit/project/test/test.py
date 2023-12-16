from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class TestCar(TestCase):

    def setUp(self):
        self.car = SecondHandCar("BMW", "e46", 310000, 2600.99)

    def test_init(self):
        self.assertEqual(self.car.model, 'BMW')
        self.assertEqual(self.car.car_type, 'e46')
        self.assertEqual(self.car.mileage, 310000)
        self.assertTrue(isinstance(self.car.mileage, int))
        self.assertEqual(self.car.price, 2600.99)
        self.assertTrue(isinstance(self.car.price, float))

    def test_free_car(self):
        with self.assertRaises(ValueError) as ve:
            self.free_car = SecondHandCar("Opel", "Cadet", 2838281, 0.50)
        self.assertEqual(str(ve.exception), 'Price should be greater than 1.0!')

    def test_new_car(self):
        """test with less than 100mileage"""
        with self.assertRaises(ValueError) as ve:
            self.new_car = SecondHandCar("BMW", "m4", 99, 280000.99)
        self.assertEqual(str(ve.exception), 'Please, second-hand cars only! '
                                            'Mileage must be greater than 100!')

    # set promo price
    def test_increase_price(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(350000)
        self.assertEqual(str(ve.exception), 'You are supposed to decrease the price!')

    def test_promo_price(self):
        result = self.car.set_promotional_price(2500)
        self.assertEqual(result, 'The promotional price has been successfully set.')
        self.assertEqual(self.car.price, 2500)

    # repair tests
    def test_impossible_repair(self):
        result = self.car.need_repair(2000, 'New engine block.')
        self.assertEqual(result, 'Repair is impossible!')

    def test_repair(self):
        new_price = self.car.price + 130
        result = self.car.need_repair(130, 'Oil and filters.')
        self.assertEqual(result, 'Price has been increased due to repair charges.')
        self.assertEqual(self.car.price, new_price)
        self.assertEqual(len(self.car.repairs), 1)
        self.assertEqual(self.car.repairs[0], 'Oil and filters.')

    def test_cars_compare(self):
        car1 = SecondHandCar("BMW", "e46", 25000, 16000.99)
        car2 = SecondHandCar("BMW", "e46", 310000, 2600.99)
        car3 = SecondHandCar("BMW", "e36", 315000, 2600.99)

        result_mismatch = car1 > car3
        result_ok = car1 > car2

        self.assertEqual(result_mismatch, 'Cars cannot be compared. Type mismatch!')
        self.assertTrue(result_ok)

    def test_str(self):
        expected_output = ("Model BMW | Type e46 | Milage 310000km\n"
                           "Current price: 2600.99 | Number of Repairs: 0")
        self.assertEqual(str(self.car), expected_output)

if __name__ == '__main__':
    main()
