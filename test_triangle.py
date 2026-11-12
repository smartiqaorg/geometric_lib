import unittest
import triangle


class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        cases = [
            ((10, 5), 25, None),
            ((0, 5), 0, None),
            ((3, 4), 6, None),
            ((1.5, 2), 1.5, None),
            ((8, 5), 20, None),
            (("6", 8), None, TypeError),
            ((6, "8"), None, TypeError),
            ((None, 8), None, TypeError),
            ((-6, 8), None, ValueError),
            ((6, -1), None, ValueError),
        ]
        for (a, h), expected, expected_exc in cases:
            with self.subTest(a=a, h=h):
                if expected_exc:
                    with self.assertRaises(expected_exc):
                        triangle.area(a, h)
                else:
                    self.assertAlmostEqual(triangle.area(a, h), expected, places=4)

    def test_perimeter(self):
        cases = [
            ((6, 8, 10), 24, None),
            ((0, 0, 0), 0, None),
            ((3, 4, 5), 12, None),
            ((1.5, 2, 2.5), 6, None),
            ((10, 10, 10), 30, None),
            (("6", 8, 10), None, TypeError),
            ((6, 8, "10"), None, TypeError),
            ((-6, 8, 10), None, ValueError),
            ((6, -8, 10), None, ValueError),
        ]
        for (a, b, c), expected, expected_exc in cases:
            with self.subTest(a=a, b=b, c=c):
                if expected_exc:
                    with self.assertRaises(expected_exc):
                        triangle.perimeter(a, b, c)
                else:
                    self.assertAlmostEqual(triangle.perimeter(a, b, c), expected, places=4)


if __name__ == "__main__":
    unittest.main()