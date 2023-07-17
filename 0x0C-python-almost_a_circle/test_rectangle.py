#!/usr/bin/py

import unittest
from models.rectangle import Rectangle


class TestRectangleMethods(unittest.TestCase):

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

    def test_rectangle_area(self):
        """Test rectangle area calculation"""
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

        r.width = 8
        r.height = 15
        self.assertEqual(r.area(), 120)

    def test_rectangle_str(self):
        """Test rectangle string representation"""
        r = Rectangle(7, 7, 1, 1, 200)
        self.assertEqual(str(r), "[Rectangle] (200) 1/1 - 7/7")

    def test_rectangle_update(self):
        """Test rectangle update method"""
        r = Rectangle(10, 20, 1, 2, 300)

        r.update(50)
        self.assertEqual(r.id, 50)

        r.update(50, 30)
        self.assertEqual(r.width, 30)

        r.update(50, 30, 40)
        self.assertEqual(r.height, 40)

        r.update(50, 30, 40, 50)
        self.assertEqual(r.x, 50)

        r.update(50, 30, 40, 50, 60)
        self.assertEqual(r.y, 60)

    def test_rectangle_to_dictionary(self):
        """Test rectangle to_dictionary method"""
        r = Rectangle(5, 10, 2, 3, 400)
        expected_dict = {'id': 400, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        self.assertEqual(r.to_dictionary(), expected_dict)


if __name__ == "__main__":
    unittest.main()
