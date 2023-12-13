import unittest
import os

from triangle import area, perimeter

# Устанавливаем PYTHONPATH
path = '/Users/amaliateresenko/geometric_lib'
os.environ['PYTHONPATH'] = path

class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_int_area(self):
        res = area(5, 8)
        self.assertEqual(res, 20)

    def test_float_area(self):
        res = area(3.5, 2.5)
        self.assertEqual(res, 4.375)

    def test_negative_area(self):
        res = area(-3, 1)
        self.assertEqual(res, 'input error')

    def test_string_area(self):
        res = area('a', 1)
        self.assertEqual(res, 'input error')
    

    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_int_perimeter(self):
        res = perimeter(7, 4, 10)
        self.assertEqual(res, 21)

    def test_float_perimeter(self):
        res = perimeter(2.5, 2.5, 3.2)
        self.assertEqual(res, 8.2)

    def test_negative_perimeter(self):
        res = perimeter(-3, 1, 2)
        self.assertEqual(res, 'input error')

    def test_string_perimeter(self):
        res = area('a', 0, -1)
        self.assertEqual(res, 'input error')

if __name__ == "__main__":
	unittest.main()