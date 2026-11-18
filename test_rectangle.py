import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    
    def test_area_zero(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
        
    def test_area_square(self):
        res = area(10, 10)
        self.assertEqual(res, 100)
        
    def test_area_negative(self):
        res = area(-5, 5)
        self.assertEqual(res, -25)

    def test_perimeter_positive(self):
        res = perimeter(2, 3)
        self.assertEqual(res, 10)
        
    def test_perimeter_zero(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

if __name__ == '__main__':
    unittest.main()