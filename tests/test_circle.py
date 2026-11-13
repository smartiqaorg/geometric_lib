import unittest
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_unit_area(self):
        res = area(1)
        self.assertAlmostEqual(res, 3.14159, places=4)

    def test_typical_area(self):
        res = area(5)
        self.assertAlmostEqual(res, 78.5398, places=4)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_typical_perimeter(self):
        res = perimeter(5)
        self.assertAlmostEqual(res, 31.4159, places=4)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            area(-1)
    
    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            perimeter(-1)

    def test_string_radius_area(self):
        with self.assertRaises(TypeError):
            area("5")

    def test_string_radius_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter("5")

    def test_invalid_string_area(self):
        with self.assertRaises((TypeError, ValueError)):
            area("abc")

    def test_invalid_string_perimeter(self):
        with self.assertRaises((TypeError, ValueError)):
            perimeter("qwqewrt")


if __name__ == '__main__':
    unittest.main()