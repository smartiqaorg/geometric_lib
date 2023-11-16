import unittest
from triangle import area
from triangle import perimeter

class TriangleTestCase(unittest.TestCase):

    def test_triangle_area_correct(self):
        res = area(13, 24)
        self.assertEqual(res, 156)

    def test_triangle_area_wrong(self):
        res = area(-23, 124)
        self.assertRaises(res, Exception)

    def test_triangle_area_null(self):
        res = area(0, 2)
        self.assertEqual(res, 0)

    def test_triangle_perimeter_correct(self):
        res = perimeter(2, 4, 6)
        self.assertEqual(res, 12)

    def test_triangle_perimeter_wrong(self):
        res = perimeter(12, -19, 23)
        self.assertRaises(res, Exception)

    def test_triangle_perimeter_null(self):
        res = perimeter(0, 3 , 9)
        self.assertEqual(res, 12)
        
if __name__ == '__main__':
    unittest.main()
