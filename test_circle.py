import unittest
import circle


class CircleTestCase(unittest.TestCase):
    def test_area(self):
        cases = [
            (4, 50.26548, None),
            (0, 0, None),
            (1, 3.14159, None),
            (2.5, 19.63495, None),
            (10, 314.15926, None),
            # ("4", None, TypeError),
            # (None, None, TypeError),
            # ("abc", None, TypeError),
            # (-4, None, ValueError),
            # (-0.5, None, ValueError),
        ]
        for r, expected, expected_exc in cases:
            with self.subTest(r=r):
                if expected_exc:
                    with self.assertRaises(expected_exc):
                        circle.area(r)
                else:
                    self.assertAlmostEqual(circle.area(r), expected, places=4)

    def test_perimeter(self):
        cases = [
            (4, 25.13274, None),
            (0, 0, None),
            (1, 6.28318, None),
            (2.5, 15.70796, None),
            (10, 62.83185, None),
            # ("4", None, TypeError),
            # (None, None, TypeError),
            # ("abc", None, TypeError),
            # (-4, None, ValueError),
            # (-0.5, None, ValueError),
        ]
        for r, expected, expected_exc in cases:
            with self.subTest(r=r):
                if expected_exc:
                    with self.assertRaises(expected_exc):
                        circle.perimeter(r)
                else:
                    self.assertAlmostEqual(circle.perimeter(r), expected, places=4)


if __name__ == "__main__":
    unittest.main()