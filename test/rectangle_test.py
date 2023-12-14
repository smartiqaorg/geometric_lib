import unittest
import os

from rectangle import area, perimeter

# Устанавливаем PYTHONPATH
path = '/Users/amaliateresenko/geometric_lib'
os.environ['PYTHONPATH'] = path

class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(10, 0)
        self.assertAlmostEqual(res, 0, delta=3)

    def test_int_area(self):
        res = area(20, 20)
        self.assertAlmostEqual(res, 400, delta=3)

    def test_float_area(self):
        res = area(2.0, 3.5)
        self.assertAlmostEqual(res, 7.0, delta=3)

    def test_negative_area(self):
        with self.assertRaises(ValueError):
            area(-3, -1)

    def test_string_area(self):
        with self.assertRaises(TypeError):
            area('a', 2)


    def test_zero_perimeter(self):
        res = perimeter(0, 0)
        self.assertAlmostEqual(res, 0, delta=3)

    def test_int_perimeter(self):
        res = perimeter(10, 10)
        self.assertAlmostEqual(res, 40, delta=3)

    def test_float_perimeter(self):
        res = perimeter(2.5, 3.5)
        self.assertAlmostEqual(res, 12.0, delta=3)

    def test_incorrect_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-3, 1)

    def test_string_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter('a', 2)

if __name__ == "__main__":
	unittest.main()