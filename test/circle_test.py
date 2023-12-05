import unittest
import os

from circle import area, perimeter

# Устанавливаем PYTHONPATH
path = '/Users/amaliateresenko/geometric_lib'
os.environ['PYTHONPATH'] = path

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_int_area(self):
        res = area(10)
        self.assertEqual(res, 314.1592653589793)

    def test_int_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 62.83185307179586)

    def test_float_area(self):
        res = area(2.3)
        self.assertEqual(res, 16.619025137490002)

    def test_float_perimeter(self):
        res = perimeter(1.5)
        self.assertEqual(res, 9.42477796076938)

if __name__ == "__main__":
	unittest.main()