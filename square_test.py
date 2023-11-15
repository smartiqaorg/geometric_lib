from square import area
from square import perimeter

import unittest

class squareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_mul(self):
        res = area(7)
        self.assertEqual(res, 49)

    def test_perimeter_mul(self):
        res = perimeter(15)
        self.assertEqual(res, 60)