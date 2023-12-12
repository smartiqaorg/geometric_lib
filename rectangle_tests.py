import unittest
import geometric_lib.rectangle


class MyTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = geometric_lib.rectangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = geometric_lib.rectangle.area(10, 10)
        self.assertEqual(res, 100)