import unittest
from circle import area
from circle import perimeter

class TestCircle(unittest.TestCase):
    
    def test_circle_area_correct(self):
        res = area(6)
        self.assertEqual(res, 113.09733552923255)
        
    def test_circle_area_wrong(self):
        res = area(-34)
        self.assertRaises(res, Exception)

    def test_circle_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_circle_perimeter_correct(self):
        res = perimeter(946)
        self.assertEqual(res, 5943.893300591889)

    def test_circle_perimeter_wrong(self):
        res = perimeter(-245)
        self.assertRaises(res, Exception)
        
    def test_circle_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
        
if __name__ == '__main__':
    unittest.main()
