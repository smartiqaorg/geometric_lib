from triangle import *
import unittest
class CircleTestCase(unittest.TestCase):

    def test_zero_area(self):

        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_zero_perim(self):

        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)
