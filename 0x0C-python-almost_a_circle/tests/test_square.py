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

    def test_create_square_with_default_values(self):
        square = Square(1)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertEqual(square.id, 12)

    def test_create_square_with_negative_size(self):
        with self.assertRaises(ValueError):
            square = Square(1, 2, -1, 4)

    def test_create_square_with_non_integer_arguments(self):
        with self.assertRaises(TypeError):
            square = Square(1, 2, '1', 3)

        with self.assertRaises(TypeError):
            square = Square(1, '2', 3, 1)

        with self.assertRaises(TypeError):
            square = Square(1, 2, '3', 1)

        with self.assertRaises(TypeError):
            S = Square('width', 'height')

        with self.assertRaises(TypeError):
            S = Square(2.4, 1.3)

        with self.assertRaises(TypeError):
            S = Square(1, 2, 'x value', 'y value')

        with self.assertRaises(TypeError):
            S = Square(1, 2, 2.4, 1.3)

        with self.assertRaises(TypeError):
            S = Square(True, False)

        with self.assertRaises(TypeError):
            S = Square(1, 2, '2', 1)

        with self.assertRaises(TypeError):
            S = Square([1, 1], 2, 3, 4)

        with self.assertRaises(TypeError):
            S = Square((1, 2), 'x value', 'y value')

        with self.assertRaises(TypeError):
            S = Square({1: 3, 2: 4}, 5, 6)

    def test_create_square_with_invalid_attributes(self):
        with self.assertRaises(ValueError):
            square = Square(1, 2, -1, 4)

    def test_create_square_with_extra_attributes(self):
        with self.assertRaises(TypeError):
            square = Square(1, 2, 3, 1, extra=5)

    def test_update_square_with_invalid_attributes(self):
        with self.assertRaises(ValueError):
            self.square.update(2, -10, 4, 6)

    def test_update_square_with_non_integer_arguments(self):
        with self.assertRaises(TypeError):
            self.square.update("2", 10, 4, 6)

        with self.assertRaises(TypeError):
            self.square.update(2, "10", 4, 6)

        with self.assertRaises(TypeError):
            self.square.update(2, 10, "4", 6)

        with self.assertRaises(TypeError):
            self.square.update(2, 10, 4, "6")

    def test_to_dictionary_method_with_updated_square(self):
        self.square.update(2, 10, 4, 6)
        expected_dict = {'id': 2, 'size': 10, 'x': 4, 'y': 6}
        self.assertEqual(self.square.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
