import unittest
import square


class SquareTestCase(unittest.TestCase):
    def test_area(self):
        cases = [
            (3, 9, None),
            (0, 0, None),
            (2, 4, None),
            (0.5, 0.25, None),
            (10, 100, None),
            ("3", None, TypeError),
            ("", None, TypeError),
            (None, None, TypeError),
            (-3, None, ValueError),
            (-0.5, None, ValueError),
        ]
        for a, expected, expected_exc in cases:
            with self.subTest(a=a):
                if expected_exc:
                    with self.assertRaises(expected_exc):
                        square.area(a)
                else:
                    self.assertAlmostEqual(square.area(a), expected, places=4)

    def test_perimeter(self):
        cases = [
            (3, 12, None),
            (0, 0, None),
            (2, 8, None),
            (1.5, 6, None),
            (10, 40, None),
            ("3", None, TypeError),
            (None, None, TypeError),
            ("abc", None, TypeError),
            (-3, None, ValueError),
            (-0.1, None, ValueError),
        ]
        for a, expected, expected_exc in cases:
            with self.subTest(a=a):
                if expected_exc:
                    with self.assertRaises(expected_exc):
                        square.perimeter(a)
                else:
                    self.assertAlmostEqual(square.perimeter(a), expected, places=4)


if __name__ == "__main__":
    unittest.main()