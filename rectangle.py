import unittest


def area(a, b):
    return a * b


def perimeter(a, b):
    return 2 * (a + b)


class RectangleTestCase(unittest.TestCase):

    def test_zero(self):
        res_p = perimeter(0, 0)
        res_a = area(0, 0)

        self.assertEqual(res_p, 0)
        self.assertEqual(res_a, 0)

    def test_work_perimeter(self):
        res = perimeter(120, 15)
        self.assertEqual(res, 270)

    def test_work_square(self):
        res = area(120, 15)
        self.assertEqual(res, 1800)

    def test_with_zero_perimeter(self):
        res = perimeter(0, 15)
        self.assertEqual(res, -1)

    def test_with_zero_square(self):
        res = area(0, 15)
        self.assertEqual(res, -1)

    def test_negative_perimeter(self):
        res = perimeter(-10, -15)
        self.assertEqual(res, -1)

    def test_negative_square(self):
        res = area(-10, -15)
        self.assertEqual(res, -1)
