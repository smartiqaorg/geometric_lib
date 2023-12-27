import unittest
from circle import area,perimeter

class CircleTestCase(unittest.TestCase):
    def test_circle_area_norm(self):
        res = area(5)
        self.assertAlmostEqual(res, 78.540,delta = 0.1)

    def test_circle_area_neNorm(self):
        with self.assertRaises(ValueError):
            area(-6)
        
    def test_circle_area_real(self):
        res = area(5.5)
        self.assertAlmostEqual(res, 95.033,delta = 0.1)

    def test_circle_area_zero(self):
        res = area(0) 
        self.assertEqual(res, 0)

    def test_circle_perimeter_norm(self):
        res = perimeter(5)
        self.assertAlmostEqual(res, 31.416, delta = 0.1)

    def test_circle_perimeter_neNorm(self):
        with self.assertRaises(ValueError):
            perimeter(-5)

    def test_circle_perimeter_real(self):
        res = perimeter(5.5)
        self.assertAlmostEqual(res, 34.558, delta = 0.1)

    def test_circle_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

if __name__ == '__main__':
    unittest.main()
