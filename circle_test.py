from circle import area
from circle import perimeter

import unittest

class circleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_mul(self):
        res = area(10)
        self.assertEqual(res, 314.1592653589793)

    def test_perimeter_mul(self):
        res = perimeter(15)
        self.assertEqual(res, 94.24777960769379)