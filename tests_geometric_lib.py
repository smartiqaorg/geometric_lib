import unittest
from circle import area as circle_area, perimeter as circle_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter

class TestGeometricLib(unittest.TestCase):
    # Circle tests (Area)
    def test_circle_area_r_0(self):
        self.assertAlmostEqual(circle_area(0), 0)

    def test_circle_area_r_1(self):
        self.assertAlmostEqual(circle_area(1), 3.141592653589793)

    def test_circle_area_r_2_5(self):
        self.assertAlmostEqual(circle_area(2.5), 19.634954084936208)

    def test_circle_area_r_0_001(self):
        self.assertAlmostEqual(circle_area(0.001), 3.1415926535897933e-06)

    # Circle tests (Perimeter)
    def test_circle_perimeter_r_0(self):
        self.assertAlmostEqual(circle_perimeter(0), 0)

    def test_circle_perimeter_r_1(self):
        self.assertAlmostEqual(circle_perimeter(1), 6.283185307179586)

    def test_circle_perimeter_r_2_5(self):
        self.assertAlmostEqual(circle_perimeter(2.5), 15.707963267948966)

    def test_circle_perimeter_r_0_001(self):
        self.assertAlmostEqual(circle_perimeter(0.001), 0.006283185307179587)

    # Square tests (Area)
    def test_square_area_a_0(self):
        self.assertAlmostEqual(square_area(0), 0)

    def test_square_area_a_1(self):
        self.assertAlmostEqual(square_area(1), 1)

    def test_square_area_a_2_5(self):
        self.assertAlmostEqual(square_area(2.5), 6.25)

    def test_square_area_a_0_001(self):
        self.assertAlmostEqual(square_area(0.001), 1e-06)

    # Square tests (Perimeter)
    def test_square_perimeter_a_0(self):
        self.assertAlmostEqual(square_perimeter(0), 0)

    def test_square_perimeter_a_1(self):
        self.assertAlmostEqual(square_perimeter(1), 4)

    def test_square_perimeter_a_2_5(self):
        self.assertAlmostEqual(square_perimeter(2.5), 10.0)

    def test_square_perimeter_a_0_001(self):
        self.assertAlmostEqual(square_perimeter(0.001), 0.004)

    # Rectangle tests (Area)
    def test_rectangle_area_a_0_b_0(self):
        self.assertAlmostEqual(rectangle_area(0, 0), 0)

    def test_rectangle_area_a_1_b_2(self):
        self.assertAlmostEqual(rectangle_area(1, 2), 2)

    def test_rectangle_area_a_2_5_b_5_0(self):
        self.assertAlmostEqual(rectangle_area(2.5, 5.0), 12.5)

    def test_rectangle_area_a_0_001_b_1000(self):
        self.assertAlmostEqual(rectangle_area(0.001, 1000), 1)

    # Rectangle tests (Perimeter)
    def test_rectangle_perimeter_a_0_b_0(self):
        self.assertAlmostEqual(rectangle_perimeter(0, 0), 0)

    def test_rectangle_perimeter_a_1_b_2(self):
        self.assertAlmostEqual(rectangle_perimeter(1, 2), 6)

    def test_rectangle_perimeter_a_2_5_b_5_0(self):
        self.assertAlmostEqual(rectangle_perimeter(2.5, 5.0), 15.0)

    def test_rectangle_perimeter_a_0_001_b_1000(self):
        self.assertAlmostEqual(rectangle_perimeter(0.001, 1000), 2000.002)

    # Triangle tests (Area)
    def test_triangle_area_a_0_h_0(self):
        self.assertAlmostEqual(triangle_area(0, 0), 0)

    def test_triangle_area_a_1_h_2(self):
        self.assertAlmostEqual(triangle_area(1, 2), 1)

    def test_triangle_area_a_2_5_h_5(self):
        self.assertAlmostEqual(triangle_area(2.5, 5.0), 6.25)

    def test_triangle_area_a_0_001_h_1000(self):
        self.assertAlmostEqual(triangle_area(0.001, 1000), 0.5)

    # Triangle tests (Perimeter)
    def test_triangle_perimeter_a_0_b_0_c_0(self):
        self.assertAlmostEqual(triangle_perimeter(0, 0, 0), 0)

    def test_triangle_perimeter_a_1_b_2_c_3(self):
        self.assertAlmostEqual(triangle_perimeter(1, 2, 3), 6)

    def test_triangle_perimeter_a_2_5_b_5_0_c_7_5(self):
        self.assertAlmostEqual(triangle_perimeter(2.5, 5.0, 7.5), 15.0)

    def test_triangle_perimeter_a_0_001_b_1000_c_10(self):
        self.assertAlmostEqual(triangle_perimeter(0.001, 1000, 10), 1010.001)
         

if __name__ == '__main__':
    unittest.main()