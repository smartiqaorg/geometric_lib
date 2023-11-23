import unittest


def area(a, h): # function that returns area of triangle
    return a * h / 2  # gets two varibles and return one


def perimeter(a, b, c): # function that returns perimeter of square 
    return a + b + c # gets two varibles and return one


class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_area(self):
        res = area(10, 10)
        self.assertEqual(res, 50)

    def test_float_area(self):
        res = area(6.4, 5.239)
        self.assertAlmostEqual(res, 16.7648, delta=0.1)

    def test_zero_perimetr(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_square_perimetr(self):
        res = perimeter(10, 10, 10)
        self.assertEqual(res, 30)

    def test_float_perimetr(self):
        res = perimeter(6.4, 5.239, 2)
        self.assertAlmostEqual(res, 13.639, delta=0.1)
