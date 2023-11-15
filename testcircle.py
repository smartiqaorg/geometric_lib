import unittest
from math import pi
from circle import area , perimeter


class MyTestCase(unittest.TestCase):
    def test_normaly_circle_square(self):
        data = area(10)
        self.assertEqual(data , 100 * pi)

    def test_zero_circle_square(self):
        data = area(0)
        self.assertEqual(data , 0)

    def test_string_circle_square(self):
        try:
            data = area('10')
        except Exception as e:
            data = e.__class__
        self.assertEqual(data , TypeError , "Incorrect input : string")

    def test_negative_circle_square(self):
        try:
            data = area(-10)
        except Exception as e:
            data = e.__class__
        self.assertEqual(data , TypeError , "Incorrect input : negative")

    def test_normaly_circle_perimeter(self):
        data = perimeter(10)
        self.assertEqual(data , 20*pi)

    def test_zero_circle_perimeter(self):
        data = perimeter(0)
        self.assertEqual(data , 0)

    def test_string_circle_perimeter(self):
        try:
            data = perimeter('10')
        except Exception as e:
            data = e.__class__
        self.assertEqual(data , TypeError , "Incorrcet input : string")

    def test_negative_circle_perimeter(self):
        try:
            data = area(-10)
        except Exception as e:
            data = e.__class__
        self.assertEqual(data , TypeError , "Incorrect input : negative")

