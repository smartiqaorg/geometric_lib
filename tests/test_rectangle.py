import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_normal_area(self):
        res = area(10, 5)
        self.assertEqual(res, 50)

    def test_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_float_area(self):
        res = area(2.5, 4.0)
        self.assertAlmostEqual(res, 10.0)

    def test_negative_area(self):
        with self.assertRaises(ValueError):
            area(-5, 4)

    def test_string_area(self):
        with self.assertRaises(TypeError):
            area("5", "4")    

    def test_normal_perimeter(self):
        res = perimeter(10, 5)
        self.assertEqual(res, 30)

    def test_zero_perimeter(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_float_perimeter(self):
        res = perimeter(2.5, 3.5)
        self.assertAlmostEqual(res, 12.0)

    def test_negative_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-5, 4)

    def test_string_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter("5", "4")

if __name__ == '__main__':
    unittest.main()