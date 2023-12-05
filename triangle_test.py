import unittest

from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_int_area(self):
        res = area(10, 8)
        self.assertEqual(res, 40)

    def test_int_perimeter(self):
        res = perimeter(10, 10, 12)
        self.assertEqual(res, 32)

    def test_float_area(self):
        res = area(3.5, 2.5)
        self.assertEqual(res, 4.375)

    def test_float_perimeter(self):
        res = perimeter(2.5, 2.5, 3.2)
        self.assertEqual(res, 8.2)

if __name__ == "__main__":
    unittest.main()