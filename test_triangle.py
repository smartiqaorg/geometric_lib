import unittest
from triangle import area
from triangle import perimeter

class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        res = area(5, 7)
        self.assertEqual(res, 17.5)
    def test_zero_area(self):
        res = area(0, 5)
        self.assertEqual(res, 0)
    def test_float_area(self):
        res = area(3.2, 8.4)
        self.assertEqual(res, 13.440000000000001)
    def test_str_input_area(self):
        with self.assertRaises(TypeError):
            area('a', 10)
    def test_negative_input_area(self):
        res = area(-1, 10)
        self.assertEqual(res, 'incorrect input')
    def test_perimeter(self):
        res = perimeter(2, 3, 5)
        self.assertEqual(res, 10)
    def test_zero_perimeter(self):
        res = perimeter(0, 3, 5)
        self.assertEqual(res, 'incorrect input')
    def test_float_perimeter(self):
        res = perimeter(3.2, 11.1, 1.2)
        self.assertEqual(res, 15.5)
    def test_str_input_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter('a', 10, 2)
    def test_negative_input_perimeter(self):
        res = perimeter(-1, 10, 100)
        self.assertEqual(res, 'incorrect input')