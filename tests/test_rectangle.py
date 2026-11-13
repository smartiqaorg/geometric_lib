import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_area(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_typical_area(self):
        res = area(10, 5)
        self.assertEqual(res, 50)

    def test_zero_perimeter(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 20)

    def test_typical_perimeter(self):
        res = perimeter(10, 5)
        self.assertEqual(res, 30)

    def test_negative_side_area(self):
        with self.assertRaises(ValueError):
            area(-1, 5)
    
    def test_negative_side_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-1, 5)
    
    def test_string_width_area(self):
        with self.assertRaises(TypeError):
            area("10", 5)

    def test_string_height_area(self):
        with self.assertRaises(TypeError):
            area(10, "5")

    def test_both_strings_area(self):
        with self.assertRaises(TypeError):
            area("10", "5")

    def test_string_width_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter("10", 5)

    def test_string_height_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter(10, "5")

    def test_both_strings_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter("10", "5")


if __name__ == '__main__':
    unittest.main()