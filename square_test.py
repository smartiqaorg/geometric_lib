import unittest

from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_int_area(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_int_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 40)

    def test_float_area(self):
        res = area(2.5)
        self.assertEqual(res, 6.25)

    def test_float_perimeter(self):
        res = perimeter(2.5)
        self.assertEqual(res, 10)

    def test_string_perimeter(self):
        res = perimeter("abc")
        self.assertEqual(res, "error")

    def test_string_area(self):
        res = area("abc")
        self.assertEqual(res, "error")
    
    def test_negative_perimeter(self):
        res = perimeter(-2.5)
        self.assertEqual(res, "error")

    def test_negative_area(self):
        res = area(-2)
        self.assertEqual(res, "error")

if __name__ == "__main__":
    unittest.main()