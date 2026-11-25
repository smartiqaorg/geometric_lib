import unittest
import square


class SquareTests(unittest.TestCase):
    def test_area(self):
        result = square.area(5)
        self.assertEqual(result, 25)

    def test_perimeter(self):
        result = square.perimeter(5)
        self.assertEqual(result, 20)