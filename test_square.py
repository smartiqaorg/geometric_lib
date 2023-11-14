import unittest
from square import area
from square import perimeter
class TestSquareFunctions(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_rand(self):
        self.assertAlmostEqual(area(7), 49)
        self.assertAlmostEqual(area(32), 1024)
        self.assertAlmostEqual(area(125.89), 15848.2921)

    def test_area_values(self):
        with self.assertRaises(ValueError):
            perimeter(-1)
        with self.assertRaises(ValueError):
            perimeter(-2)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_rand(self):
        self.assertAlmostEqual(perimeter(125.89), 503.56)
        self.assertAlmostEqual(perimeter(4), 16)
        self.assertAlmostEqual(perimeter(7), 28)

    def test_perimeter_values(self):
        with self.assertRaises(ValueError):
            perimeter(-1)
        with self.assertRaises(ValueError):
            perimeter(-2)
