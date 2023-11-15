import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_wrong_type_area(self):
        self.assertEqual(area("5"),25)
        self.assertEqual(area("7"),49)

    def test_wrong_value_area(self):
        self.assertRaises(ValueError, area, -5)
        self.assertRaises(ValueError, area, "-5")
    def test_area(self):
        self.assertEqual(area(5),25)
        self.assertEqual(area(7),49)
    def test_zero_area(self):
        self.assertEqual(area(0), 0)
        self.assertEqual(area("0"), 0)

    def test_wrong_type_perimeter(self):
        self.assertEqual(perimeter("5"),25)
        self.assertEqual(perimeter("7"),49)

    def test_wrong_value_perimeter(self):
        self.assertRaises(ValueError, perimeter, -5)
        self.assertRaises(ValueError, perimeter, "-5")
    def test_perimeter(self):
        self.assertEqual(perimeter(5),25)
        self.assertEqual(perimeter(7),49)
    def test_zero_perimeter(self):
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter("0"), 0)
    