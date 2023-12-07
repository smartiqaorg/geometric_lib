import unittest


def area(a, h):
    return a * h / 2


def perimeter(a, b, c):
    return a + b + c


class TriangleTestCase(unittest.TestCase):
    def test_square_mul1(self):
        res1 = area(10, 0)
        self.assertEqual(res1, 0)

    def test_square_mul2(self):
        res2 = area(10, 1)
        self.assertEqual(res2, 5)

    def test_square_mul3(self):
        with self.assertRaises(Exception):
            area(-234, 34)

    def test_square_mul4(self):
        res4 = area(100, 100)
        self.assertEqual(res4, 5000)

    def test_square_mul5(self):
        res5 = area(26, 25.25)
        self.assertEqual(res5, 328.25)

    def test_perimeter_mul1(self):
        res1 = perimeter(0, 0, 0)
        self.assertEqual(res1, 0)

    def test_perimeter_mul2(self):
        res2 = perimeter(10, 1, 5)
        self.assertEqual(res2, 16)

    def test_perimeter_mul3(self):
        with self.assertRaises(Exception):
            perimeter(-578, 82, 33)

    def test_perimeter_mul4(self):
        res4 = perimeter(100, 100, 200)
        self.assertEqual(res4, 400)

    def test_perimeter_mul5(self):
        res5 = perimeter(25, 25, 5.25)
        self.assertEqual(res5, 55.25)