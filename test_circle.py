import unittest
from circle import area,perimeter

class CircleTestCase(unittest.TestCase):
    def test_circle_area_norm(self):
        res = area(5)
        self.assertEqual(res, 78.53981633974483)

    def test_circle_area_neNorm(self):
        with self.assertEqual(ValueError):
            area(-5)
        
    def test_circle_area_real(self):
        res = area(5.5)
        self.assertEqual(res, 95.03317777109123)

    def test_circle_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_circle_perimeter_norm(self):
        res = perimeter(5)
        self.assertEqual(res, 31.41592653589793)

    def test_circle_perimeter_neNorm(self):
        with self.assertEqual(ValueError):
            perimeter(-5)

    def test_circle_perimeter_real(self):
        res = perimeter(5.5)
        self.assertEqual(res, 34.55751918948772)

    def test_circle_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

if __name__ == '__main__':
    unittest.main()
