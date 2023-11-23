import unittest

def area(a, b): # Function that returns area of rectangle
    return a * b 


def perimeter(a, b): # function that returns perimeter of rectangle
    return 2*(a + b) # gets 2 varibles and returns one


class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_area(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_float_area(self):
        res = area(6.4, 5.239)
        self.assertAlmostEqual(res, 33.5296, delta=0.1)

    def test_zero_perimetr(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_square_perimetr(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_float_perimetr(self):
        res = perimeter(6.4, 5.239)
        self.assertAlmostEqual(res, 23.278, delta=0.1)
