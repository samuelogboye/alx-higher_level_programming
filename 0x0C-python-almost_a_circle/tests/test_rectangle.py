#!/usr/bin/py

from io import StringIO
from unittest.mock import patch
import os
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

    def test_rectangle_exists(self):
        """Test that a Rectangle object can be created"""
        r = Rectangle(1, 2)
        self.assertIsInstance(r, Rectangle)

    def test_rectangle_with_three_arguments(self):
        """Test that a Rectangle object can be created with three arguments"""
        r = Rectangle(1, 2, 3)
        self.assertIsInstance(r, Rectangle)

    def test_rectangle_with_four_arguments(self):
        """Test that a Rectangle object can be created with four arguments"""
        r = Rectangle(1, 2, 3, 4)
        self.assertIsInstance(r, Rectangle)

    def test_rectangle_with_string_arguments(self):
        """Test, a Rectangle object can't be created with string arguments"""
        with self.assertRaises(TypeError):
            r = Rectangle("1", 2)

    def test_rectangle_with_negative_arguments(self):
        """Test that a Rectangle object can't be created with negative arguments"""
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2)

    def test_display_without_x_and_y(self):
        """Test the display method of Rectangle without x and y"""
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with patch("sys.stdout", new=StringIO()) as fake_output:
            r.display()
            self.assertEqual(fake_output.getvalue(), expected_output)

    def test_display_without_y(self):
        """Test the display method of Rectangle without y"""
        r = Rectangle(3, 2, 1)
        expected_output = " ###\n ###\n"
        with patch("sys.stdout", new=StringIO()) as fake_output:
            r.display()
            self.assertEqual(fake_output.getvalue(), expected_output)

    def test_update_with_kwargs(self):
        """Test the update method of Rectangle with keyword arguments"""
        r = Rectangle(1, 2)
        r.update(id=89, width=1, height=2, x=3, y=4)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_create_with_kwargs(self):
        """Test the create method of Rectangle with keyword arguments"""
        r = Rectangle.create(id=89, width=1, height=2, x=3, y=4)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_save_to_file(self):
        """Test the save_to_file method of Rectangle"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9, 10)
        Rectangle.save_to_file([r1, r2])
        file_exists = os.path.isfile("Rectangle.json")
        self.assertTrue(file_exists)

    def test_load_from_file_nonexistent_file(self):
        """Test the load_from_file method of Rectangle when the file doesn't exist"""
        Rectangle.save_to_file([])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(rectangles, [])

    def test_load_from_file_existing_file(self):
        """Test the load_from_file method of Rectangle when the file exists"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9, 10)
        Rectangle.save_to_file([r1, r2])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 2)
        self.assertIsInstance(rectangles[0], Rectangle)
        self.assertIsInstance(rectangles[1], Rectangle)


    def test_create_rectangle_with_non_integer_arguments(self):
        with self.assertRaises(TypeError):
            rectangle = Rectangle(13, "12")


if __name__ == '__main__':
    unittest.main()
