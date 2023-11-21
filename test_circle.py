import unittest
from circle import area
from math import pi


class TestCircleArea(unittest.TestCase):

    def test_area(self):
        self.assertEqual (area(3),pi*3**2)
        self.assertEqual(area(1), pi )
        self.assertEqual(area(0),0)
        self.assertEqual(area(2.5), pi *2.5** 2)

    def test_values(self):
        self.assertRaises(ValueError,area,-2)
        self.assertRaises(ValueError,area,-1)

    def test_types(self):
        self.assertRaises(TypeError,area,5+2j)
        self.assertRaises(TypeError, area, 'five')
        self.assertRaises(TypeError, area, [16,22])
        self.assertRaises(TypeError, area, [42])
        self.assertRaises(TypeError, area, True)

