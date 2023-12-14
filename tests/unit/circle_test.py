import unittest

from circle import area, perimeter


class CircleTest(unittest.TestCase):
	def test_area(self):
		self.assertAlmostEqual(area(8), 201.062, delta=0.001)
		self.assertAlmostEqual(area(4), 50.266, delta=0.001)
		self.assertAlmostEqual(area(-34), 3631.681, delta=0.001)

	def test_perimeter(self):
		self.assertAlmostEqual(perimeter(4), 25.133, delta=0.001)
		self.assertAlmostEqual(perimeter(8), 50.266, delta=0.001)
		self.assertAlmostEqual(perimeter(-15), 94.248, delta=0.001)


if __name__ == "__main__":
	unittest.main()