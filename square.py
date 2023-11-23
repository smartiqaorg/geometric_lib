import unittest


def area(a): # function that returns area of square 
    return a * a # gets two varibles and return one


def perimeter(a): # function that returns perimeter of square 
    return 4 * a # gets two varibles and return one


class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_int_area(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_float_area(self):
        res = area(4.2)
        self.assertAlmostEqual(res, 17.64 , delta=0.1)

    def test_zero_perimetr(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_int_perimetr(self):
        res = perimeter(10)
        self.assertEqual(res, 40)

    def test_float_perimetr(self):
        res = perimeter(16.8)
        self.assertAlmostEqual(res, 16.8, delta=0.1)
