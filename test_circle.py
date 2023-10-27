import unittest
from circle import area
from circle import perimeter
class RectangleTestCase(unittest.TestCase):
    def test_zero_r(self):
        resarea = area(0)
        resperimetr = area(0)
        self.assertEqual(resarea, 0)
        self.assertEqual(resperimetr, 0)
    def test_single_к(self):
        resarea = area(1)
        resperimetr = area(1)
        self.assertEqual(resarea, 3.141592653589793)
        self.assertEqual(resperimetr, 3.141592653589793)
    def test_examplefromdeclaration_к(self):
        resarea = area(4)
        resperimetr = area(4)
        self.assertEqual(resarea, 50.26548245743669)
        self.assertEqual(resperimetr, 50.26548245743669)