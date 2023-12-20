import unittest
from square import area
from square import perimeter
class SquareTestCase(unittest.TestCase):
    def test_1_area(self):
        res = area(5)
        self.assertEqual(res, 25)

    def test_2_area(self):
        res = area(2)
        self.assertEqual(res, 4)
        
    def test_3_area(self):
        with self.assertRaises(ValueError) as context:
            area(-5)

    
    
    def test_4_area(self):
        with self.assertRaises(ValueError) as context:
            area(-5.5)


    def test_1_perimeter(self):
        res = perimeter(5)
        self.assertEqual(res, 20)

    def test_2_perimeter(self):
        res = perimeter(2)
        self.assertEqual(res, 8)

if __name__ == '__main__':
    unittest.main()
    
