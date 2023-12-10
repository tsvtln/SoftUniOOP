from collections import deque
from unittest import TestCase, main

from project.railway_station import RailwayStation


class TestStation(TestCase):
    def setUp(self):
        self.station = RailwayStation('Gara_Iskur')

    def test_init(self):
        self.assertEqual(self.station.name, 'Gara_Iskur')
        self.assertEqual(self.station.arrival_trains, deque())
        self.assertEqual(self.station.departure_trains, deque())

    def test_name_property(self):
        with self.assertRaises(ValueError) as ve:
            self.station.name = 'Ab'
        self.assertEqual(str(ve.exception), "Name should be more than 3 symbols!")

    def test_new_arrival_on_board(self):
        self.station.new_arrival_on_board('Train 1')
        self.assertEqual(self.station.arrival_trains, deque(['Train 1']))

    def test_train_has_arrived(self):
        self.station.new_arrival_on_board('Train 1')
        self.station.new_arrival_on_board('Train 2')

        result = self.station.train_has_arrived('Train 2')
        self.assertEqual(result, 'There are other trains to arrive before Train 2.')
        self.assertEqual(self.station.arrival_trains, deque(['Train 1', 'Train 2']))
        self.assertEqual(self.station.departure_trains, deque([]))

    def test_train_has_arrived_invalid_order(self):
        self.station.new_arrival_on_board('Train 1')
        self.station.new_arrival_on_board('Train 2')

        result = self.station.train_has_arrived('Train 1')
        self.assertEqual(result, 'Train 1 is on the platform and will leave in 5 minutes.')
        self.assertEqual(self.station.arrival_trains, deque(['Train 2']))
        self.assertEqual(self.station.departure_trains, deque(['Train 1']))

    def test_train_has_left(self):
        self.station.new_arrival_on_board('Train 1')
        self.station.train_has_arrived('Train 1')

        result = self.station.train_has_left('Train 1')
        self.assertTrue(result)
        self.assertEqual(self.station.departure_trains, deque())

    def test_train_has_left_invalid_train(self):
        self.station.new_arrival_on_board('Train 1')
        self.station.train_has_arrived('Train 1')

        result = self.station.train_has_left('Train 2')
        self.assertFalse(result)
        self.assertEqual(self.station.departure_trains, deque(['Train 1']))


if __name__ == '__main__':
    main()
