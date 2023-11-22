import unittest


def area(a, b):
    return a * b


def perimeter(a, b):
    return 2 * (a + b)


class RectangleTest(unittest.TestCase):

    def test_area1(self):
        res = area(4, 5)
        self.assertEqual(res, 4 * 5)

    def test_perimeter1(self):
        res = perimeter(2, 5)
        self.assertEqual(res, 2*(2 + 5))

    def test_area2(self):
        res = area(17, 4)
        self.assertEqual(res, 17 * 4)

    def test_perimeter2(self):
        res = perimeter(16, 4)
        self.assertEqual(res, 2 * (16 + 4))

    def test_area3(self):
        res = area(28, 41)
        self.assertEqual(res, 28 * 41)

    def test_perimeter3(self):
        res = perimeter(16, 3)
        self.assertEqual(res, 2 * (16 + 3))


if __name__ == "__main__":
    unittest.ma

