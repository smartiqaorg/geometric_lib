import unittest
import os

from rectangle import area, perimeter

# Устанавливаем PYTHONPATH
path = '/Users/amaliateresenko/geometric_lib'
os.environ['PYTHONPATH'] = path

class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_zero_perimeter(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_int_area(self):
        res = area(20, 20)
        self.assertEqual(res, 400)

    def test_int_perimeter(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_float_area(self):
        res = area(2.0, 3.5)
        self.assertEqual(res, 7.0)

    def test_float_perimeter(self):
        res = perimeter(2.5, 3.5)
        self.assertEqual(res, 12.0)

if __name__ == "__main__":
	unittest.main()