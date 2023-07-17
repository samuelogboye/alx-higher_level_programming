import unittest
from models.base import Base


class TestBaseMethods(unittest.TestCase):

    def test_parent_initialization(self):
        """Test parent initialization"""
        b1 = Base()
        b2 = Base()
        b3 = Base(10)

        self.assertAlmostEqual(b1.id, 1)
        self.assertAlmostEqual(b2.id, 2)
        self.assertAlmostEqual(b3.id, 10)

    def test_custom_id(self):
        """Test initialization with custom id"""
        b = Base(100)
        self.assertAlmostEqual(b.id, 100)

    def test_increment_id(self):
        """Test id incrementation"""
        b1 = Base()
        b2 = Base()

        self.assertAlmostEqual(b1.id, 1)
        self.assertAlmostEqual(b2.id, 2)

    def test_multiple_instances(self):
        """Test multiple instances"""
        b1 = Base()
        b2 = Base()
        b3 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)


if __name__ == "__main__":
    unittest.main()
