import unittest
from rectangle import area
from rectangle import perimeter

class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        res = area(5, 3)
        self.assertEqual(res, 15)
    def test_zero_area(self):
        res = area(0, 100)
        self.assertEqual(res, 0)
    def test_float_area(self):
        res = area(3.5, 7.2)
        self.assertEqual(res, 25.2)
    def test_str_input_area(self):
        with self.assertRaises(TypeError):
            perimeter('a', 10)
    def test_perimeter(self):
        res = perimeter(5, 3)
        self.assertEqual(res, 16)
    def test_zero_perimeter(self):
        res = perimeter(0, 100)
        self.assertEqual(res, 0)
    def test_float_perimeter(self):
        res = perimeter(3.5, 7.2)
        self.assertEqual(res, 21.4)
    def test_str_input_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter('a', 10)
