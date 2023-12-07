import unittest

from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_int_perimeter(self):
        res = perimeter(10, 10, 12)
        self.assertEqual(res, 32)

    def test_float_area(self):
        res = area(3.5, 2.5)
        self.assertEqual(res, 4.375)

    def test_float_perimeter(self):
        res = perimeter(2.5, 2.5, 3.2)
        self.assertEqual(res, 8.2)

    def test_string_perimeter(self):
        res = perimeter("abc", 2, -1)
        self.assertEqual(res, "error")

    def test_string_area(self):
        res = area("abc", 2)
        self.assertEqual(res, "error")
    
    def test_negative_perimeter(self):
        res = perimeter(-2.5, -10, 34)
        self.assertEqual(res, "error")

    def test_negative_area(self):
        res = area(-2, -10)
        self.assertEqual(res, "error")

if __name__ == "__main__":
    unittest.main()