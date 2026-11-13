import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):

    def test_unit_area(self):
        res = area(1)
        self.assertEqual(res, 1)

    def test_typical_area(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_typical_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 40)

    def test_negative_side_area(self):
        with self.assertRaises(ValueError):
            area(-5)

    def test_negative_side_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-5)
    
    def test_string_side_area(self):
        with self.assertRaises(TypeError):
            area("10")

    def test_string_side_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter("10")

    def test_invalid_string_area(self):
        with self.assertRaises((TypeError, ValueError)):
            area("abc")

    def test_invalid_string_perimeter(self):
        with self.assertRaises((TypeError, ValueError)):
            perimeter("abc")



if __name__ == '__main__':
    unittest.main()