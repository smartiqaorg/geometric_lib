import unittest
import os

from square import area, perimeter

# Устанавливаем PYTHONPATH
path = '/Users/amaliateresenko/geometric_lib'
os.environ['PYTHONPATH'] = path

class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertAlmostEqual(res, 0, delta=3)

    def test_int_area(self):
        res = area(5)
        self.assertAlmostEqual(res, 25, delta=3)

    def test_float_area(self):
        res = area(5.5)
        self.assertAlmostEqual(res, 30.25, delta=3)

    def test_negative_area(self):
        with self.assertRaises(ValueError):
            area(-2)

    def test_string_area(self):
        with self.assertRaises(TypeError):
            area('a')


    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertAlmostEqual(res, 0, delta=3)

    def test_int_perimeter(self):
        res = perimeter(5)
        self.assertAlmostEqual(res, 20, delta=3)

    def test_float_perimeter(self):
        res = perimeter(1.5)
        self.assertAlmostEqual(res, 6.0, delta=3)

    def test_incorrect_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-3)

    def test_string_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter('a')
            
if __name__ == "__main__":
	unittest.main()