import unittest


def area(a):
    return a * a


def perimeter(a):
    return 4 * a


class SquareTest(unittest.TestCase):

    def test_area1(self):
        res = area(7)
        self.assertEqual(res, 49)

    def test_area2(self):
        res = area(17)
        self.assertEqual(res, 289)

    def test_area3(self):
        res = area(104)
        self.assertEqual(res, 10_816)

    def test_perimeter1(self):
        res = perimeter(4)
        self.assertEqual(res, 16)

    def test_peimeter2(self):
        res = perimeter(17)
        self.assertEqual(res, 68)

    def test_perimeter3(self):
        res = perimeter(10)
        self.assertEqual(res, 40)


if __name__ == "__main__":
    unittest.ma
