import math

def area_rectangle(a, b):
    return a * b
def perimeter_rectangle(a, b):
    return 2*(a + b)

def area_square(a):
    return a * a

def perimeter_square(a):
    return 4 * a

def area_triangle(a, h):
	return a * h / 2
def perimeter_triangle(a, b, c):
	return a + b + c

def area_circle(r):
    return math.pi * r * r
def perimeter_circle(r):
    return 2 * math.pi * r

import unittest

class TestCase(unittest.TestCase):
    def test_one_area_rectangle(self):
        res = area_rectangle(10, 0)
        self.assertEqual(res, 0)

    def test_two_perimetr_rectangle(self):
        res = area_rectangle(5, 25)
        self.assertEqual(res, 125)

    def test_three_area_square(self):
        res = area_square(14)
        self.assertEqual(res, 196)

    def test_four_perimetr_square(self):
        res = perimeter_square(21)
        self.assertEqual(res, 84)

    def test_five_area_triangle(self):
        res = area_triangle(7262, 9146)
        self.assertEqual(res, 33209126)

    def test_six_perimeter_triangle(self):
        res = perimeter_triangle(10, 10, 20)
        self.assertEqual(res, 40)

    def test_seven_area_circle(self):
        res = area_circle(5)
        self.assertEqual(res, 78.53981633974483)

    def test_eight_perimetr_circle(self):
        res = perimeter_circle(5)
        self.assertEqual(res, 31.41592653589793)


if __name__ == '__main__':
    unittest.main()
