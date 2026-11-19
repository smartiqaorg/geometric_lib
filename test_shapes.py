import unittest
import circle
import rectangle
import square
import triangle

class TestGeometricLib(unittest.TestCase):

    def test_circle_area(self):
        self.assertAlmostEqual(circle.area(5), 78.54, places=2)

    def test_circle_perimeter(self):
        self.assertAlmostEqual(circle.perimeter(5), 31.42, places=2)

    def test_rectangle_area(self):
        self.assertEqual(rectangle.area(10, 5), 50)

    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle.perimeter(10, 5), 30)

    def test_square_area(self):
        self.assertEqual(square.area(4), 16)

    def test_square_perimeter(self):
        self.assertEqual(square.perimeter(4), 16)

    def test_triangle_area(self):
        self.assertEqual(triangle.area(4, 3), 6.0)

    def test_triangle_perimeter(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)

if __name__ == '__main__':
    unittest.main()