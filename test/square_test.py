import unittest
import os

from square import area, perimeter

# Устанавливаем PYTHONPATH
path = '/Users/amaliateresenko/geometric_lib'
os.environ['PYTHONPATH'] = path

class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_int_area(self):
        res = area(5)
        self.assertEqual(res, 25)

    def test_int_perimeter(self):
        res = perimeter(5)
        self.assertEqual(res, 20)

    def test_float_area(self):
        res = area(5.5)
        self.assertEqual(res, 30.25)

    def test_float_perimeter(self):
        res = perimeter(1.5)
        self.assertEqual(res, 6.0)

if __name__ == "__main__":
	unittest.main()