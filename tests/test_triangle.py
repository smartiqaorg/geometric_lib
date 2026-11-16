import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_normal_area(self):
        res = area(10, 5)
        self.assertEqual(res, 25)

    def test_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_float_area(self):
        res = area(2.5, 4.0)
        self.assertAlmostEqual(res, 5.0)

    def test_negative_area(self):
        with self.assertRaises(ValueError):
            area(-5, 4)

    def test_string_area(self):
        with self.assertRaises(TypeError):
            area("5", "4")    

    def test_normal_perimeter(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_float_perimeter(self):
        res = perimeter(2.5, 3.5, 4.0)
        self.assertAlmostEqual(res, 10.0)

    def test_negative_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-5, 4, 1)

    def test_string_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter("5", "4", "3")

    def test_invalid_triangle_perimater(self):
        with self.assertRaises(ValueError):
            perimeter(1, 2, 10)

if __name__ == '__main__':
    unittest.main()