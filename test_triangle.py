import unittest
from triangle import area
from triangle import perimeter
class RectangleTestCase(unittest.TestCase):
    def test_zero_ab(self):
        resarea = area(0,0)
        resperimetr = perimeter(0,0,0)
        self.assertEqual(resarea, 0)
        self.assertEqual(resperimetr, 0)
    def test_single_ab(self):
        resarea = area(1,1)
        resperimetr = perimeter(1,1,1)
        self.assertEqual(resarea, 0.5)
        self.assertEqual(resperimetr, 3)
    def test_examplefromdeclaration_ab(self):
        resarea = area(4,4)
        resperimetr = perimeter(4,4,4)
        self.assertEqual(resarea, 8)
        self.assertEqual(resperimetr, 12)