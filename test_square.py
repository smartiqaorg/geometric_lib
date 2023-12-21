
def area(a):
    return a * a


def perimeter(a):
    return 4 * a


import unittest

class TestArea(unittest.TestCase):
    def test_square_area_1(self):
        self.assertEqual(area(2), 4)
    def test_square_area_2(self):
        self.assertEqual(area(0), 0)
    def test_square_area_3(self):
        self.assertEqual(area(5), 25)
    def test_square_area_negative(self):
        self.assertEqual(TypeError,area, -1)
    def test_square_area_string(self):
        self.assertEqual(TypeError,area, 'abcыы')

class TestPerimeter(unittest.TestCase):
    def test_perimeter_1(self):
        self.assertEqual(perimeter(2), 8)
    def test_perimeter_2(self):
        self.assertEqual(perimeter(5), 20)
    def test_perimeter_3(self):
        self.assertEqual(perimeter(0), 0)
    def test_perimeter_negative(self):
        self.assertEqual(TypeError,perimeter, -1)
    def test_square_perimeter_string(self):
        self.assertEqual(TypeError,perimeter, 'abcыы')