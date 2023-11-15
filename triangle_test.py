from triangle import area
from  triangle import perimeter

import unittest

class triangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(15,0)
        self.assertEqual(res, 0)

    def test_area_mul(self):
        res = area(10, 20)
        self.assertEqual(res, 100)

    def test_perimeter_mul(self):
        res = perimeter(14, 10, 56)
        self.assertEqual(res, 80)