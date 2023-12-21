import unittest


def area(a, b):
    return a * b


def perimeter(a, b):
    return 2 * (a + b)


class RectangleTest(unittest.TestCase):

    def test_area1(self):
        res = area(4, 5)
        self.assertEqual(res, 20)

    def test_perimeter1(self):
        res = perimeter(2, 5)
        self.assertEqual(res, 14)

    def test_area2(self):
        res = area(17, 4.4)
        self.assertEqual(res, 74.8)

    def test_perimeter2(self):
        res = perimeter(16.2, 4.7)
        self.assertEqual(res, 41.8)

    def test_area3(self):
        with self.assertRaises(Exception):
            area(28, -41)

    def test_perimeter3(self):
        with self.assertRaises(Exception):
            perimeter(16, -3)
    

if __name__ == "__main__":
    unittest.ma

