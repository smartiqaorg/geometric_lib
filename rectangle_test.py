import unittest

from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_int_area(self):
        res = area(10, 20)
        self.assertEqual(res, 200)

    def test_int_perimeter(self):
        res = perimeter(10, 20)
        self.assertEqual(res, 60)

    def test_float_area(self):
        res = area(2.5, 3.5)
        self.assertEqual(res, 8.75)

    def test_float_perimeter(self):
        res = perimeter(2.5, 3.5)
        self.assertEqual(res, 12.0)

    def test_string_perimeter(self):
        res = perimeter("abc", 2)
        self.assertEqual(res, "error")

    def test_string_area(self):
        res = area("abc", 2)
        self.assertEqual(res, "error")
    
    def test_negative_perimeter(self):
        res = perimeter(-2.5, -10)
        self.assertEqual(res, "error")

    def test_negative_area(self):
        res = area(-2, -10)
        self.assertEqual(res, "error")

if __name__ == "__main__":
    unittest.main()
