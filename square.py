import unittest


class SquareTestCase(unittest.TestCase):
    def test_zero_area_case(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_general_area_case(self):
        res = area(1337)
        self.assertEqual(res, 1787569)

    def test_negative_value_area_case(self):
        with self.assertRaises(ValueError):
            area(-1337)

    def test_wrong_type_value_area_case(self):
        with self.assertRaises(TypeError):
            area("abcd")

    def test_zero_perimeter_case(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_general_perimeter_case(self):
        res = perimeter(1337)
        self.assertEqual(res, 5348)

    def test_negative_value_perimeter_case(self):
        with self.assertRaises(ValueError):
            perimeter(-1337)

    def test_wrong_type_value_perimeter_case(self):
        with self.assertRaises(TypeError):
            perimeter("abcd")


def area(a):
    return a * a


def perimeter(a):
    return 4 * a
