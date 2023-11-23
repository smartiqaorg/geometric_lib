import unittest


def area(a, h):
    return a * h / 2


def perimeter(a, b, c):
    return a + b + c


class TriangleTestCase(unittest.TestCase):

    def test_zero(self):
        res_p = perimeter(0, 0, 0)
        res_a = area(0, 0)

        self.assertEqual(res_p, 0)
        self.assertEqual(res_a, 0)

    def test_work_perimeter(self):
        res = perimeter(15, 20, 10)
        self.assertEqual(res, 45)

    def test_work_square(self):
        res = area(20, 5)
        self.assertEqual(res, 50)

    def test_with_zero_perimeter(self):
        res = perimeter(0, 15, 10)
        self.assertEqual(res, -1)

    def test_with_zero_square(self):
        res = area(0, 15)
        self.assertEqual(res, -1)

    def test_negative_perimeter(self):
        res = perimeter(-10, -15, 8)
        self.assertEqual(res, -1)

    def test_negative_square(self):
        res = area(-10, -15)
        self.assertEqual(res, -1)
