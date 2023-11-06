import unittest


class RectangleTestCase(unittest.TestCase):
    def test_zero_area_case(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_general_area_case(self):
        res = area(1337)
        self.assertEqual(res, 1787569)

    def test_zero_perimeter_case(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_general_perimeter_case(self):
        res = perimeter(1337)
        self.assertEqual(res, 5348)


def area(a):
    return a * a


def perimeter(a):
    return 4 * a
