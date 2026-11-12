import unittest
import rectangle


class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        cases = [
            ((2, 6), 12, None),
            ((0, 7), 0, None),
            ((5, 5), 25, None),
            ((0.3, 0.4), 0.12, None),
            ((10, 10), 100, None),
            (("2", 6), None, TypeError),
            ((6, None), None, TypeError),
            (("a", "b"), None, TypeError),
            ((-2, 6), None, ValueError),
            ((2, -6), None, ValueError),
        ]
        for (a, b), expected, expected_exc in cases:
            with self.subTest(a=a, b=b):
                if expected_exc:
                    with self.assertRaises(expected_exc):
                        rectangle.area(a, b)
                else:
                    self.assertAlmostEqual(rectangle.area(a, b), expected, places=4)

    def test_perimeter(self):
        cases = [
            ((2, 6), 16, None),
            ((0, 0), 0, None),
            ((5, 5), 20, None),
            ((1.5, 3.5), 10, None),
            ((10, 10), 40, None),
            (("2", 6), None, TypeError),
            ((6, ""), None, TypeError),
            ((None, 6), None, TypeError),
            ((-2, 6), None, ValueError),
            ((2, -0.5), None, ValueError),
        ]
        for (a, b), expected, expected_exc in cases:
            with self.subTest(a=a, b=b):
                if expected_exc:
                    with self.assertRaises(expected_exc):
                        rectangle.perimeter(a, b)
                else:
                    self.assertAlmostEqual(rectangle.perimeter(a, b), expected, places=4)


if __name__ == "__main__":
    unittest.main()