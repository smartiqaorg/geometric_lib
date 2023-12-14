import unittest

from circle import area, perimeter


class CircleTest(unittest.TestCase):
	def test_area_correct(self):
		self.assertAlmostEqual(area(8), 201.062, delta=0.001)
		self.assertAlmostEqual(area(4), 50.266, delta=0.001)

	def test_area_value_error(self):
		self.assertRaises(ValueError, area, -34)

	def test_area_type_error(self):
		self.assertRaises(TypeError, area, "str")

	def test_perimeter_correct(self):
		self.assertAlmostEqual(perimeter(4), 25.133, delta=0.001)
		self.assertAlmostEqual(perimeter(8), 50.266, delta=0.001)

	def test_perimeter_value_error(self):
		self.assertRaises(ValueError, perimeter, -15)

	def test_perimeter_type_error(self):
		self.assertRaises(TypeError, perimeter, "str")


if __name__ == "__main__":
	unittest.main()