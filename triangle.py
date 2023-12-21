import unittest

def area(a, h):
    return a * h / 2

def perimetr(a, b, c):
    return a + b + c

class TriangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_area_multiple(self):
        res1 = area(4, 3)
        res2 = area(11, 3)
        self.assertAlmostEqual(res1, 6.0, places=1)
        self.assertAlmostEqual(res2, 16.5, places=1)

    def test_area_float_number(self):
        res = area(10.6, 2)
        self.assertAlmostEqual(res, 10.6, places=1)

    def test_area_negative_number(self):
        with self.assertRaises(Exception):
            area(-10, -20)

    def test_perimetr_zero(self):
        res = perimetr(0, 0, 0)
        self.assertEqual(res, 0)

    def test_perimetr_multiple(self):
        res1 = perimetr(5, 3, 1)
        self.assertEqual(res1, 9)

    def test_perimetr_float_number(self):
        res = perimetr(10.5, 2, 3)
        self.assertEqual(res, 15.5)

    def test_perimetr_negative_number(self):
        with self.assertRaises(Exception):
            perimetr(-10, -10, -10)