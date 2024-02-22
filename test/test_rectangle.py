import unittest
import rectangle


class RectangleAreaTestCase(unittest.TestCase):
    def test_zero_side(self):
        self.assertRaises(ValueError, rectangle.area, 0, 3)

    def test_simple(self):
        res = rectangle.area(2, 3)
        self.assertEqual(res, 6)

    def test_huge(self):
        res = rectangle.area(9999999, 9999888)
        exp_res = 99998870000112
        self.assertEqual(res, exp_res)

    def test_neg(self):
        self.assertRaises(ValueError, rectangle.area, -2, 3)

    def test_invalid(self):
        self.assertRaises(TypeError, rectangle.area, "100", 3)


class RectanglePerTestCase(unittest.TestCase):
    def test_zero_side(self):
        self.assertRaises(ValueError, rectangle.perimeter, 0, 3)

    def test_simple(self):
        res = rectangle.perimeter(2, 3)
        self.assertEqual(res, 10)

    def test_huge(self):
        res = rectangle.perimeter(9999999, 9999888)
        exp_res = 39999774
        self.assertEqual(res, exp_res)

    def test_neg(self):
        self.assertRaises(ValueError, rectangle.perimeter, -2, 3)

    def test_invalid(self):
        self.assertRaises(TypeError, rectangle.perimeter, "100", 3)
