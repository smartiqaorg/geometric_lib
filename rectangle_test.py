import unittest
from rectangle import area
from rectangle import perimeter

class RectangleTestCase(unittest.TestCase):

    def test_rectangle_area_correct(self):
        res = area(12, 15)
        self.assertEqual(res, 180)

    def test_rectangle_area_wrong(self):
        res = area(324, -234)
        self.assertEqual(res, "negative number cannot be used")

    def test_rectangle_area_null(self):
        res = area(10, 0)
        self.assertEqual(res, "null cannot be used")

    def test_rectangle_perimeter_correct(self):
        res = perimeter(42, 36)
        self.assertEqual(res, 156)

    def test_rectangle_perimeter_wrong(self):
        res = perimeter(1, 3)
        self.assertEqual(res, "negative number cannot be used")

    def test_rectangle_perimeter_null(self):
        res = perimeter(0, 35567)
        self.assertEqual(res, "null cannot be used")
        
if __name__ == '__main__':
    unittest.main()
