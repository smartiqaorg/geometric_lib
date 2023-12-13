import unittest

from square import area, perimeter
class TestSquare(unittest.TestCase):
   def test_area_1(self):
       result = area(10)
       self.assertEqual(result, 100)

   def test_area_2(self):
       result = area(9872874872482648727481914)
       self.assertEqual(result, 97473658247699277371350878924269926886479197103396)

   def test_area_3(self):
       res = area(-5)
       self.assertEqual(res, 0)
   def test_area_4(self):
       res = area(0)
       self.assertEqual(res, 0)




   def test_perimeter_1(self):
       result = perimeter(10)
       self.assertEqual(result, 40)

   def test_perimeter_2(self):
       result = perimeter(9872874872482648727481914)
       self.assertEqual(result, 39491499489930594909927656)

   def test_perimeter_3(self):
       res = perimeter(-5)
       self.assertEqual(res, 0)
   def test_perimeter_4(self):
       res = perimeter(0)
       self.assertEqual(res, 0)

if __name__ == "__main__":
    unittest.main()
