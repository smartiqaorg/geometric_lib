def area(a,b):
    return a*b

def perimeter(a,b):
    return 2*a+2*b


import unittest

class TestArea(unittest.TestCase):
    def test_rectangle_area_1(self):
        self.assertEqual(area(2, 3), 6)
    def test_rectangle_area_2(self):
        self.assertEqual(area(0, 0), 0)
    def test_rectangle_area_3(self):
        self.assertEqual(area(5, 5), 25)
    def test_rectangle_area_negative_1(self):
        self.assertRaises(TypeError,area, -4)
    def test_rectangle_area_negative_2(self):
        self.assertRaises(TypeError,area, -1)
    def test_circle_area_string(self):
        self.assertRaises(TypeError, area, 'abcыы')


class TestPerimeter(unittest.TestCase):
    def test_perimeter_1(self):
        self.assertEqual(perimeter(2, 3), 10)
    def test_perimeter_2(self):
        self.assertEqual(perimeter(5, 5), 20)
    def test_perimeter_3(self):
        self.assertEqual(perimeter(0, 0), 0)
    def test_rectangle_perimeter_negative(self):
        self.assertRaises(TypeError,perimeter,-1)
    def test_circle_perimeter_string(self):
        self.assertRaises(TypeError, perimeter, 'abcыы')