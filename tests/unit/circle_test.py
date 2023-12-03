import unittest

from circle import area, perimeter


class CircleTest(unittest.TestCase):
	def test_area(self):
		self.assertAlmostEqual(area(8), 201.06192982974676)
		self.assertAlmostEqual(area(4), 50.26548245743669)
		self.assertAlmostEqual(area(34), 3631.6811075498013)

	def test_perimeter(self):
		self.assertAlmostEqual(perimeter(4), 25.132741228718345)
		self.assertAlmostEqual(perimeter(8), 50.26548245743669)
		self.assertAlmostEqual(perimeter(15), 94.24777960769379)


if __name__ == "__main__":
	unittest.main()