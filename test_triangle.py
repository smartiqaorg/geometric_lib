import unittest
from triangle import area
from triangle import perimeter
class SquareTestCase(unittest.TestCase):
    def test_1_area(self):
        res = area(5,2)
        self.assertEqual(res, 5)

    def test_2_area(self):
        res = area(13,4)
        self.assertEqual(res, 26)

    def test_3_area(self):
        with self.assertRaises(ValueError) as context:
            area(-3, 4)
    


    def test_1_perimeter(self):
        res = perimeter(3,4,1)
        self.assertEqual(res, 8)

    def test_2_perimeter(self):
        res = perimeter(2, 3, 4)
        self.assertEqual(res, 9)

if __name__ == '__main__':
    unittest.main()
