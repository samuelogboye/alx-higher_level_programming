#!/usr/bin/py

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(5, 10, 2, 3, 1)

    def test_area(self):
        self.assertEqual(self.rectangle.area(), 50)

    def test_rectangle_attributes(self):
        """Test rectangle attributes"""
        r = Rectangle(10, 20, 1, 2, 100)

        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 100)

        r.width = 30
        r.height = 40
        r.x = 3
        r.y = 4

        self.assertEqual(r.width, 30)
        self.assertEqual(r.height, 40)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_str(self):
        expected_output = "[Rectangle] (1) 2/3 - 5/10"
        self.assertEqual(str(self.rectangle), expected_output)

    def test_update(self):
        self.rectangle.update(2, 7, 12, 4, 5)
        self.assertEqual(self.rectangle.width, 7)
        self.assertEqual(self.rectangle.height, 12)
        self.assertEqual(self.rectangle.x, 4)
        self.assertEqual(self.rectangle.y, 5)

    def test_to_dictionary(self):
        expected_output = {
            'id': 1,
            'width': 5,
            'height': 10,
            'x': 2,
            'y': 3
        }
        self.assertEqual(self.rectangle.to_dictionary(), expected_output)


if __name__ == '__main__':
    unittest.main()
