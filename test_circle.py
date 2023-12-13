import unittest
import math

from circle import area, perimeter
class Testcircle(unittest.TestCase):
   def test_area_1(self):
       result = area(10)
       self.assertEqual(result, math.pi*100)

   def test_area_2(self):
       result = area(-5)
       self.assertEqual(result, 0)




   def test_perimeter_1(self):
       result = perimeter(5)
       self.assertEqual(result, 2 * math.pi * 5)

   def test_perimeter_2(self):
       result = perimeter(0)
       self.assertEqual(result, 0)

if __name__ == "__main__":
    unittest.main()
