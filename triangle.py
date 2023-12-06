import unittest


def area(a, h):
    return a * h / 2


def perimeter(a, b, c):
    return a + b + c


class TriangleTestCase(unittest.TestCase):
    def test_square_mul(self):
        res1 = area(10, 0)
        self.assertEqual(res1, 0)

        res2 = area(10, 1)
        self.assertEqual(res2, 5)

        res3 = area(-5, 6)
        self.assertEqual(res3, "error")

        res4 = area(100, 100)
        self.assertEqual(res4, 5000)

        res5 = area(26, 25.25)
        self.assertEqual(res5, 328.25)

    def test_perimeter_mul(self):
        res1 = perimeter(0, 0, 0)
        self.assertEqual(res1, 0)

        res2 = perimeter(10, 1, 5)
        self.assertEqual(res2, 16)

        res3 = perimeter(-5, 5, 5)
        self.assertEqual(res3, "error")

        res4 = perimeter(100, 100, 200)
        self.assertEqual(res4, 400)

        res5 = perimeter(25, 25, 5.25)
        self.assertEqual(res5, 55.25)