import unittest
from square import area
from square import perimeter

class TestSquare(unittest.TestCase):
    
    def test_square_area_correct(self):
        res = area(12)
        self.assertEqual(res, 144)

    def test_square_area_wrong(self):
        res = area(-98)
        self.assertEqual(res, "negative number cannot be used")

    def test_square_area_null(self):
        res = area(0)
        self.assertEqual(res, "null cannot be used")

    def test_square_perimeter_correct(self):
        res = perimeter(42)
        self.assertEqual(res, 168)

    def test_square_perimter_wrong(self):
        res = perimeter(-245)
        self.assertEqual(res, "negative number cannot be used")

    def test_square_perimeter_null(self):
        res = perimeter(0)
        self.assertEqual(res, "null cannot be used")    
        
if __name__ == '__main__':
    unittest.main()
