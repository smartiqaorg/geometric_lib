import unittest

from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_int_area(self):
        res = area(10)
        self.assertAlmostEqual(res, 314.159, 3)

    def test_int_perimeter(self):
        res = perimeter(10)
        self.assertAlmostEqual(res, 62.832, 3)

    def test_float_area(self):
        res = area(2.5)
        self.assertAlmostEqual(res, 19.635, 3)

    def test_float_perimeter(self):
        res = perimeter(2.5)
        self.assertAlmostEqual(res, 15.708, 3)

    def test_string_perimeter(self):
        res = perimeter("abc")
        self.assertAlmostEqual(res, "error", 3)

    def test_string_area(self):
        res = area("abc")
        self.assertAlmostEqual(res, "error", 3)
    
    def test_negative_perimeter(self):
        res = perimeter(-2.5)
        self.assertAlmostEqual(res, "error", 3)

    def test_negative_area(self):
        res = area(-2)
        self.assertAlmostEqual(res, "error", 3)
if __name__ == "__main__":
    unittest.main()