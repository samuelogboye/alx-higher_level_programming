#!/usr/bin/python3

import unittest
from models.square import Square


class SquareTest(unittest.TestCase):
    def setUp(self):
        self.square = Square(5, 2, 3, 1)

    def test_attributes(self):
        self.assertEqual(self.square.size, 5)
        self.assertEqual(self.square.x, 2)
        self.assertEqual(self.square.y, 3)
        self.assertEqual(self.square.id, 1)

    def test_string_representation(self):
        self.assertEqual(str(self.square), "[Square] (1) 2/3 - 5")

    def test_update_method(self):
        self.square.update(2, 10, 4, 6)
        self.assertEqual(self.square.id, 2)
        self.assertEqual(self.square.size, 10)
        self.assertEqual(self.square.x, 4)
        self.assertEqual(self.square.y, 6)

    def test_to_dictionary_method(self):
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(self.square.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
