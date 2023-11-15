import unittest
from circle import *
class CircleTestCase(unittest.TestCase):

    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_zero_perim(self):

        res = perimeter(0)
        self.assertEqual(res, 0)
